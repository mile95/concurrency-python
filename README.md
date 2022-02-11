# concurrency-python

A collection of documentation, scripts, and POCs related to concurrency in Python.

Each script touches upon a specific problem and shows a corresponding suggested solution, for instance, shared resources or exceptions handling. 

In Python, you can achieve concurrency by using multiple threads or processes, and each way has its pros and cons, depending on the situation.

* TODO: Write a bit about the difference between threads and processes.
* TODO: Write a bit about asynchronous execution VS synchronous execution.

There exist a few different libraries and modules for handling concurrency in Python. I will stick to [concurrent.features](https://docs.python.org/3/library/concurrent.futures.html), for asynchronous execution since it is part of pythons standard library.

There will be scripts and explanations for multi-threading and multi-processing, and we will start with multi-threading.

## Running the scripts
```python
python3 <name-of-script>
```

For instance

```python
python3 multithreaded-basic.py
```

## Multithreaded - Basic

Script name: `multithreaded-basic.py`, see [this](multithreaded-basic.py).

This script tries to show how to run the same function `foo` asynchronously (multiple executions during the same time), using threads. The function `foo` takes the `id` of the thread (0-4), and forces that thread to sleep for a random amount of seconds.

We use a `ThreadPoolExecutor` which uses a pool of at most `max_workers` (in this case 5) threads to execute `foo` asynchronously. 

By using the `with` statement in Python, we make sure that the threads get cleaned up promptly when they finished executing `foo`

Example output from the script:

```
$ python3 multithreaded-basic.py

2022-02-10 09:00:30,258 - __main__ - INFO - Thread: 0 started foo. Will sleep for: 2s
2022-02-10 09:00:30,258 - __main__ - INFO - Thread: 1 started foo. Will sleep for: 2s
2022-02-10 09:00:30,259 - __main__ - INFO - Thread: 2 started foo. Will sleep for: 4s
2022-02-10 09:00:30,259 - __main__ - INFO - Thread: 3 started foo. Will sleep for: 4s
2022-02-10 09:00:30,259 - __main__ - INFO - Thread: 4 started foo. Will sleep for: 4s
2022-02-10 09:00:32,262 - __main__ - INFO - Thread: 0 finished foo
2022-02-10 09:00:32,263 - __main__ - INFO - Thread: 1 finished foo
2022-02-10 09:00:34,261 - __main__ - INFO - Thread: 2 finished foo
2022-02-10 09:00:34,261 - __main__ - INFO - Thread: 4 finished foo
2022-02-10 09:00:34,262 - __main__ - INFO - Thread: 3 finished foo

```

Here we see that all 5 threads are started at the same time, but since `foo` can take 0-4s to finish, the threads finishes in different order.

## Multithreaded - Shared Resources

Script name: `multithreaded-locks.py`, see [this](multithreaded-locks.py).

This script aims to show how to handle [race conditions](https://en.wikipedia.org/wiki/Race_condition) by protecting the shared resource. The problem occurs when multiple threads try to update the same resource, during the same time. In this example, we run two different scenarios. Scenario 1, the `race condition scenario`, runs the `foo_without_locks` asynchronously in 2 threads without protecting the shared resource `count`. Scenario 2, the `safe scenario`, runs the `foo_with_locks` in the same way but protects the shared resource. In both scenarios, one of the two threads decreases the `count` variable by 1, and the other thread increases the `count` variable by 1. Each tread does its operation `200000` times, and the value of `count` should be `0` when the scenario terminates.

Example output from the script:

```
$ python3 multithreaded-locks.py

2022-02-11 08:20:14,856 - __main__ - INFO - Running race condition scenario!
2022-02-11 08:20:14,857 - __main__ - INFO - Thread: 0 started foo_without_locks
2022-02-11 08:20:14,863 - __main__ - INFO - Thread: 1 started foo_without_locks
2022-02-11 08:20:14,875 - __main__ - INFO - Thread: 0 finished foo_without_locks
2022-02-11 08:20:14,881 - __main__ - INFO - Thread: 1 finished foo_without_locks
2022-02-11 08:20:14,882 - __main__ - WARNING - Count is: -102998 but should be 0!
2022-02-11 08:20:14,882 - __main__ - INFO - 
2022-02-11 08:20:14,882 - __main__ - INFO - Running safe scenario!
2022-02-11 08:20:14,882 - __main__ - INFO - Thread: 0 started foo_with_locks
2022-02-11 08:20:14,893 - __main__ - INFO - Thread: 1 started foo_with_locks
2022-02-11 08:20:14,927 - __main__ - INFO - Thread: 0 finished foo_with_locks
2022-02-11 08:20:14,960 - __main__ - INFO - Thread: 1 finished foo_with_locks
2022-02-11 08:20:14,960 - __main__ - INFO - Count is 0, congratulations!

```

As seen in the output, the `race condition scenario` fails since the `count` is not `0` (you may need to run the script a few times to get the script to fail). This scenario fails since both threads are updating the same resource at the same time. The increment and decrement are atomic operations and need to be executed sequentially. The increase operation can be explained like this (simplified)

1. Read `count`
2. Update `count` with 1
3. Store `count`

The increase operation is **not** atomic (by default), meaning that any thread can jump in during any of the 3 steps above, and therefore store an "incorrect" value for `count`.

Luckily, we can make the increase and decrease operations atomic by using `locks` which we do in scenario 2. By using a global `lock` from the `threading` library we can lock sections of our code to be executed by only one thread. The thread that `acquires` the lock is the thread that can continue executing the code. When the thread has executed the code in the `critical section`, it needs to release the `lock`. Otherwise, other threads will not be able to access the `critical section`. By surrounding the `critical section` with a lock, we make sure that the increment and decrement operations are atomic, and we get the correct value of `count`, namely 0.

When a thread reaches `LOCK.aqquire()`, and the lock is already acquired by another thread, it waits until the `lock` is released by the current thread. 

## Multithreaded - Exceptions

Script name: `multithreaded-exceptions.py`, see [this](multithreaded-exceptions.py). 

TODO!