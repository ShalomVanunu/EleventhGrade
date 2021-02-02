
"""
this is simple program thats run 2 functions
"""

import time
import threading # use threading mode

def function_one(symbol1,time1,sleep1):
    for i in range(time1):
        print('\033[36m'+10*symbol1)
        time.sleep(sleep1)


def function_two(symbol2,time2,sleep2):
    for i in range(time2):
        print('\033[31m'+10*symbol2)
        time.sleep(sleep2)


def main():
    th1 = threading.Thread(target=function_one, args=('*',50,0.1))
    th2 = threading.Thread(target=function_two, args=('#',50,0.2))
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    #function_one('*',50,0.1) # 5 sec
    #function_two('#', 50, 0.2) # 10 sec

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print('\033[38m'+f'Total Time in {round(stop-start,2)}')