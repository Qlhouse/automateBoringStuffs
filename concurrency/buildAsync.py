SEQUENTIAL = False
THREAD = False
ASYNC_V1 = False
ASYNC_V2 = False
ASYNC_V3 = False
ASYNC_V4 = False

Producer_Consumer_Problem = False
Async_Producer_Consumer_V1 = False
Async_Producer_Consumer_V2 = False
Async_Producer_Consumer_V3 = False
Async_Producer_Consumer_V4 = False


# Sequential execution
if SEQUENTIAL:
    import time
    
    def countDown(n):
        while n > 0:
            print('Down', n)
            time.sleep(1)
            n -= 1
    
    def countUp(stop):
        x = 0
        while x < stop:
            print('Up', x)
            time.sleep(1)
            x += 1

    countDown(5)
    countUp(5)


# Concurrent execution

# Classic solution: use threads
if THREAD:
    import threading
    import time
    
    def countDown(n):
        while n > 0:
            print('Down', n)
            time.sleep(1)
            n -= 1
    
    def countUp(stop):
        x = 0
        while x < stop:
            print('Up', x)
            time.sleep(1)
            x += 1

    threading.Thread(target=countDown, args=(5,)).start()
    threading.Thread(target=countUp, args=(5,)).start()

# Problem: How to achieve concurrency without threads?
# Issue: Figure out how to switch between tasks.

if ASYNC_V1:
    import time
    from collections import deque   
    
    class Scheduler:
        def __init__(self):
            self.ready = deque()   # Function ready to execute
            self.sleeping = []     # Sleeping functions
    
        def call_soon(self, func):
            self.ready.append(func)
    
        def run(self):
            while self.ready:
                func = self.ready.popleft()
                func()
    
    sched = Scheduler()    # Behind scenes scheduler object
    
    def countDown(n):
        if n > 0:
            print('Down', n)
            time.sleep(4)    # Blocking call (nothing else can happen)
            sched.call_soon(lambda : countDown(n-1))
    
    '''
    def countUp(stop, x=0):
        if x < stop:
            print('Up', x)
            time.sleep(1)
            sched.call_soon(lambda : countUp(stop, x + 1))
    '''
    
    def countUp(stop, x=0):
        def _run(x):
            if x < stop:
                print('Up', x)
                time.sleep(1)
                sched.call_soon(lambda : _run(x+1))
        _run(0)
    
    sched.call_soon(lambda : countDown(5))
    sched.call_soon(lambda : countUp(5))
    sched.run()


if ASYNC_V2:
    import time
    from collections import deque
    class Scheduler:
        def __init__(self):
            self.ready = deque()   # Function ready to execute
            self.sleeping = []     # Sleeping functions
    
        def call_soon(self, func):
            self.ready.append(func)
    
        def call_later(self, delay, func):
            deadline = time.time() + delay    # Expiration time
            # Prioprity queue
            self.sleeping.append((deadline, func))
            self.sleeping.sort()   # Sort by closest deadline
    
        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    # Find the nearest deadline
                    deadline, func = self.sleeping.pop(0)
                    delta = deadline - time.time()
                    if delta > 0:
                        time.sleep(delta)
                    self.ready.append(func)
    
                while self.ready:
                    func = self.ready.popleft()
                    func()
    
    sched = Scheduler()    # Behind scenes scheduler object
    
    def countDown(n):
        if n > 0:
            print('Down', n)
            time.sleep(4)    # Blocking call (nothing else can happen)
            sched.call_later(4, lambda : countDown(n-1))
    
    def countUp(stop, x=0):
        def _run(x):
            if x < stop:
                print('Up', x)
                # time.sleep(1)
                sched.call_later(1, lambda : _run(x+1))
        _run(0)
    
    sched.call_soon(lambda : countDown(5))
    sched.call_soon(lambda : countUp(20))
    sched.run()

if ASYNC_V3:
    import time
    from collections import deque   
    import heapq
    
    class Scheduler:
        def __init__(self):
            self.ready = deque()   # Function ready to execute
            self.sleeping = []     # Sleeping functions
    
        def call_soon(self, func):
            self.ready.append(func)
    
        def call_later(self, delay, func):
            deadline = time.time() + delay    # Expiration time
            # Prioprity queue
            heapq.heappush(self.sleeping, (deadline, func))
    
        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    # Find the nearest deadline
                    deadline, func = heapq.heappop(self.sleeping)
                    delta = deadline - time.time()
                    if delta > 0:
                        time.sleep(delta)
                    self.ready.append(func)
    
                while self.ready:
                    func = self.ready.popleft()
                    func()
    
    sched = Scheduler()    # Behind scenes scheduler object
    
    def countDown(n):
        if n > 0:
            print('Down', n)
            time.sleep(4)    # Blocking call (nothing else can happen)
            sched.call_later(4, lambda : countDown(n-1))
    
    def countUp(stop, x=0):
        def _run(x):
            if x < stop:
                print('Up', x)
                # time.sleep(1)
                sched.call_later(1, lambda : _run(x+1))
        _run(0)
    
    sched.call_soon(lambda : countDown(5))
    sched.call_soon(lambda : countUp(20))
    sched.run()


if ASYNC_V4:
    import time
    from collections import deque   
    import heapq
    
    class Scheduler:
        def __init__(self):
            self.ready = deque()   # Function ready to execute
            self.sleeping = []     # Sleeping functions
            self.sequence = 0
    
        def call_soon(self, func):
            self.ready.append(func)
    
        def call_later(self, delay, func):
            self.sequence += 1
            deadline = time.time() + delay    # Expiration time
            # Prioprity queue
            heapq.heappush(self.sleeping, (deadline, self.sequence, func))
    
        def run(self):
            while self.ready or self.sleeping:
                if not self.ready:
                    # Find the nearest deadline
                    deadline, _, func = heapq.heappop(self.sleeping)
                    delta = deadline - time.time()
                    if delta > 0:
                        time.sleep(delta)
                    self.ready.append(func)
    
                while self.ready:
                    func = self.ready.popleft()
                    func()
    
    sched = Scheduler()    # Behind scenes scheduler object
    
    def countDown(n):
        if n > 0:
            print('Down', n)
            time.sleep(4)    # Blocking call (nothing else can happen)
            sched.call_later(4, lambda : countDown(n-1))
    
    def countUp(stop, x=0):
        def _run(x):
            if x < stop:
                print('Up', x)
                # time.sleep(1)
                sched.call_later(1, lambda : _run(x+1))
        _run(0)
    
    sched.call_soon(lambda : countDown(5))
    sched.call_soon(lambda : countUp(20))
    sched.run()


if Producer_Consumer_Problem:
    # Producer-Consumer problem
    import queue
    import threading
    import time
    
    def producer(q, count):
        for n in range(count):
            print('Producing', n)
            q.put(n)
            time.sleep(1)
        
        print('Producer done')
        q.put(None)   # "Sentinel" to shutdown
    
    def consumer(q):
        while True:
            item = q.get()
            if item is None:
                break
            print("Consuming", item)
    
        print("Consumer done!")
    
    q = queue.Queue()  # Thread-safe queue
    threading.Thread(target=producer, args=(q, 10)).start()
    threading.Thread(target=consumer, args=(q,)).start()


# Producer-Consumer problem 
# Challenge: How to implement the same funtionality, but no threads.