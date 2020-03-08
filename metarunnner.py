#!/usr/bin/env python3
import importlib
import os

import main
import main_frame


def main_frame_mod_time():
    return int(os.path.getmtime(main_frame.__file__))


def amain():
    last_mod_time = main_frame_mod_time()
    args = main_frame.init()
    while True:
        args = main_frame.init()
        main.draw(*args)
        importlib.reload(main)


if __name__ == '__main__':
    amain()
