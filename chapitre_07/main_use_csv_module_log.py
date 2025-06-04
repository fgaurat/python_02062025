import csv
import logging
import logging.config

import configparser

logging.config.fileConfig('config.ini')
logger = logging.getLogger('simpleExample')

# logging.basicConfig(filename="test.log",level=logging.INFO,format="%(name)s - %(asctime)s: %(message)s")
# logger = logging.getLogger(__name__)


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # csv_file = "MOCK_DATA.csv"
    csv_file = config['APP']["csv_file"]
    with open(csv_file) as f:
        reader = csv.DictReader(f,delimiter=";")
        for d in reader:
            logger.info(d['last_name'])
            # print(d)

if __name__=='__main__':
    main()
