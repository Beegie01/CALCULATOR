from simple_calc_OOP import *
from datetime import datetime

print('\n'*5, '\t\t\tOSAGIE CALC 2021')
print('\n'*2, '{t}\t\t\t{d}'.format(d=datetime.date(datetime.today()), t=datetime.time(datetime.today())))

# calculator is on
# calculator screen is set
calc = Calc()


CALCULATING = True

while CALCULATING:

    # for first three input (1st num, arithmetic oper, 2nd num)
    calc.compute()

    more_calc = True

    while more_calc:

        # continue adding input or check result
        ans = calc.ask_to_cont()

        # if continue adding input
        if ans == '':
            calc.cont_calc()
            recalc = False
            continue

        # if check result
        elif ans == '=':
            calc.show_answer()

        # continue with current calculation
        # start a new calculation
        # or exit the app
        reply = calc.ask_to_recalc()

        # current calculation
        if reply == 'c':
            calc.cont_calc()
            continue


        # different calculation
        elif reply == 'd':
            calc.clear_rec()
            more_calc = False
            break

        # exit calculator
        else:
            print("\nThank You for Using OsagieCalc2021")
            quit()
