import logging
import concurrent.futures

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG
)
LOGGER = logging.getLogger(__name__)


def foo_with_exception(thread_id):
    raise Exception(f"Exception in thread id: {thread_id}")

if __name__ == "__main__":
    LOGGER.info("Starting thread 0-4 using executor.map...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = executor.map(foo_with_exception, range(5))
        try:
            for result in results:
                LOGGER.info(result)
        except Exception as e:
            LOGGER.info(e)
    
    LOGGER.info("Starting thread 5-9 using executor.submit...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        future_to_thread = {executor.submit(foo_with_exception, thread_id): thread_id for thread_id in range(5,10)}
        for future in concurrent.futures.as_completed(future_to_thread):
            try:
                future.result()
            except Exception as e:
                LOGGER.info(e)