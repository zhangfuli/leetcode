from multiprocessing import Pool, cpu_count
import os
import time


def long_time_task(i):
    print('子进程: {} - 任务{}'.format(os.getpid(), i))
    time.sleep(2)
    print("结果: {}".format(8 ** 20))


if __name__=='__main__':
    print("CPU内核数:{}".format(cpu_count()))
    print('当前母进程: {}'.format(os.getpid()))
    start = time.time()
    p = Pool(4)  # 四个进程
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('等待所有子进程完成。')
    p.close()
    # 对Pool对象调用join()方法会等待所有子进程执行完毕
    # 调用join()之前必须先调用close()或terminate()方法，让其不再接受新的Process了
    p.join()
    end = time.time()
    print("总共用时{}秒".format((end - start)))