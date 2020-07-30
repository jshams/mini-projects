class Eval():
    def __init__(self, expression_string=None):
        '''break up this expression into a list while checking if the input
        is valid. Next solve the expression and store the result in
        self.solution.

        raises: ValueError if expression_string is invalid.'''
        self.expression_string = expression_string
        self.expression_list = None
        self.solution = None

        if expression_string is not None:
            self._get_expression_list()
            if not self._has_valid_parentheses():
                raise ValueError('Invalid input, fix parentheses.')
            self.solution = self.solve()

    def __repr__(self):
        return self.expression_string

    def _get_expression_list(self):
        '''given an expression in the form of a string
        return the expression in the form of a list

        raises: ValueError - if the given expression string is invalid'''
        # these are the symbols we want to look out for
        symbols = set('^*/+-')
        # create an array to store the split up expression
        expression_list = []
        # iterate through each char in the expression string
        for char in self.expression_string:
            # check if the char is in our set of symbols
            if char in symbols:
                if len(expression_list) > 0 and expression_list[-1] in symbols:
                    raise ValueError('Invalid string input')
                # if so add the symbol to our list
                expression_list.append(char)
            # otherwise check if our char is a digit
            elif char.isdigit():
                # make sure expression list has a len > 0 to avoid index error
                if len(expression_list) > 0:
                    # check if the last index of our array is also an int
                    if type(expression_list[-1]) == int:
                        # if so add the char (string) to that int and convert
                        # them to an int
                        expression_list[-1] = int(
                            str(expression_list[-1]) + char)
                    # ADD FLOAT FUNCTIONALITY HERE
                else:
                    # otherwise just add the char in int form
                    expression_list.append(int(char))
            elif char == '.':
                if type(expression_list[-1]) == int:
                    expression_list[-1] = float(expression_list[-1])
                else:
                    raise ValueError('Invalid string input. "." out of place.')

        # once we traverse the string return what we've collected
        self.expression_list = expression_list

    def _find(self, arr, item, item2=None):
        '''find the first instance of up to 2 items in an array and return its
        index.
        Example: arr=["a", "b", "c", "d"], item="b" --> 1
        Explanation: the item "b" is found at the oneth index.
        '''
        for i, char in enumerate(arr):
            if char == item or char == item2:
                return i

    def _find_num_of_occurances(self, arr, item, item2=None):
        '''given an array and an item, return the number of times that item is
        present in the array. If a second item is given, return the total
        number of times either is seen.'''
        # keep track of the number of occurancees
        num_occurances = 0
        # iterate over the chars in the array
        for char in arr:
            # check if thee char matches the given items
            if char == item or char == item2:
                # if so, increment num occurances by 1
                num_occurances += 1
        # return the number of occurances found
        return num_occurances

    def exponents(self, part):
        '''return the inputted array with the first exponents evaluated'''
        # find the index of the first instance of ^
        i = self._find(part, '^')
        # evaluate whats around it
        result = part[i - 1] ** part[i + 1]
        # remove the evaluated vals
        part.pop(i)
        # remove the evaluated vals
        part.pop(i)
        # input the result in place
        part[i - 1] = result
        # return the manipulated array
        return part

    def multiplication_or_division(self, part):
        '''return the inputted array with the first multiplication or division evaluated'''
        # find the index of the first instance of * or
        i = self._find(part, '*', '/')
        # if mult
        if part[i] == '*':
            # calculate the product
            result = part[i - 1] * part[i + 1]
        # otherwise: part[i] == '/'
        else:
            # calculate the quotient
            result = part[i - 1] / part[i + 1]
        # remove the evaluated vals
        part.pop(i)
        # remove the evaluated vals
        part.pop(i)
        # input the result in place
        part[i - 1] = result
        # return the manipulated array
        return part

    def addition_or_subtraction(self, part):
        '''return the inputted array with the first addition or subtraction
        evaluated'''
        # find the index of the first instance of '+' or '-'
        i = self._find(part, '+', '-')
        # if addition
        if part[i] == '+':
            # calculate the sum
            result = part[i - 1] + part[i + 1]
        # otherwise subtraction
        else:
            # calculate the difference
            result = part[i - 1] - part[i + 1]
        # remove the evaluated vals
        part.pop(i)
        # remove the evaluated vals
        part.pop(i)
        # input the result in place
        part[i - 1] = result
        # return the manipulated array
        return part

    def order_emdas(self, part):
        '''given an expression list without parentheses evaluate it
        exponents, then multiplication and division, then addition and subtraction'''

        # for the number of times an exponent appears:
        for _ in range(self._find_num_of_occurances(part, '^')):
            # evaluate the first instance of expoenent
            part = self.exponents(part)

        # for the number of times a mult or div appears
        for _ in range(self._find_num_of_occurances(part, '*', '/')):
            # evaluate the first instance of mult or div
            part = self.multiplication_or_division(part)

        # for the number of times a add or sub appears
        for _ in range(self._find_num_of_occurances(part, '+', '-')):
            # evaluate the first instance of add or sub
            part = self.addition_or_subtraction(part)

        # length of part should be 1 so we can return whats left, the
        # evaluated statement
        return part[0]

    def _has_valid_parentheses(self):
        '''returns a boolean indicating whether the expression string has valid
        parentheses.'''
        # keep track of the number of opened parentheses seen
        num_opened = 0
        # iterate over the characters in the expression
        for char in self.expression_string:
            # when an opening parentheses is seen increment num_opened by 1
            if char == '(':
                num_opened += 1
            # when a closing parentheses is seen
            elif char == ')':
                # if num opened is 0, no opening parenthses match this closing
                if num_opened == 0:
                    # return false deeming the expression invalid
                    return False
                # otherwise decrement num_opened
                num_opened -= 1
        # if num opened is 0, return true, otherwise false
        return num_opened == 0

    def _find_set_parentheses(self, expression):
        '''finds a set of parentheses that do not have any sub parentheses and
        returns the indices of the opening and closing parentheses in a tuples
        in respective order. If no parentheses are found the function returns
        None.'''
        # keep track of the last opening parentheses
        last_opening_par_index = None
        for i, char in enumerate(expression):
            # if the char is an opening parentheses store its index
            if char == '(':
                last_opening_par_index = i
            # when a closing parentheses is found
            if char == ')':
                # return the opening and closing indices
                return last_opening_par_index, i
        # if none are found, return None
        return None

    def solve_set_of_parentheses(self):
        '''solves the first set of parentheses (that have no sub parentheses)
        and updates this expression string with the solution. If none are
        found, None is returned'''
        # find a set of parentheses to solve
        par_set = self._find_set_parentheses(self.expression_list)
        # if the return is None, none have been found, return None
        if par_set is None:
            return None
        # unpack the resulting parentheses set
        open_par, closing_par = par_set
        # create a sub expression from a slice of the larger
        sub_expression = self.expression_list[open_par + 1: closing_par]
        # solve the subproblem
        sub_solution = self.order_emdas(sub_expression)
        # replace the subproblem with the solved result
        self.expression_list = self.expression_list[:open_par] + [
            sub_solution] + self.expression_list[closing_par + 1:]

    def solve_parentheses(self):
        '''searches for subproblems enclosed in parentheses and solves them
        until no more parentheses are found'''
        # while parentheses pairs exist, solve them. If the return is None
        # there are no more parentheses to solve and the while loop will exit
        while self.solve_set_of_parentheses() is not None:
            continue

    def solve(self):
        '''solves the equation by solving all sub parentheses, the calling
        order emdas on the remaining equation.'''
        # solve parentheses first
        self.solve_parentheses()
        # solve the rest
        return self.order_emdas(self.expression_list)


if __name__ == '__main__':
    method = Eval(
        '(22 + (17) * (14)) + 69 * 23 + (32 / 2 + (12 + 4) + 2 ^ 6)')
    print(method)
    solution = method.solution
    print(solution)
