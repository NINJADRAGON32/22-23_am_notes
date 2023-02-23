def wordInALine(line, word):
    if word in line:
        print(line.index(word))
        return True

rowImIn="asdfbaconghjkl"
wordImSearchingFor = 'bacon'

wordInALine(rowImIn, wordImSearchingFor)

# horizontl searching
puzzleList=[[]]
def printFile(fileName):
    global puzzleList,wordImSearchingFor,puzzle
    file=open