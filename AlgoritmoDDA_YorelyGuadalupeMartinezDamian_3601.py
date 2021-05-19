import matplotlib.pyplot as plt


def ddl(x1, y1, x2, y2, color2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    steps = 0

    if (dx) > (dy):
        steps = (dx)
    else:
        steps = (dy)

    xInc = float(dx / steps)
    yInc = float(dy / steps)

    xInc = round(xInc, 1)
    yInc = round(yInc, 1)

    for i in range(0, int(steps + 1)):
        plt.plot(round(x1), round(y1), color2)
        x1 += xInc
        y1 += yInc

        print("VALOR DE X:",x1)
        print("VALOR DE Y:",y1)

    plt.title("Algoritmo DDA.")
    plt.grid()
    plt.show()

def main():
    x1 = int(input("INGRESA EL VALOR DE X1: "))
    y1 = int(input("INGRESA EL VALOR DE Y1: "))
    x2 = int(input("INGRESA EL VALOR DE X2: "))
    y2 = int(input("INGRESA EL VALOR DE Y2: "))
    color2 = "r."

    ddl(x1, y1, x2, y2, color2)

if __name__ == "__main__":
    main()
