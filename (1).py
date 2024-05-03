limit='A'
for i in range(1,6):
    for j in range(ord('A'),ord(limit)+1):
        print(chr(j),end='')
    limit=(chr)((ord(limit))+1)
    print()
