class DecisionNode:
    def __init__(self, question, true_branch, false_branch):
        '''initialize a decision node with a question and its two branches'''
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch