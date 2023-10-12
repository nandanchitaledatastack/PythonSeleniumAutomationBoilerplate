import logging
import os
from datetime import datetime

def init_logger():
    root = os.path.abspath(os.curdir)
    logdir = os.path.join(root, 'Logs')
    if not os.path.exists(logdir):
        os.mkdir(logdir)
    log_file = os.path.join(logdir, f'{datetime.now().strftime("_%y_%m_%d")}.log')
    logging.basicConfig(filename=log_file, level=logging.INFO, format=f'%(asctime)s %(levelname)s : %(message)s')