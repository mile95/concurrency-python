# concurrency-python

A collection of documentation, scripts, and POCs related to concurrency in Python.

Each script touches upon a specific problem and shows a corresponding suggested solution, for instance, shared resources or exceptions handling. 

In Python, you can achieve concurrency by using multiple threads or processes, and each has its pros and cons, depending on the situation.

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

TODO!

## Multithreaded - Exceptions

Script name: `multithreaded-exceptions.py`, see [this](multithreaded-exceptions.py).

TODO!