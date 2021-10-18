def countwords():
    name=input("Enter your file name: ")
    countnum=0
    file=open(name, 'r')
    for line in file :
        words=line.split()
        countnum += len(words)
    print("Number of words = ", countnum)
countwords()