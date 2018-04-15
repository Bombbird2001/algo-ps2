#O(n)
def latinSquare(n):
    numbers = []
    for i in range(n):
        numbers.append(str(i + 1))
    for i in range(n):
        print(' '.join(numbers))
        popped = numbers.pop(0)
        numbers.append(popped)

while True:
    try:
        n = input("Enter a number for the latin square, or X to exit:")
        if n == "X":
            break
        else:
            latinSquare(int(n))
    except:
        print("Please input a valid integer!")
