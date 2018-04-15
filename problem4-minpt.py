def minPt(numbers):
    length = len(numbers)
    if length > 2:
        mid = length // 2
        left = numbers[:mid]
        left = minPt(left)
        right = numbers[mid:]
        right = minPt(right)
        left.extend(right)
        if left[0] < left[1]:
            left.pop(1)
        else:
            left.pop(0)
        return left
    else:
        if length == 2:
            if numbers[0] < numbers[1]:
                numbers.pop(1)
            else:
                numbers.pop(0)
        return numbers

while True:
	try:
		rawInput = input("Enter a list of numbers, or X to exit:").strip()
		if rawInput == "X":
			break
		else:
			numbers = list(map(int, rawInput.split(" ")))
			print(minPt(numbers))
	except:
		print("Please enter a valid list of space-separated integers!")
