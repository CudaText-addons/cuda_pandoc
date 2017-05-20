import platform
import subprocess

s = platform.system()
exe = 'pandoc.exe'
if s=='Linux':
    exe = 'pandoc'
elif s=='Darwin':
    exe = '/usr/local/bin/pandoc'


def run_pandoc(params_list):
    cmd = [exe]+params_list
    subprocess.call(cmd, shell=False)
