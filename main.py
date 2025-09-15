def main():
    x = float(input("Was ist die erste Zahl?\n"))
    y = float(input("Was ist die zweite Zahl?\n"))

    print(f"{x} + {y} = {add(x, y)}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


if __name__ == '__main__':
    main()
