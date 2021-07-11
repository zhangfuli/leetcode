import threading


def print_num():
    while True:
        print(1)


def print_str():
    while True:
        print(2)


if __name__ == '__main__':
    t1 = threading.Thread(target=print_num, args=())  # target是指定函数(不要带括号)，args是函数的参数(如果没有参数可以省略不写)
    t2 = threading.Thread(target=print_str, args=())  # 上面是print_num的线程，下面是print_str的线程
    t1.start()  # 运行t1线程
    t2.start()  # 运行t2线程
