import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #logfile name
logs_path=os.path.join(os.getcwd(),"logs") #src/logs/LOG_FILE -> new floder with LOG_FILE is created inside it new file with LOG_FILE.log is created with makedirs()
os.makedirs(logs_path,exist_ok=True) #file is made at logs_path with LOG_FILE.log name on it

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) #storing path in constant

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == '__main__':
     logging.info("Logging started")