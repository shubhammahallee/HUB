import logging
import os

class Log_details:

    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Report", "test_log.log")

    @staticmethod
    def get_logger():
        logging.basicConfig(
            filename= "demo.log",
            level = logging.INFO,
            format = '%(asctime)s - %(levelname)s - %(message)s',
            datefmt = '%Y-%m-%d %H:%M:%S %p'
        )
        return logging.getLogger()

