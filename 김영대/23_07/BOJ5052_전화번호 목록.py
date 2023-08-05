import sys
def solution():
    read = sys.stdin.readline
    testCase = int(read())
    for _ in range(testCase):
        n = int(read())
        book = []
        cFlag = 0
        for i in range(n):
            tel = read().rstrip()
            book.append(tel)
<<<<<<< HEAD

=======
    
>>>>>>> origin/main
        bookSet = set(book)
        for target in bookSet:
            while(len(target) > 1):
                target = target[:-1]
                if target in bookSet:
                    cFlag = 1
                    break
            if cFlag:
                print("NO")
                break
<<<<<<< HEAD

=======
    
>>>>>>> origin/main
        if not cFlag:
            print("YES")
solution()