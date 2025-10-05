import os
from pathlib import Path

from sagi.config.main import get_main_config


def load_config():
    cfg = get_main_config()
    print(cfg)


if __name__ == '__main__':
    load_config()


