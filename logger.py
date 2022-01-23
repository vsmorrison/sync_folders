import logging
import sys


def make_logger(log_path, time):
    logger = logging.getLogger("sync_log")
    logger.setLevel(logging.INFO)
    log_file = logging.FileHandler(
        filename=f'{log_path}/Sync report [{time}].log'
    )
    log_format = logging.Formatter('[%(asctime)s] %(levelname)s -- %(message)s')
    log_file.setFormatter(log_format)
    logger.addHandler(log_file)
    terminal_output = logging.StreamHandler(sys.stdout)
    terminal_output.setFormatter(log_format)
    logger.addHandler(terminal_output)
    return logger
