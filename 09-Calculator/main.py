import art

def add(n1, n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}


def calculator():
    print(art.logo)
    num = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:
        for key in operations_dict:
            print(key)
        operation = input("pick an operation: ")
        next_num = float(input("What's the next number?: "))
        value= operations_dict[operation](num,next_num)
        print(f"{num} {operation} {next_num} = {value}")

        choice = input(f"Type 'y' to continue calculating with {value}, or type 'n' to start a new calculation: ").lower()
        if choice=="n":
            should_continue=False
            print("\n" * 30)
            calculator()

        elif choice=="y":
            num = value

calculator()
