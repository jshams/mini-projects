from question import Question
from decision_node import DecisionNode
from leaf_node import LeafNode

class DecisionTree:
    def __init__(self, data, features):
        '''initialize a decision tree with features and data'''
        self.data = data
        self.features = features
        self.root = self.build_tree(self.data)

    def build_tree(self, rows, parent=None):
        '''takes the data and recursively builds a tree'''
        gain, best_question = self.find_best_split(rows)
        if gain == 0:
            return LeafNode(self.label_counts(rows))
        true_rows, false_rows = self.partition(rows, best_question)
        true_branch = self.build_tree(true_rows)
        false_branch = self.build_tree(false_rows)
        return DecisionNode(best_question, true_branch, false_branch)
    
    def __iter__(self):
        '''iterate through the tree using DFS'''
        for node, d in self.traverse_dfs(lambda item, j:item):
            yield node

    def traverse_dfs(self, visit,node=None, depth=0):
        '''traverse the tree using DFS and applying a visit function to each node'''
        if node is None:
            node = self.root
        visit(node, depth)
        # print(node)
        if not isinstance(node, LeafNode):
            # visit(node.true_branch, depth)
            self.traverse_dfs(visit, node.true_branch, depth + 1)
            # visit(node.false_branch, depth)
            self.traverse_dfs(visit, node.false_branch, depth + 1)
        
    def __repr__(self, node=None, indent=None, result=None):
        if result == None:
            result = ''
        if indent == None:
            indent = ''
        if node is None:
            node = self.root
        # Base case: we've reached a leaf
        if isinstance(node, LeafNode):
            return f'{indent}Prediction: {node.probabilities}\n'
        
        # Print the question at this node
        result += f'{indent} {node.question}\n'
        indent += '\t'

        # Call this function recursively on the true branch
        result += f'{indent}|--> True:\n'
        result += self.__repr__(node.true_branch, indent + '|\t', result)

        # Call this function recursively on the false branch
        result += f'{indent}|--> False:\n'
        result += self.__repr__(node.false_branch, indent + '|\t', result)
        # print(node)
        # print(result)
        return result

    def find_best_split(self, rows):
        '''finds the best split of data using gini index and information gain'''
        max_gain = 0
        best_question = None

        current_uncertainty = self.gini_index(rows)

        for col_index in range(len(rows[0]) - 1):
            values = set([row[col_index] for row in rows])
            
            for val in values:
                q = Question(col_index, val, self.features[col_index])
                true_rows, false_rows = self.partition(rows, q)
                if len(true_rows) == 0 or len(false_rows) == 0:
                    continue
                else:
                    gain = self.info_gain(true_rows, false_rows, current_uncertainty)
                if gain >= max_gain:
                    max_gain = gain
                    best_question = q

        return max_gain, best_question

    def info_gain(self, true_rows, false_rows, uncertainty):
        '''returns the information gain of split data'''
        p = len(true_rows) / (len(false_rows) + len(true_rows))
        left_gini = self.gini_index(true_rows)
        right_gini = self.gini_index(false_rows)
        return uncertainty - p * left_gini - (1 - p) * right_gini

    def gini_index(self, rows):        
        '''this can be better'''
        counts = self.label_counts(rows)
        impurity = 1
        for count in counts.values():
            p_label = count / len(rows)
            impurity -= p_label**2
        return impurity
    
    def label_counts(self, rows):
        '''given data this will return a histogram of values in the label (last) column'''
        label_hist = {}
        for row in rows:
            label = row[-1]
            if label not in label_hist:
                label_hist[label] = 1
            else:
                label_hist[label] += 1
        return label_hist

    def partition(self, rows, question):
        '''iterate through data asking a question on each row and partitioning the
        data based on the answer'''
        true_rows, false_rows = [], []
        for row in rows:
            if question.satisfy(row):
                true_rows.append(row)
            else:
                false_rows.append(row)
        return true_rows, false_rows

    def classify(self, row, node=None):
        '''given a row input the tree can predict its outcome'''
        if node is None:
            node = self.root
        if isinstance(node, LeafNode):
            return node.probabilities
        if node.question.satisfy(row):
            return self.classify(row, node.true_branch)
        else:
            return self.classify(row, node.false_branch)


if __name__ == '__main__':
    training_data = [
        ['Green', 3, 'Apple'],
        ['Yellow', 3,'Apple'],
        ['Red', 1, 'Grape'],
        ['Red', 1, 'Grape'],
        ['Yellow', 3, 'Lemon']]
    feature_names = ['color', 'diameter', 'fruit']
    dt = DecisionTree(training_data, feature_names)
    print(dt)