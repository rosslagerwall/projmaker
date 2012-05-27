import os
import string
import datetime
from projmaker.utils import *

DATADIR = os.path.abspath(os.path.dirname(sys.argv[0])) + "/../share/projmaker/"

with open(DATADIR + "configure.template", "r") as f:
    CONFIGURE_SCRIPT = string.Template(f.read(-1))

with open(DATADIR + "Makefile.template", "r") as f:
    MAKEFILE = string.Template(f.read(-1))

with open(DATADIR + "README.template", "r") as f:
    README = string.Template(f.read(-1))

with open(DATADIR + "NEWS.template", "r") as f:
    NEWS = string.Template(f.read(-1))

with open(DATADIR + "ChangeLog.template", "r") as f:
    CHANGELOG = string.Template(f.read(-1))

with open(DATADIR + "main.c.template", "r") as f:
    CODE = string.Template(f.read(-1))

with open(DATADIR + "gitignore.template", "r") as f:
    GITIGNORE = string.Template(f.read(-1))


class AutoTooler:

    def __init__(self):
        self._p = {}

    def ask_questions(self):
        self._p['name'] = get_answer("What is your name?")
        self._p['email'] = get_answer("What is your email?")
        self._p['project_name'] = get_answer("What is your project's name?")
        self._p['package_name'] = get_answer("What is your package's name?")
        self._p['exec_name'] = get_answer("What is your executable's name?")
        self._p['version'] = get_answer(
            "What is your project's initial version?")
        self._p['username'] = get_answer("What is your GitHub username?")

    def run(self):
        self._p['underline'] = "=" * len(self._p['project_name'])
        self._p['date'] = datetime.date.today().isoformat()
        self._p['year'] = str(datetime.date.today().year)

        execl('git init ' + self._p['package_name'])
        os.mkdir(self._p['package_name'] + '/src')

        with open(self._p['package_name'] + '/configure.ac', 'w') as out:
            out.write(CONFIGURE_SCRIPT.substitute(self._p))

        with open(self._p['package_name'] + '/Makefile.am', 'w') as out:
            out.write(MAKEFILE.substitute(self._p))

        with open(self._p['package_name'] + '/README', 'w') as out:
            out.write(README.substitute(self._p))

        with open(self._p['package_name'] + '/AUTHORS', 'w') as out:
            print(self._p['name'], file=out)

        with open(self._p['package_name'] + '/NEWS', 'w') as out:
            out.write(NEWS.substitute(self._p))

        with open(self._p['package_name'] + '/ChangeLog', 'w') as out:
            out.write(CHANGELOG.substitute(self._p))

        with open(self._p['package_name'] + '/src/main.c', 'w') as out:
            out.write(CODE.substitute(self._p))

        with open(self._p['package_name'] + '/.gitignore', 'w') as out:
            out.write(GITIGNORE.substitute(self._p))

        os.chdir(self._p['package_name'])
        execl('autoreconf')
        execl('automake --add-missing --copy')
        execl('autoreconf')
