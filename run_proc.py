import os
import platform
import subprocess

MSG_CANNOT_RUN = "Cannot run Pandoc. Make sure it's in your PATH."

#
# Linux: package "nodejs" installs binary "nodejs"
# Mac: need to specify path
#
RUN_FILE = 'pandoc'
s = platform.system()
if s == 'Darwin':
    RUN_FILE = '/usr/local/bin/pandoc'


def run(text, params_list):
    enc = 'utf8'
    if os.name == 'nt':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE
        try:
            p = subprocess.Popen([RUN_FILE] + params_list,
              startupinfo=startupinfo,
              stdout=subprocess.PIPE,
              stdin=subprocess.PIPE,
              stderr=subprocess.PIPE)
        except OSError:
            raise Exception(MSG_CANNOT_RUN)
    else:
        try:
            p = subprocess.Popen([RUN_FILE] + params_list,
              stdout=subprocess.PIPE,
              stdin=subprocess.PIPE,
              stderr=subprocess.PIPE)
        except OSError:
            raise Exception(MSG_CANNOT_RUN)


    stdout, stderr = p.communicate(text.encode(enc))
    if stdout:
        return stdout.decode(enc)
    else:
        raise Exception('Error:\n' + stderr.decode(enc))
