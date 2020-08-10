
import telnetlib
import threading

def get_port(ip, port):

    server = telnetlib.Telnet()
    try:
        server.open(ip, port)
        #print('{0} 的 {1} 端口是打开的 '.format(ip, port))
        with open("test.txt", "a", encoding='utf-8') as out_file:
            out_file.write('{0} 的 {1} 端口是打开的 \n'.format(ip, port))

    except Exception as err:
        pass
        # print('{0} 的 {1} 端口是没有打开的'.format(ip, port))

    finally:
        server.close()


if __name__ == '__main__':
    ipadress = input("输入目标ip:")
    host = ipadress
    print('端口扫描开始')
    everything = []

    for port in range(1, 65535):
        t = threading.Thread(target=get_port, args=(host, port))
        t.start()
        everything.append(t)

    for t in everything:
        t.join()
print('扫描完成，请查看test.txt文件')
