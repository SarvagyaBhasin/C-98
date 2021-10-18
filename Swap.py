def swapFile():
    file1 = input("File name: ")
    file2 = input("File name: ")

    a = open(file1, 'r')
    data1 = a.read()
    b = open(file2, 'r')
    data2 = b.read()

    a = open(file1, 'w')
    a.write(data2)
    b = open(file2, 'w')
    b.write(data1)

swapFile() 