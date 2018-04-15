def findAnchor(numbers):
    anchors = []
    for index, no in enumerate(numbers):
        if index == no:
            anchors.append(no)
    return anchors

while True:
	try:
		rawInput = input("Enter a list of numbers, or X to exit:").strip()
		if rawInput == "X":
			break
		else:
			numbers = list(map(int, rawInput.split(" ")))
			print(findAnchor(numbers))
	except:
		print("Please enter a valid list of space-separated integers!")
