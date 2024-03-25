import platform
import subprocess
import re

computer_platform:str = platform.platform(terse=True)
pattern = re.compile("Windows")

conf_path = "config/config.ini"
def edition():
    if re.match(pattern,computer_platform):
        subprocess.run(f"notepad {conf_path}",shell=True,encoding='utf-8')
    else:
        subprocess.run(f"vim {conf_path}",shell=True,encoding='utf-8')


if __name__ == "__main__":
    edition()

