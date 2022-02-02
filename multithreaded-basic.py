import logging
import concurrent.futures
import time
import random

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
LOGGER = logging.getLogger(__name__)


def foo(thread_id):
    sleep_time = random.randint(1, 5)
    LOGGER.info(f"Thread: {thread_id} started foo. Will sleep for: {sleep_time}s")
    time.sleep(sleep_time)
    LOGGER.info(f"Thread: {thread_id} finished foo")


if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(foo, range(5))
