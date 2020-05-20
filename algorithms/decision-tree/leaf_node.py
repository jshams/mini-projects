class LeafNode:
    '''initialize a leaf node with a prediction'''
    def __init__(self, predictions):
        self.predictions = predictions
        self.probabilities = self.get_probabilities()
    
    def get_probabilities(self):
        total = sum(self.predictions.values())
        probs = {}
        for val, count in self.predictions.items():
            probs[val] = 100 * (count / total)
        return probs