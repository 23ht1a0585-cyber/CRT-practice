# import threading
# import time
# def task():
#     time.sleep(5)
#     print("Thread Finished")
# t = threading.Thread(target=task)
# t.start()
# t.join()
# print("Main thread ends here")





'''multiple threads with join
'''
# import threading
# import time

# def task(name):
#     print(name, "started")
#     time.sleep(2)
#     print(name, "finished")

# t1 = threading.Thread(target=task, args=("A",))
# t2 = threading.Thread(target=task, args=("B",))
# t3 = threading.Thread(target=task, args=("C",))

# t1.start()
# t2.start()
# t3.start()

# t1.join()
# t2.join()
# t3.join()

# print("All threads completed")



'''example on naming threads
'''
# import threading
# import time

# def task():
#     print(threading.current_thread().name, "started")
#     time.sleep(2)
#     print(threading.current_thread().name, "finished")

# t1 = threading.Thread(target=task, name="UPLOAD")
# t2 = threading.Thread(target=task, name="DOWNLOAD")
# t3 = threading.Thread(target=task, name="BALASREE")

# t1.start()
# t2.start()
# t3.start()


# '''REAL TIME DOWNLOADING:'''
# import threading
# import time

# def download_file(file):
#     print("downloading", file)
#     time.sleep(2)
#     print(file, "finished")

# files = [
#     "movies.mp4",
#     "song.mp3",
#     "image.jpg"
# ]

# threads = []

# for file in files:
#     t = threading.Thread(target=download_file, args=(file,))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print("All downloads finished")
# import threading
# import time 

# def student(name):
#     print(name, "started exam")
#     time.sleep(3)
#     print(name, "submitted paper")

# t1 = threading.Thread(target=student, args=("rahul",),name="stdent-1")
# t2 = threading.Thread(target=student, args=("sravani",),name="stdent-1")


# t1.start()
# t2.start()


# t1.join()
# t2.join()


# print("All students completed exam")

'''
race condition
synchronoizaation
lock
Rlock


#why we need schronization?
# '''
# balance =1000
# thread1 -- withdraw 500
# thread2 -- withdraw 700

# both are accessing the same variables
# without proper control



# inncorrect balance
# wrong transactions
#data coorupt
# to avoid the above we will use?
# SYNCHRONIZATION:
# this is a process of controlling access to shared 
# resources so tht only one thread modifies at a time


# '''lock
# hared
# resources:any variables,sile,database,object
# EXAMPLE:
#  count=0
#  if multiple thrreads modifies count simultaneously'''

# count= 0
# count+=1
# print(count)
# import threading

# counter = 0

# def increment():
#     global counter
#     for _ in range(221):
#         counter += 1

# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("Final counter:", counter)

# import threading

# count = 0
# lock = threading.Lock()

# def increment():
#     global count
#     with lock:
#         count += 1

# threads = []

# for i in range(2900):
#     t = threading.Thread(target=increment)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# # print(count)       
# import threading

# count = 0
# lock = threading.Lock()

# def increment():
#     global count
#     with lock:
#         temp = count
#         temp += 1
#         count = temp
#     print(count)

# threads = []

# for i in range(10):
#     t = threading.Thread(target=increment)
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()

# print("Final:", count)


# '''lock:
# whats is lock?
# synchornization mechanism that allows only one thread to execute a critical nsection at qa time.

# Thread a acquries lock
# other threads will wait
# threads a release lock++++
# next thread gets lock '''

# import threading
# lock = threading.Lock()
# #to apply lock
# lock.release()


# import threading
# import time

# lock = threading.Lock()

# def task(name):
#     print(name, "is waiting for the lock")

#     lock.acquire()  # Acquire the lock
#     try:
#         print(name, "acquired the lock")
#         time.sleep(2)
#         print(name, "finished work")
#     finally:
#         lock.release()  # Release the lock
#         print(name, "released the lock")

# t1 = threading.Thread(target=task, args=("Thread-1",))
# t2 = threading.Thread(target=task, args=("Thread-2",))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("All threads completed")


import threading
import time

def thread1():
    print("Thread1: Started")
    print("Thread1: Waiting for Thread2 to finish...")
    t2.join()   # waits for thread2
    print("Thread1: Finished")

def thread2():
    print("Thread2: Started")
    print("Thread2: Waiting for Thread1 to finish...")
    t1.join()   # waits for thread1
    print("Thread2: Finished")

t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

t1.start()
t2.start()



