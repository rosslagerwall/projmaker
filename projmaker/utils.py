import sys
import subprocess

def execl(args):
    subprocess.Popen(args, shell=True).wait()

def get_answer(str):
    print(str + " ", end='')
    sys.stdout.flush()
    return sys.stdin.readline().strip()
