thonpython
from automation.tasks import run_profile_automation
from automation.scheduler import Scheduler
from automation.utils.logger import get_logger
from automation.utils.config_loader import load_settings, load_env_credentials

logger = get_logger(__name__)

def main():
 logger.info("Starting Bumble Profile Manager automation engine.")

 settings = load_settings()
 credentials = load_env_credentials()

 scheduler = Scheduler(settings)
 scheduler.schedule_job(run_profile_automation, interval_seconds=settings.get("schedule", {}).get("interval", 300))

 try:
 scheduler.start()
 except KeyboardInterrupt:
 logger.info("Shutting down gracefully...")
 finally:
 scheduler.stop()

if __name__ == "__main__":
 main()