
import time
import threading # use threading mode

def function(symbol,time1,sleep1):
    for i in range(time1):
        print('\033[36m'+10*symbol)
        time.sleep(sleep1)

def main():
    symbols = ["!","@","#","$","%"]
    threads = []
    for i in symbols:
        th = threading.Thread(target=function, args=(i,20,0.1))
        th.start()
        threads.append(th)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    stop = time.perf_counter()
    print('\033[38m'+f'Total Time in {round(stop-start,2)}')