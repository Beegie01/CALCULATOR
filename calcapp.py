from simple_calc_OOP import *
from datetime import datetime

print('\n'*5, '\t\t\tOSAGIE CALC 2021')
print('\n'*2, '{t}\t\t\t{d}'.format(d=datetime.date(datetime.today()), t=datetime.time(datetime.today())))

# calculator is on
print("THIS IS OSAGIE CALC 2021")

# calculator screen is set
calc = Calc()

calc.nums['numbers'].append(calc.prompt_num())

calc.opers['arith_opers'].append(calc.prompt_oper())

calc.calculate()
