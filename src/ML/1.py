from Calc import Calc

def main():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))

    c = Calc(n1, n2)

    print("Sum =", c.sum())
    print("Sub =", c.sub())
    print("Mul =", c.mul())

    if n2 == 0:
        print("Cannot divide by zero")
    else:
        print("Div =", c.div())

main()