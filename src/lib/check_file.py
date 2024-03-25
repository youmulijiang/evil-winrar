import os

def check_file(path:str,hook=None):
    if not os.path.isfile(path):
        print(f"{path}不是文件")
        if hook is not None:
            return hook()

