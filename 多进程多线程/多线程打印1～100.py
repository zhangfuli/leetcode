import threading
import time


def worker():
    global count
    while True:
        lock.acquire()  # 加锁
        count += 1
        print(threading.current_thread(), count)
        lock.release()  # 操作完成后释放锁
        if count >= 99:
            break
        time.sleep(1)
    print(1)


def main():
    threads = []
    for i in range(2):  # 控制线程的数量
        t = threading.Thread(target=worker, args=())
        threads.append(t)
    for i in threads:
        i.start()
    for i in threads:
        i.join()  # 将线程加入到主线程中


if __name__ == '__main__':
    lock = threading.Lock()
    count = 0
    main()
