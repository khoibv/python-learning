def file_sample():
    """This is a sample about working with File I/O in Python"""
    fo = open("sample.txt", 'w+')
    fo.write("This is sample text\r\n")
    fo.write("This is second line")
    fo.close()

    fo = open('sample.txt', 'r')
    data = fo.readline(100)
    print('This is content of file: %s' % data)
    fo.readline(3)
    print('This is second data: %s' % fo.readline(100))


file_sample()
