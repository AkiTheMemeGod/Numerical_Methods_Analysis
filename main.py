import math
import sympy as sp
x = sp.Symbol("x")
def runge_kutta():
    x0 = float(input("Enter the value of x_n : "))
    y0 = float(input("Enter the value of y_n : "))
    h = float(input("Enter the height : "))

    function_str = input("Enter the function f(x, y) as a Python expression, e.g., x**2 + y**2: ")
    f = lambda x, y: eval(function_str)

    k1 = h * f(x0, y0)
    print("k1 = ", round(k1, 4))
    k2 = h * f(x0+h/2, y0+k1/2)
    print("k2 = ", round(k2, 4))
    k3 = h * f(x0 + h / 2, y0 + k2 / 2)
    print("k3 = ", round(k3, 4))
    k4 = h * f(x0 + h, y0 + k3)
    print("k4 = ", round(k4, 4))
    del_y = (k1 + (2*k2) + (2*k3) + k4)
    del_y = del_y / 6
    print("\ny1 = ", round(y0 + del_y, 4))



# def taylor_series():

f = x ** 3
ans = str(f.diff(x))
ans = ans.replace("**", "^").replace("*", "")
print(ans)

#runge_kutta()
