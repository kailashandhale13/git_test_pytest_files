# import threading
# import time

# def print_numbers():
#     for i in range(1,6):
#         print('Thead 1',i)
#         time.sleep(1)


# def print_latters():
#     for i in 'abcde':
#         print('Thread 2',i)
#         time.sleep(1)

# #creating thead

# threading1= threading.Thread(target=print_numbers)
# threading2=threading.Thread(target=print_latters)

# threading1.start()
# threading2.start()

# threading1.join()
# threading2.join()
# print('Both threads have be finished executing ')









import threading
import time


def print_number():
    for i in range(1,6):
        time.sleep(1)
        print('Thread-- 1 ',i)

def print_latter():
    for i in 'ABCDE':
        time.sleep(1)
        print('Thread-- 2' ,i)


time_star= time.time()
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_latter)

t1.start()
t2.start()

t1.join()
t2.join()
time_end = time.time()
time_elapse = time_end - time_star
print(f'both thread completed in {time_elapse} sec.')
