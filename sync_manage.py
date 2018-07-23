# coding: utf-8
import sys


if __name__ == '__main__':

    from crogull_sync.management import run_from_command
    from crogull_sync.app import croture

    from config.local import SETTINGS

    croture.config(SETTINGS)
    run_from_command(sys.argv)
