# coding=utf-8
import os
import sys
# sys.path.append(os.path.dirname(sys.path[0]))

from kylib.co_runner import run

if __name__ == '__main__':
    if sys.argv[1]:
        suites_name = sys.argv[1]
    else:
        raise Exception
    run(suites_name)

