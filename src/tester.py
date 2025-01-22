import os

import src.log
from src.log import log_info

def test():
    cp = os.path.join(os.path.dirname(os.path.dirname(__file__)), "secret", "config.yaml")
    print(cp)