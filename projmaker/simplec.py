import os
import string
import datetime
from projmaker.utils import *

DATADIR = os.path.abspath(os.path.dirname(sys.argv[0])) + "/../share/projmaker/"

with open(DATADIR + "Makefile.simple.template", "r") as f:
    MAKEFILE = string.Template(f.read(-1))

with open(DATADIR + "simpleprog.c.template", "r") as f:
    PROG = string.Template(f.read(-1))


class SimpleC:

    def __init__(self):
        self._p = {}

    def ask_questions(self):
        self._p['exec_name'] = get_answer("What is your executable's name?")

    def run(self):
        with open('Makefile', 'w') as out:
            out.write(MAKEFILE.substitute(self._p))

        with open(self._p['exec_name'] + '.c', 'w') as out:
            out.write(PROG.substitute(self._p))
