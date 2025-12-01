thonpython
import threading
import time
from automation.utils.logger import get_logger

logger = get_logger(__name__)

class Scheduler:
 def __init__(self, settings):
 self.jobs = []
 self.settings = settings
 self.running = False

 def schedule_job(self, func, interval_seconds: int):
 self.jobs.append((func, interval_seconds))
 logger.info(f"Scheduled job every {interval_seconds} seconds: {func.__name__}")

 def start(self):
 self.running = True
 threads = []

 for job_func, interval in self.jobs:
 thread = threading.Thread(target=self._run_job, args=(job_func, interval), daemon=True)
 thread.start()
 threads.append(thread)

 while self.running:
 time.sleep(1)

 def _run_job(self, func, interval):
 while self.running:
 start = time.time()
 func()
 elapsed = time.time() - start
 time.sleep(max(0, interval - elapsed))

 def stop(self):
 self.running = False
 logger.info("Scheduler stopped.")