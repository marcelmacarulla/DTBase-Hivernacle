import threading
import time
import datetime

# Define a function that will be executed by each thread
def thread_function1(name, delay):
    print("Thread {} started".format(name))
    time.sleep(delay)  # Simulate some work or delay
    print("Thread {} finished".format(name))

# Create threads
threads = []
thread1 = threading.Thread(target=thread_function1, args=(1, 1+1))  # Each thread will have a unique name and delay
threads.append(thread1)
thread1.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads have finished execution")

print(datetime.datetime.utcnow())