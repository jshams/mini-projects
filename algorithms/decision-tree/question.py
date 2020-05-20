class Question:
    def __init__(self, col_index, val, col_name):
        '''initialize a question object with a column index, and a val
        to ask a question on'''
        self.col_index = col_index
        self.val = val
        self.col_name = col_name
    
    def is_numeric(self, data):
        '''indicates whether data is a number'''
        return type(data) == int or type(data) == float
        # return isinstance(data (int, float))

    def satisfy(self, example):
        example_val = example[self.col_index]
        if self.is_numeric(example_val):
            return example_val >= self.val
        else:
            return example_val == self.val
    
    def __repr__(self):
        condition = '>='
        if not self.is_numeric(self.val):
            condition = 'equal to'
        return f'Is {self.col_name} {condition} {self.val}?'