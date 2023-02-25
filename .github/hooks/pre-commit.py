import os
import sys
import subprocess

file_types = ('.py',)

flake8_command = 'flake8'
autopep8_command = 'autopep8 -i'

changed_files = subprocess.check_output(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACM']).decode().splitlines()

for filename in changed_files:
    if filename.endswith(file_types):
        # Run Flake8 to check for errors
        flake8_result = subprocess.call([flake8_command, filename])
        if flake8_result != 0:
            print('Flake8 found errors in {}.'.format(filename))
            sys.exit(1)
        subprocess.call([autopep8_command, filename])

sys.exit(0)
