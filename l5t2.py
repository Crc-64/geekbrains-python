inFile = open("l5t2-in.txt", "r")

lineCount:int = 0
wordCount:int = 0
wordsInLine:int = 0
for strLine in inFile:
	lineCount += 1
	wordsInLine = len(strLine.split())
	wordCount += wordsInLine
	print(f"#{lineCount - 1}, {wordsInLine}: {strLine}", end = "")

print(f"\n\nTotal lines: {lineCount}\nTotal words: {wordCount}")
