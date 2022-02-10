# concurrency-python

A collection of documentation, scripts, and POCs related to concurrency in Python.

Each script touches upon a specific problem and shows a corresponding suggested solution, for instance, shared resources or exceptions handling. 

In Python, you can achieve concurrency by using multiple threads or processes, and each has its pros and cons, depending on the situation.

* TODO: Write a bit about the difference between threads and processes.
* TODO: Write a bit about asynchronous execution VS synchronous execution.

There exist a few different libraries and modules for handling concurrency in Python. I will stick to [concurrent.features](https://docs.python.org/3/library/concurrent.futures.html), for asynchronous execution since it is part of pythons standard library.

There will be scripts and explanations for multi-threading and multi-processing, and we will start with multi-threading.