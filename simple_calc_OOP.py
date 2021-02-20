# simple calculator Using OOP

class Calc:

    def __init__(self):
        self.nums = {'numbers': []}
        self.opers = {'arith_opers': []}


    def prompt_num(self):
        '''
        take number input
        '''

        prompt = "\nPlease enter a number\n:>\t"

        while True:
            inp = input(prompt)

            try:
                num = float(inp)
            except:
                print(f"Error: {inp} is invalid!")
                continue
            return str(num) + ' '

    def prompt_oper(self):
        '''
        take arithmetic operator input
        '''

        print("\nPlease enter next operation below")

        prompt = "To add: '+',\nTo subtract: '-',\nTo multiply: '*',\nTo divide: '/'\n:>\t"

        acc_range = ['-', '+', '*', '/']

        while True:
            inp = input(prompt)

            if inp not in acc_range:
                print(f"Error: {inp} is invalid!")
                continue
            return inp + ' '


    def compute(self):

        # taking the first number
        self.nums['numbers'].append(self.prompt_num())

        # taking the first operator
        self.opers['arith_opers'].append(self.prompt_oper())

        # taking the second number
        self.nums['numbers'].append(self.prompt_num())


    def ask_to_cont(self):
        '''
        to decide if to compute calculation so far
        or input more numbers and operations
        '''

        print("\nTo continue, press enter\nFor result, enter '='")
        acc_range = ['', '=']
        while True:
            inp = input(":>\t")

            if inp not in acc_range:
                print(f"{inp} is invalid!")
                continue
            return inp


    def cont_calc(self):
        '''
        prompts user for operator first
        followed by number
        '''
        self.opers['arith_opers'].append(self.prompt_oper())
        self.nums['numbers'].append(self.prompt_num())

    def show_answer(self):

        expr = ''

        for (ind, num) in enumerate(self.nums['numbers']):
            expr += num
            if len(self.opers['arith_opers']) == ind:
                continue
            expr += self.opers['arith_opers'][ind]
            continue

        print('\n'*2, \
        f"\n***********************************\
        \n{expr} = \
        \n{eval(expr)}\
        \n***********************************")

    def ask_to_recalc(self):
        print('\n'*2, \
        "\nTo continue with the current calcaulation, enter 'c'\
        \nTo perform a different calcaulation, enter 'd'\
        \nTo exit, enter 'e'")

        acc_range = ['e', 'c', 'd']
        prompt = ":>\t"
        while True:
            inp = input(prompt)

            if inp.lower() not in acc_range:
                print("\nError!")
                continue

            return inp.lower()

    def clear_rec(self):

        self.nums['numbers'].clear()
        self.opers['arith_opers'].clear()
