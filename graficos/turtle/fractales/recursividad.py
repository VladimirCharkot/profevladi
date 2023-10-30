
def misterio(cantidad):
    print('Hola')
    if cantidad == 0:
        return
    misterio(cantidad - 1)
    

##def recursiva(param):
##    if condicion(param):
##        return
##    else:
##        recursiva(param*)

llamadas = 0

def fibonacci(n):
    global llamadas
    llamadas += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


##fibo(3) = fibo(2) + fibo(1) = 1 + 1
##
##fibo(4) = fibo(3) + fibo(2) = fibo(2) + fibo(1) + 1 = 1 + 1 + 1
##
##fibo(5) = fibo(4)           + fibo(3)
##        = fibo(3) + fibo(2) + fibo(2) + fibo(1)
##        = fibo(2) + fibo(1) + 1 + 1 + 1
##        = 1 + 1 + 1 + 1 + 1
##        = 5

llamadas_factorial = 0

def factorial(n):
    global llamadas_factorial
    llamadas_factorial += 1
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

##factorial(5) = 5 * factorial(4)
##             = 5 * 4 * factorial(3)
##             = 5 * 4 * 3 * factorial(2)
##             = 5 * 4 * 3 * 2 * factorial(1)
##             = 5 * 4 * 3 * 2 * 1




    
