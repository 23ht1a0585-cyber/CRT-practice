# #multi threading
# # program is a set of instructions
# # we can stored on a disk
# '''

# print("hello")

# storing on a disk???
# python day288.py
# hello

# what is proces?
# when a program starts executing it becomes a process running?
# python day288.py
# hello

# os -- operating System
# chrome :
# vs code:
# spotify:
# each one is a seperate ProcessLookupError
# charateristics :

# 1.independent Process
# 2.seperate memory:
# chrome:1.8GB,vs-code -500MB
# 3.Heavy weight:
# Memory allocations
# cpu scheduling

# what is thread?
# A thread is smallest unit of execution inside a ProcessLookupError

# ex:
# Resturant == process
# workers inside resturant = threads

# worker1: taking the orders
# worker2: cooking
# worker3: billing
# worker4: cleaning


# visually:
# processs:
# like chrome will have
# +thread1 :
# +thread2:
# +thread3:


# process                 thread
# 1.independent           1.part of processs
# 2.heavy weight          2.light weight
# 3.seperate memory       3.shared memory
# 4.creation process slow 4.fast
# 5.expensive             5.cheap
# 6>difficult             6.communication easy



# why threads are faster?
# threads will share the memory 
# process needs separate memory allocation

# concurrency?

# teacher checking the noteboks 
# student A 
# student B
# student c
# A
# B
# C
# A
# B
# C
# one at a time
# rapidly switching
# appears simultaneously

# parallesim:
# cashier1: -->customer 1
# cashier2: -->customer 2
# cashier3: -->customer 3

# truly simulatenously

# cpu1 --> task a
# cpu2 --> task b
# cpu3 --> task c

# A
# B
# A
# B
# A
# B

# parallesim:
# cpu1 --AAA  
# cpu2 --BBB


# one chef cooking:
# soup
# noodles
# fried rice

# parallesim:
# chef1: sopu
# chef2: noodles
# chef3: fried rice
#  python threads use concurrency 

#  due to GIL----GLOBAL INTERPRETER LOCK

# '''
# #creation of threads
# # import threading

# # # function created (do's nothing)
# # def display():
# #     print("Hello")
# # t = threading.Thread(target=display)
# # t.start()


# #multiple threads
# # import threading

# # def task(task):
# #     print("thread running")

# # t1 = threading.Thread(target=task) 
# # t2 = threading.Thread(target=task) 
# # t3 = threading.Thread(target=task)

# # t1.start()
# # t2.start()
# # t3.start()



# # import threading

# # def task(task):
# #     print("thread running")

# # t1 = threading.Thread(target=task) 
# # t2 = threading.Thread(target=task) 
# # t3 = threading.Thread(target=task)

# # t1.start()
# # t2.start()
# # t3.start()


# ''''threads with loops
# '''

# # import threading

# # def task():
# #     for i in range(4):
# #         print("Thread running:", i)

# # t = threading.Thread(target=task)
# # t.start()


# # '''two tasks with diff tasks'''
# # import threading

# # def print_even():
# #     for i in range(0, 10, 2):
# #         print("Even:", i)

# # def print_odd():
# #     for i in range(0,10,2):
# #         print("Odd:", i)

# # t1 = threading.Thread(target=print_even)
# # t2 = threading.Thread(target=print_odd)

# # t1.start()
# # t2.start()

# # '''
# # os schedular decides:
# # which thread to runs first?
# # '''
# # print(threading.current_thread())


# #Naming of threads:
# import threading
# def task():
#     print(threading.current_thread().name)
# t = threading.Thread(target=task,name="student_thread")
# t.start()

# paasing arguments:
# def square(n):
#     print(n*n)

# t = threading.Thread(target=square,args=(5,))    
# t.start()



# import time
# print("start")
# time.sleep(3)
# print("end")


# import threading
# import time
# def task():
#     for i in range(4):
#         print(i)
#         time.sleep(1)
# t = threading.Thread(target=task)
# t.start()


# retry mechanism

# while true:
#     try:
#         connect()
#     except:
#         time.sleep(5)


# Rlock: Recursive lock
# A thread can aquire the same lock multiple times

# why RLOCK:

# Normal Lock
# acquire lock
# release lock

# if same thread acquires again deadlock



import threading

lock = threading.RLock()

def inner():
    with lock:
        print("Inner function")

def outer():
    with lock:
        print("Outer function")
        inner()   

t = threading.Thread(target=outer)
t.start()
t.join()

