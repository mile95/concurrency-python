import logging
import concurrent.futures
import threading

count = 0
iterations = 200000
LOCK = threading.Lock()

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
LOGGER = logging.getLogger(__name__)


def foo_without_locks(thread_id):
    global count
    LOGGER.info(f"Thread: {thread_id} started foo_without_locks")
    # For every equal thread_id we increase the count with 1
    if thread_id % 2 == 0:
        for _ in range(iterations):
            count += 1
    # For every odd thread_id we decrease the count with 1
    else:
        for _ in range(iterations):
            count -= 1
    LOGGER.info(f"Thread: {thread_id} finished foo_without_locks")


def foo_with_locks(thread_id):
    global count
    LOGGER.info(f"Thread: {thread_id} started foo_with_locks")
    # For every equal thread_id we increase the count with 1
    if thread_id % 2 == 0:
        for _ in range(iterations):
            LOCK.acquire()
            count += 1
            LOCK.release()
    # For every odd thread_id we decrease the count with 1
    else:
        for _ in range(iterations):
            LOCK.acquire()
            count -= 1
            LOCK.release()
    LOGGER.info(f"Thread: {thread_id} finished foo_with_locks")


if __name__ == "__main__":
    LOGGER.info("Running race condition scenario!")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(foo_without_locks, range(2))
    if count != 0:
        LOGGER.warning(f"Count is: {count} but should be 0!")
    else:
        LOGGER.info("Count is 0, congratulations!")

    LOGGER.info("")
    LOGGER.info("Running safe scenario!")
    count = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(foo_with_locks, range(2))
    if count != 0:
        LOGGER.warning(f"Count is: {count} but should be 0!")
    else:
        LOGGER.info("Count is 0, congratulations!")
