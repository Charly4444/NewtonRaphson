#This is a python program on Newton-Raphson method
import numpy as np
"""This program computes the real solution(if exists) for a
function in single-variable that is linearly_differentiable
or expressible in polynomial form.
TO USE THIS:
just change the expression for f(x) and f_prime(x) below
to represent desired functions"""

#Input values of initial_guess, minimum_error and max_iterations
# x_old = float(input("initial_guess: "))
# error_min = float(input("minimum error: "))
# iter_max = int(input("max_iteration: "))

#===========================================================================================



def NR_mtd(x_old: float, error_min: float, iter_max: int =100):
    # define initial values for the variables
    iter = 0
    count1 = 0
    count2 = 0
    divchek = 0
    er = 1
    x = x_old

    while (iter <= iter_max) and (er > error_min) and (count1 <= 5) and (count2 <= 5) and (divchek <= 4):

        # EVALUATING f(x) IN A TRY-CATCH
        try:
            fx = 2*(x**2)+2*x-5             #INPUT YOUR f(x) HERE
            # fx = round(((x ** 3) - (16 * np.real(((x + 1) ** (1 / 3)))) - 8), 3)
        except Exception as e1:
            print("error", e1.__class__, f"has occurred in evaluating f(x) at {x}")
            x += 1
            count1 += 1
            fx = "null"

        # EVALUATING f'(X) IN A TRY-CATCH
        try:
            f_primex = 4*x+2                #INPUT YOUR f_Prime(x) HERE
            # f_primex = round(((2 * x) - (16 / (3 * np.real(((x + 1) ** (2 / 3)))))), 3)
        except Exception as e2:
            print("error", e2.__class__, f"has occurred in evaluating f_prime(x) at {x}")
            x += 1
            count2 += 1
            f_primex = -1  # return to a default value

        if (f_primex == 0):
            x += 1
            count2 += 1
        # EVALUATING THE NEW VALUE FOR X ACCORDING TO THE NR-Formula
        else:
            x += round((-1 * fx / f_primex), 4)
            er = abs(round((x - x_old), 4))
            print(f"{iter}, {x_old}, {fx}, {f_primex}, {x}")

            # CHECK IF SOLUTION IS DIVERGING
            if abs(fx) >= 100000:
                divchek += 1
            x_old = x
            iter += 1

    # OUTPUT SELECTION
    if (er <= error_min):
        print(f"\n the solution is {x} after {iter} iterations")
        return x
    elif (iter < iter_max) and (count1 > 5):
        print("\n error occurred multiple times in evaluating f(x)")
    elif (iter < iter_max) and (count2 > 5):
        print("\n error occurred multiple times in evaluating f_prime(x)")
    elif (divchek > 4):
        print("\n this solution is diverging")
    else:
        print(f"couldn't find a Real solution for f(x) in {iter_max} iterations")





#CALLING THE FUNCTION
if __name__ == '__main__':
    NR_mtd(1, 0.01)
