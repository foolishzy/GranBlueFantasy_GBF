from jobselect import jobselect
import sys
from jobargs import jobargs
if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        jobselect()
    else:
        jobargs(args)
