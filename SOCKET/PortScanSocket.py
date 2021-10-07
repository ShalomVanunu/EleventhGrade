import socket
import threading


def scan(i):
    for j in range(0, 1024):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = client.connect_ex((f"172.20.157.{i}", j))
        if result == 0:
            print(f"172.20.157.{i}", j)


def main():
    thr = []
    for i in range(1, 255):
        thr.append(threading.Thread(target=scan, args=(i,)))
        thr[-1].start()
    for t in thr:
        t.join()


main()
