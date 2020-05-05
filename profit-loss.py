def main():
    x = int(input("Enter purchase value: "))
    y = int(input("Enter sell value: "))
    profit = (y*0.92-x)
    if profit < 0:
        print("Loss with value " + str(abs(profit)))
    else:
        print("Profit with value " + str(profit))
main()