import subprocess
command = 'pyinstaller "Website User Builder.spec"'
proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
