from random import random
from math import sqrt


class NotFittedError(Exception):
    pass


class KMeans():
    def __init__(self, n_clusters):
        '''initializes KMeans with n_clusters number of clusters'''
        self.n_clusters = n_clusters
        self.data_width = None
        self.X = None
        self.mins = None
        self.maxs = None
        self.cluster_centers_ = None
        self.n_epochs = 0

    def fit(self, X):
        '''params: X: an Nd list of x, y coordinates
        gets the information from the data and applies Kmeans'''
        # store the data
        self.X = X
        # store the width of the data
        self.data_width = len(X[0])

        # apply_k_means
        self.cluster_centers_ = self._k_means()

    @property
    def shape(self, X=None):
        '''returns the shape of an n dimensional array.
        does this by recursively checking the len of each first subarray.
        Assumes the shape is uniform throughout.'''
        if X is None:
            X = self.X
        try:
            x_len = len(X)
            inner_shape = self.shape(X[0]) if len(X) > 0 else 0
            return (x_len, *inner_shape)
        except TypeError:
            return tuple()

    def distance(self, l1, l2):
        '''params: l1 - iterable of float or int coordinates
        l2 - iterable of float or int coordinates
        returns: the euclidean distance from l1 to l2'''
        return sqrt(sum((x1 - x2) ** 2 for x1, x2 in zip(l1, l2)))

    def find_closest_cluster(self, coords, clusters):
        '''params: coords, iterable of coordinates (x, y, z, ...)
        clusters: 2d array. list of cluster coordinates
        returns: the closest cluster_center to the point x, y'''
        # keep track of the closest point and its distance
        nearest_cluster = None
        min_dist = float('inf')
        # for each cluster center
        for cluster in clusters:
            # find the distance from coords to this cluster
            dist = self.distance(coords, cluster)
            # if the distance is the shortest so far
            if dist < min_dist:
                # update min distance with this dist
                min_dist = dist
                # also update nearest_cluster with the cluster's points
                nearest_cluster = cluster
        # once we've gone through all the points the closest point is nearest_cluster
        return nearest_cluster

    def average(self, x_n_list):
        '''params: x_y_list
        x_y_list: 2d array. list of points([[x1, y1, z1...], [x2, y2, z2...], [x3, y3, z3...]...])
        returns the average coordinate of all coordinates.
        '''
        averages = (
            sum(row[i] for row in x_n_list) / len(x_n_list)
            for i in range(self.data_width)
        )
        return tuple(averages)

        # averages = []
        # for i in range(self.data_width):
        #     sum_column = sum(row[i] for row in x_n_list)
        #     averages.append(sum_column / len(x_n_list))
        # return averages

    def get_mins_and_maxs(self):
        mins = []
        maxs = []
        for i in range(self.data_width):
            col_min = min(row[i] for row in self.X)
            col_max = max(row[i] for row in self.X)
            mins.append(col_min)
            maxs.append(col_max)
        self.mins = mins
        self.maxs = maxs

    def generate_random_cluster_center(self):
        '''generates a random cluster center in bounds of the min and max
        of each point'''
        # get mins and maxs if need be (occurs on first call)
        if self.mins is None or self.maxs is None:
            self.get_mins_and_maxs()

        random_cluster = []
        for minimum, maximum in zip(self.mins, self.maxs):
            random_point = (random() * (maximum - minimum)) + minimum
            random_cluster.append(random_point)
        return tuple(random_cluster)

    def generate_random_centers(self):
        '''returns a generator that creates n_clusters new clusters'''
        return (self.generate_random_cluster_center() for _ in range(self.n_clusters))

    def epoch(self, prev_cluster):
        self.n_epochs += 1
        current_clusters = {}
        # -- for cluster-center in prev.keys():
        for centroid in prev_cluster.keys():
            # if this cluster center has no nearest points
            if len(prev_cluster[centroid]) == 0:
                # generate a new random cluster center
                cluster_mean = self.generate_random_cluster_center()
            else:
                # cluster_mean = (avg_xs, avg_ys)
                cluster_mean = self.average(prev_cluster[centroid])
            # current[cluster_mean] = []
            current_clusters[cluster_mean] = []
        # iterate through Xi, Yi in both x and y to add them to the
        for row in self.X:
            # find the cluster-center this row point is closest to
            closest_cluster = self.find_closest_cluster(
                row, current_clusters.keys())
            # add it, (Xi ,Yi) to that clusters val in dict
            current_clusters[closest_cluster].append(row)
        return current_clusters

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
        # create a dictionary with keys being clusters centers as tuples
        current_clusters = dict(
            (cluster_center, []) for cluster_center in self.generate_random_centers()
        )
        # while prev
        while prev_cluster != current_clusters:
            # the current cluster becomes the previous
            prev_cluster = current_clusters
            # update the current cluster after one epoch
            current_clusters = self.epoch(prev_cluster)
        # return the cluster centers
        return list(current_clusters.keys())

    def predict(self):
        if self.cluster_centers_ is None:
            raise NotFittedError(
                "This KMeans instance is not fitted yet. Call 'fit' with",
                'appropriate arguments before using this method')

    def display(self):
        pass


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

km = KMeans(6)
km.fit(X)
[print(center) for center in sorted(km.cluster_centers_)]
