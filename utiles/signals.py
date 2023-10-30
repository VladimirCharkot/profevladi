import signal
import sys
import time

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    print(sig)
    print(frame)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
while True:
    time.sleep(1)
    print('.')
