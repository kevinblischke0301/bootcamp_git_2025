def main():
    x = 2.0
    y = 4.0

    print(f"{x} + {y} = {add(x, y)}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y

while True:
    main()
    _ = input("Programm Schluss. Drücke Enter!")

if __name__ == '__main__':
    main()
