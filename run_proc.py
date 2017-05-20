import cudatext as app
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
    try:
        subprocess.call(cmd, shell=False)
    except:
        app.msg_box('Error running Pandoc program (not in PATH?)', app.MB_OK+app.MB_ICONERROR)
