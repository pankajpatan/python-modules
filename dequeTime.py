from collections import deque
import time
start_time = time.time()
d = deque([1,5,6,8,9,10,15])

d.popleft()

print("time taken", start_time-time.time())


start_time2 = time.time()
d.append(4)
print('deque after appended',d)
print('time taken to insert',start_time2-time.time())