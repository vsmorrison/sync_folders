import sync_folders
import argparse
import time
import logger
from datetime import datetime


def main(source, replica, interval, log_path):
    launch_time = datetime.now().strftime("%d.%m.%Y %H-%M-%S")
    log = logger.make_logger(log_path, launch_time)
    while True:
        sync_folders.sync_folders(source, replica, log)
        time.sleep(interval)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('source', type=str, help='source folder')
    parser.add_argument('replica', type=str, help='replica folder')
    parser.add_argument(
        'sync_interval', type=int, help='sync interval in seconds'
    )
    parser.add_argument('log_path', type=str, help='log file path')
    args = parser.parse_args()
    main(args.source, args.replica, args.sync_interval, args.log_path)
