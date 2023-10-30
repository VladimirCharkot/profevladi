import time, threading, queue


def collect(que):
    msg = input()
    que.put(msg)

que = queue.Queue()
thread = threading.Thread(target=collect, args=[que])
thread.start()

while thread.is_alive():
    time.sleep(5)
    print("...")

msg = que.get()
print('You typed:', msg)
