def main():
    x = 2.0
    y = 4.0

    operator = input("Welchen Operator möchtest du nutzen: ")

    solution = 0

    if operator == "+":
        solution = add(x,y)
    elif operator == "-":
        solution = sub(x,y)

    print(f"{x} {operator} {y} = {solution}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


if __name__ == '__main__':
    main()
