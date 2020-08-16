
def bytes(bytes):
    if bytes < 1024:  #比特
        bytes = str(round(bytes, 2)) + ' B' #字节
    elif bytes >= 1024 and bytes < 1024 * 1024:
        bytes = str(round(bytes / 1024, 2)) + ' KB' #千字节
    elif bytes >= 1024 * 1024 and bytes < 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024, 2)) + ' MB' #兆字节
    elif bytes >= 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024 / 1024, 2)) + ' GB' #千兆字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024 / 1024 / 1024, 2)) + ' TB' #太字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024 / 1024 / 1024 / 1024, 2)) + ' PB' #拍字节
    elif bytes >= 1024 * 1024 * 1024 * 1024 * 1024 * 1024 and bytes < 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024:
        bytes = str(round(bytes / 1024 / 1024 / 1024 / 1024 / 1024 /1024, 2)) + ' EB' #艾字节
    return bytes
 
if __name__ == '__main__':
    print('0：' + bytes(0))
    print('1：' + bytes(1))
    print('2：' + bytes(10))
    print('3：' + bytes(100))
    print('4：' + bytes(1000))
    print('5：' + bytes(10000))
    print('6：' + bytes(100000))
    print('7：' + bytes(1000000))
    print('8：' + bytes(10000000))
    print('9：' + bytes(100000000))
    print('10：' + bytes(1000000000))
    print('11：' + bytes(10000000000))
    print('12：' + bytes(100000000000))
    print('13：' + bytes(1000000000000))
    print('14：' + bytes(10000000000000))
    print('15：' + bytes(100000000000000))
    print('16：' + bytes(1000000000000000))
    print('17：' + bytes(10000000000000000))
    print('18：' + bytes(100000000000000000))
    print('19：' + bytes(1000000000000000000))
    print('20：' + bytes(10000000000000000000))
    print('20：' + bytes(100000000000000000000))
    print('20：' + bytes(1000000000000000000000))


