import matplotlib.pyplot as plt


def ddl(x1, y1, x2, y2, color):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    p = 2*dy - dx

    x = x1
    y = y1

    for i in range(x, x2):
        plt.plot(round(x), round(y), color)
        x = x + 1
        if p < 0:
            p = p + 2 * dy
        else:
            p = p + (2*dy) - (2*dx)
            y = y + 1

        print("VALOR DE X:", x)
        print("VALOR DE Y:", y)
    plt.title("Algoritmo Bresenhams")
    plt.grid()
    plt.show()

def main():
    x1 = int(input("INGRESA EL VALOR DE X1: "))
    y1 = int(input("INGRESA EL VALOR DE Y1: "))
    x2 = int(input("INGRESA EL VALOR DE X2: "))
    y2 = int(input("INGRESA EL VALOR DE Y2: "))
    color = "b."

    ddl(x1, y1, x2, y2, color)


if __name__ == "__main__":
    main()