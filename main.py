def main():
    x = 2.0
    y = 4.0

    print(f"{x} + {y} = {add(x, y)}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

if __name__ == '__main__':
    main()
