# coding: utf-8
import os
import sys

from config.env import env

if __name__ == '__main__':
    os.environ.setdefault("CROGULL_SETTINGS_MODULE", "config." + env)
    from crogull.management import execute_from_command_line
    execute_from_command_line(sys.argv)
