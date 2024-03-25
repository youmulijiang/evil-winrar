from http.server import SimpleHTTPRequestHandler,ThreadingHTTPServer
import configparser
from pathlib import Path
from src.lib.colorprint import Color,cprint



conf = configparser.ConfigParser()
conf.read("D:\开发系列\开发练习\安全开发2\evil-winrar\config\config.ini")
host = conf.get("http-server","httpserver-host")
port = conf.get("http-server","port")
url_download_path = conf.get("http-server","url_download_path")
download_payload_name = conf.get("http-server","download_payload_name")
    
input_shuffix = cprint("httpserver> ",style=Color.PURPLE,isstr=True)

def get_paload_path():
    global payload_path
    try:
        while True:
            payload_path = input("请输入要payload的位置: ")
            if Path(payload_path).exists():
                if Path(payload_path).is_file():
                    break 
                else:
                    print("该路径是个目录,不是文件,请重新输入")
            else:
                print("该路径不存在,请重新输入")
    except:
        pass

class DownLoaderHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == f'{url_download_path}':
            self.send_response(200)
            self.send_header('Content-Disposition', f'attachment; filename="{download_payload_name}"')
            self.send_header('Content-Type', 'application/octet-stream')
            self.end_headers()
            with open(payload_path, 'rb') as f:
                self.wfile.write(f.read())
        else:  
            super().do_GET() 


def HttpServer_start(host=host,port=port):
    port = int(port)
    addr = (host,port)
    with ThreadingHTTPServer(addr,DownLoaderHandler) as server:
        print(f"url下载地址是:http://{host}:{port}{url_download_path}")
        server.serve_forever()

def HttpServer_SSL_start(host,port,certfile=None,keyfile=None):
    import ssl
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    if certfile is not None or keyfile is not None:
        ssl_context.load_cert_chain(certfile=certfile, keyfile=keyfile)
    port = int(port)
    addr = (host,port)
    with ThreadingHTTPServer(addr,DownLoaderHandler) as server:
        server.socket = ssl_context.wrap_socket(server.socket, server_side=True)
        print(f"url下载地址是:https://{host}:{port}{url_download_path}")
        server.serve_forever()


def http_server_main():
    global host, port, url_download_path, download_payload_name
    global payload_path
    while True:
        ok=input(f"{input_shuffix}是否使用配置文件对下载服务器进行初始化(yes/no): ").lower()
        if ok == "yes":
            break
        elif ok == "no":
            host = input(f"{input_shuffix}请输入下载服务器启动地址: ")
            port = input(f"{input_shuffix}请输入下载服务器启动的端口: ")
            certfile = input(f"{input_shuffix}请输入下载服务器certfile(选填): ")
            keyfile = input(f"{input_shuffix}请输入下载服务器keyfile(选填): ")
            url_download_path = input(f"{input_shuffix}请输入payload的下载路径,exp:download: ")
            download_payload_name = input(f"{input_shuffix}请输入payload的名字: ")
            break
        else:
            print("无效选项,请重新输入")
    get_paload_path()
    while True:
        ok = input(f"{input_shuffix}是否启动带ssl(yes/no)").lower()
        if ok == "yes":
            if certfile != '' and keyfile != '':
                print("开启带有ssl的下载服务器")
                HttpServer_SSL_start(host,port,certfile,keyfile)
                break
            else:
                print("检测到没有certfile和keyfile,无法开启带有ssl的下载服务器")
                HttpServer_start(host,port)
                break   
        elif ok == "no": 
            print("开启下载服务器")
            HttpServer_start(host,port)
            break
        else:
            print("输入无效选项,请重新输入:")

# HttpServer_start(host,port)
if __name__ == "__main__":
    http_server_main()
    





