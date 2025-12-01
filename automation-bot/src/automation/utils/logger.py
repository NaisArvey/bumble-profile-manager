thonpython
import logging
import os

def get_logger(name: str):
 log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs")
 os.makedirs(log_dir, exist_ok=True)
 log_path = os.path.join(log_dir, "activity.log")

 logging.basicConfig(
 level=logging.INFO,
 format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
 handlers=[
 logging.FileHandler(log_path),
 logging.StreamHandler()
 ]
 )
 return logging.getLogger(name)