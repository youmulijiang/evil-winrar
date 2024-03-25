import smtplib
from email.message import EmailMessage
import ssl
import mimetypes
import os


context = ssl.create_default_context()
mimetypes.init()

email = EmailMessage()


class EmailClient():
    def __init__(self,host,port,email_addr:str|list[str],email_password) -> None:
        self.host = host
        self.port = port
        self.email_addr = email_addr
        self.passwd = email_password

    def do_content(self,From:str=None,Subject:str=None,content=None,file=None):
        email["From"]=self.email_addr
        if From is not None:
            email["From"] = From
        email["Subject"] = Subject
        if content is not None:
            email.set_content(content)
        if file is not None:
            while True:
                if os.path.isfile(file):
                    with open(file,"rb+") as file:
                        email.set_content(file)
                    break
                else:
                    print("该路径不存在")
                    file = input("请重新输入文件路径: ")
        return self
    
    def set_file(self,file_path:str,filename:str):
        if not filename.endswith(".rar"):
            filename = filename + ".rar"
        with open(file_path,"rb+") as file:
            file_content = file.read()
            email.add_attachment(file_content,maintype=(mimetypes.guess_type(file_path))[0],subtype="",filename=filename)
        
        return self

    def send(self,addr,addr_list:str=None):
        with smtplib.SMTP_SSL(host=self.host,port=self.port,context=context) as smtp:
            smtp.login(self.email_addr,self.passwd)
            if addr_list is not None:
                for addr in addr_list.split(','):
                    email["To"] = addr
                    smtp.send_message(email)
                    print(f"成功向{addr}发送邮件")
            else:
                email["To"]=addr
                smtp.send_message(email)
                addr = email["To"]
                print(f"成功向{addr}发送邮件")

    def send_one(self,addr):
        with smtplib.SMTP_SSL(host=self.host,port=self.port,context=context) as smtp:
            smtp.login(self.email_addr,self.passwd)
            email["To"]=addr
            smtp.send_message(email)
            print(f"成功向{addr}发送邮件")

    def send_everyone(self,addr_list:list):
        with smtplib.SMTP_SSL(host=self.host,port=self.port,context=context) as smtp:
            smtp.login(self.email_addr,self.passwd)
        
        #     email["To"] = addr
            email["To"] = addr_list
            smtp.send_message(email)
            for addr in addr_list:
                print(f"成功向{addr}发送邮件")

    def filelist_send(self,filepath:str):
        if not os.path.isfile(filepath):
            exit("该路径不是一个文件")
        with open(filepath,"r") as file:
            addr_list = file.readlines()
            with smtplib.SMTP_SSL(host=self.host,port=self.port,context=context) as smtp:
                smtp.login(self.email_addr,self.passwd)
                # for addr in addr_list:
                email['To'] = addr_list
                smtp.send_message(email)
                for addr in addr_list:
                    print(f"成功向{addr}发送邮件")
                
        
            

        
    