# simple calculator Using OOP

class Calc:

    def __init__(self):
        self.nums = {'numbers': []}
        self.opers = {'arith_opers': []}


    def prompt_num(self):

        prompt = "\nPlease enter a number:\t"

        while True:
            inp = input(prompt)

            try:
                num = float(inp)
            except:
                print(f"Error: {inp} is invalid!")
                continue
            return str(num) + ' '

    def prompt_oper(self):
        print("\nPlease enter next operation below")

        prompt = "To add: '+',\nTo subtract: '-',\nTo multiply: '*',\nTo divide: '/'\n"

        acc_range = ['-', '+', '*', '/']

        while True:
            inp = input(prompt)

            if inp not in acc_range:
                print(f"Error: {inp} is invalid!")
                continue
            return inp + ' '

    def check_for_nums(self):
        if len(self.nums['numbers']) < 2:
            return 'auto'
        else:
            return 'ask'

    def calculate(self):
        while True:
            step = self.check_for_nums()

            if step == 'auto':
                self.nums['numbers'].append(self.prompt_num())
                continue
            elif step == 'ask':
                return self.replay()

    def asking(self):
        print("To continue, press enter\nTo see result, enter '='")
        acc_range = ['', '=']
        while True:
            inp = input()

            if inp not in acc_range:
                print(f"{inp} is invalid!")
                continue
            return inp

    def replay(self):
        while True:
            ans = self.asking()

            if ans == '':
                self.opers['arith_opers'].append(self.prompt_oper())
                self.nums['numbers'].append(self.prompt_num())
                continue
            else:
                return self.finalize()

    def finalize(self):

        expr = ''

        for (ind, num) in enumerate(self.nums['numbers']):
            expr += num
            if len(self.opers['arith_opers']) == ind:
                continue
            expr += self.opers['arith_opers'][ind]
            continue

        print(f"***********************************\
        \n{expr} = \
        \n{eval(expr)}\
        \n***********************************")
