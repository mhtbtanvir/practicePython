def add(n1, n2):
    return n1+n2


def sub(n1, n2):
    return n1-n2


def divide(n1, n2):
    return n1/n2


def multiply(n1, n2):
    return n1*n2


def modulus(n1, n2):
    return n1 % n2


calculations = {
    "+": add,
    "-": sub,
    "/": divide,
    "*": multiply,
    "%": modulus
}


def calculator():
    num1 = float(input("pick first number: "))
    for method in calculations:
        print(method)
    should_continue = True
    while should_continue:
        calc = input("pick calculation method :")

        num2 = float(input("pick next number: "))

        call_method = calculations[calc]
        result1 = call_method(num1, num2)

        print(f"result  {num1}{calc}{num2}={result1}")

        if input(f"type 'y' continue this calculation further with {result1} or 'n' to restart:").lower() == "y":
            num1 = result1
        else:
            should_continue = False
            calculator()


calculator()
