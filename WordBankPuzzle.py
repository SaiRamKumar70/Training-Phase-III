wordbank = [
            ['n','b','c','d','e'],
            ['d','i','l','v','a'],
            ['u','j','e','n','r'],
            ['r','s','a','i','w'],
            ['w','m','a','r','m']]
word = input("Enter the Word to search : ")
#n=len(word)
def find(row, col, i, path):
    if i == len(word):
        print("Valid path coordinates : ")
        for r, c in path:
            print(f"({r}, {c})", end=" -> ")
        print("Destination")
        return True
    if row < 0 or row >= len(wordbank) or  col< 0 or col >= len(wordbank[0]):
        return False
    if [row, col] not in path:
        path.append([row, col])
        if wordbank[row][col] == word[i]:
            if find(row+1, col, i+1, path):
                return True
            if find(row-1, col, i+1, path):
                return True
            if find(row, col+1, i+1, path):
                return True
            if find(row, col-1, i+1, path):
                return True
        path.remove([row, col])
    return False
path = []
found = False
for i in range(len(wordbank)):
    for j in range(len(wordbank[i])):
        if find(i, j, 0, path):
            found = True
            break
    if found:
        break
else:
    print("Invalid path")
