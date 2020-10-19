def main():

    number = int(input("enter a number: "))
    # creating empty list
    collatz = []
    # adding the number to the list
    collatz.append(number)
    steps = 0
    largest = collatz[0]
    # calculating collatz conjecture
    while True:
        # storing the latest number in lastest var
        latest = collatz[-1]
        if latest == 1:
            break
        if latest % 2 == 0:
            collatz.append(int(latest/2))
        else:
            collatz.append(int((latest*3)  + 1))
        steps += 1
        if latest > largest:
            largest = latest
    print(collatz)
    print(f"\nsteps: {steps}")
    print(f"largest number: {largest}")



main()