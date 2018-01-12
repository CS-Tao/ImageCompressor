import os
import sys

if __name__ == '__main__':
    print(sys.path[0])
    os.system('python ' + sys.path[0] + '\ImageCompressor.py' + ' -i ./input/ -o ./output/ -s 4')
    input()