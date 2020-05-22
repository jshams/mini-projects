from random import random
from math import sqrt


class KMeans():
    def __init__(self, n_clusters):
        '''initializes KMeans with n_clusters number of clusters'''
        self.n_clusters = n_clusters
        self.X = None
        self.Y = None
        self.min_x = None
        self.max_x = None
        self.min_y = None
        self.max_y = None
        self.cluster_centers_ = None

    def fit(self, X):
        '''params: X: a 2d list of x, y coordinates
        takes X, a 2d array of coordinates and unzips it into two X and Y arrays
        Sets cluster_centers_ to the result of k_means'''
        # create lists to store x and y values
        self.X = []
        self.Y = []
        # iterate though the x and y vals in X
        for x, y in X:
            # add the x or y to X or Y
            self.X.append(x)
            self.Y.append(y)
        # set cluster_centers equal to the calculation of k_means
        self.cluster_centers_ = self._k_means()

    def distance(self, x1, y1, x2, y2):
        '''params: x1, y1, x2, y2: float
        returns: the difference of points (x1,y1) and (x2,y2)'''
        # distance formula: a^2 + b^2 = c^2
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def find_closest_cluster(self, x, y, clusters):
        '''params: x, y, clusters
        x, y: float
        clusters: 2d array. list of cluster coordinates
        returns: the closest cluster_center to the point x,y'''
        # keep track of the closest point and its distance
        min_dist_cluster = None
        min_dist = float('inf')
        # for each cluster center
        for cluster_x, cluster_y in clusters:
            # find its distance to (x,y)
            dist = self.distance(x, y, cluster_x, cluster_y)
            # if the distance is less than min distance
            if dist < min_dist:
                # update min distance with this dist
                min_dist = dist
                # also update min_dist_cluster with the cluster's points
                min_dist_cluster = (cluster_x, cluster_y)
        # once we've gone through all the points the closest point is min_dist_cluster
        return min_dist_cluster

    def average(self, x_y_list):
        '''params: x_y_list
        x_y_list: 2d array. list of points ([[x1,y1], [x2, y2], [x3, y3]...])
        returns the average of all points
        '''
        # if the length of the list is 0 (it has no closest points)
        # stretch: try to optimize this by wisely chosing its location
        # if the new point doesn't affect the other points we will have an infinite loop
        if len(x_y_list) == 0:
            # return a random coordinate so it can find a new cluster
            random_x = (random() * abs(self.max_x - self.min_x)) + self.min_x
            random_y = (random() * abs(self.max_y - self.min_y)) + self.min_y
            return random_x, random_y
        # othewise
        else:
            # find and return the average of the points in its cluster
            x_tot = 0
            y_tot = 0
            for x, y in x_y_list:
                x_tot += x
                y_tot += y
            return x_tot / len(x_y_list), y_tot / len(x_y_list)

    def _k_means(self):
        '''using self.X, self.Y, self.n_clusters:
        self.X: array, list of x values
        self.Y: array, list of y values
        self.n_clusters: int, number of clusters
        This runs the K-Means algorithm on X and Y with n_clusters cluster-centers
        returns: 2d array, list of cluster-center coordinates
        '''
        # set current_clusters to None
        prev_cluster = None
        # create the next clusters by:
        # create a dictionary with keys being n_clusters random points from x_min, x_max to y_min, y_max (vals = [])
        current_clusters = {}
        # create a flag to see if we are on the first iteration
        first_iteration = True
        # while prev
        while prev_cluster != current_clusters:
            if first_iteration:
                first_iteration = False
                self.min_x, self.max_x = min(self.X), max(self.X)
                self.min_y, self.max_y = min(self.Y), max(self.Y)
                for _ in range(self.n_clusters):
                    random_x = (
                        random() * abs(self.max_x - self.min_x)) + self.min_x
                    random_y = (
                        random() * abs(self.max_y - self.min_y)) + self.min_y
                    current_clusters[(random_x, random_y)] = []
            else:
                # -- prev, current = current, {}
                prev_cluster, current_clusters = current_clusters, {}
                # -- for cluster-center in prev.keys():
                for centroid in prev_cluster.keys():
                    # cluster_mean = (avg_xs, avg_ys)
                    cluster_mean = self.average(prev_cluster[centroid])
                    # current[cluster_mean] = []
                    current_clusters[cluster_mean] = []
            # iterate through Xi, Yi in both x and y to add them to the
            for Xi, Yi in zip(self.X, self.Y):
                # find the cluster-center this (Xi, Yi) point is closest to
                closest_cluster = self.find_closest_cluster(
                    Xi, Yi, current_clusters.keys())
                # add it, (Xi ,Yi) to that clusters val in dict
                current_clusters[closest_cluster].append((Xi, Yi))
        return list(current_clusters.keys())


def test_sucess_rate(n):
    '''will test KMeans n times and print its success rate'''
    passed = n
    for _ in range(100):
        try:
            km = KMeans(2)
            km.fit([(1, 1), (2, 2), (3, 3)])
        except TypeError:
            passed -= 1
    print('Passed:', passed, '/ 100')


def get_data(FILENAME='sample_blob.txt'):
    X = []
    f = open(FILENAME)
    for line in f.readlines():
        split_line = line.split(', ')
        coords = (float(num) for num in split_line)
        X.append(tuple(coords))
    f.close()
    return X


X = get_data()

km = KMeans(4)
km.fit(X)
[print(center) for center in sorted(km.cluster_centers_)]
