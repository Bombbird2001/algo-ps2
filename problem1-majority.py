import math
def find_majority(noList):
    noList.sort()
    prevMaxCount = 0
    maxCount = 0
    max = noList[0]
    count = 0
    prevNo = max
    for index, no in enumerate(noList):
        if no == prevNo:
            count += 1
            if index == len(noList) - 1:
                prevMaxCount = maxCount
                maxCount = count
                max = no
        else:
            if count > maxCount:
                prevMaxCount = maxCount
                maxCount = count
                max = prevNo
            prevNo = no
            count = 1
    if maxCount > prevMaxCount and maxCount >= math.ceil(len(noList) / 2.0):
        print("Majority is", max, "with", maxCount, "occurence(s).")
    else:
        print("There is no majority in this list.")

while True:
		try:
			rawInput = input("Enter a list of numbers, or X to exit:").strip()
			if rawInput == "X":
				break
			else:
				numbers = list(map(int, rawInput.split(" ")))
				find_majority(numbers)
		except:
			print("Please enter a valid list of space-separated integers!")
