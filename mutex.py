import threading, time, random
lock = threading.Lock()

def run():
    global lock
    print('Thread 1 sleeping')
    time.sleep(random.randint(1,10))
    print('I should finish first')
    lock.release()
def run1 ():
    global lock
    print('Thread 2 sleep')
    time.sleep(random.randint(1,10))
    lock.acquire()
    print('I should finish last')

lock.acquire()
m1 = threading.Thread(target=run)
m1.start()
m2 = threading.Thread(target=run1)
m2.start()

