from src.termial import terminal
import argparse
from src.lib.colorprint import Color,cprint,zone_print

logo = """ 

▓█████ ██▒   █▓ ▄▄▄       ██▓              █     █░ ██▓ ███▄    █  ██▀███   ▄▄▄       ██▀███  
▓█   ▀▓██░   █▒▒████▄    ▓██▒             ▓█░ █ ░█░▓██▒ ██ ▀█   █ ▓██ ▒ ██▒▒████▄    ▓██ ▒ ██▒
▒███   ▓██  █▒░▒██  ▀█▄  ▒██░             ▒█░ █ ░█ ▒██▒▓██  ▀█ ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██ ░▄█ ▒
▒▓█  ▄  ▒██ █░░░██▄▄▄▄██ ▒██░             ░█░ █ ░█ ░██░▓██▒  ▐▌██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒██▀▀█▄  
░▒████▒  ▒▀█░   ▓█   ▓██▒░██████▒         ░░██▒██▓ ░██░▒██░   ▓██░░██▓ ▒██▒ ▓█   ▓██▒░██▓ ▒██▒
░░ ▒░ ░  ░ ▐░   ▒▒   ▓▒█░░ ▒░▓  ░         ░ ▓░▒ ▒  ░▓  ░ ▒░   ▒ ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░
 ░ ░  ░  ░ ░░    ▒   ▒▒ ░░ ░ ▒  ░           ▒ ░ ░   ▒ ░░ ░░   ░ ▒░  ░▒ ░ ▒░  ▒   ▒▒ ░  ░▒ ░ ▒░
   ░       ░░    ░   ▒     ░ ░              ░   ░   ▒ ░   ░   ░ ░   ░░   ░   ░   ▒     ░░   ░ 
   ░  ░     ░        ░  ░    ░  ░             ░     ░           ░    ░           ░  ░   ░     
           ░                                                                                  
 """

def banner_help():
    help = """ 
    winrar cve-2023-38831漏洞利用框架
    
    生成exp: python evil-winrar.py -b <模板文件> -s <payload> -o <保存目录>
    启动框架: python evil-winrar.py --shell
     """
    
    cprint(help,Color.DARKCYAN)


cprint(logo,style=Color.RED)


parse = argparse.ArgumentParser()
parse.add_argument("--shell",help="开启shell模式",action='store_true')
generate_group = parse.add_argument_group("generate exp")
generate_group.add_argument("-b",help="选择模板文件")
generate_group.add_argument("-s",help="选择要执行的脚本")
generate_group.add_argument("-o",help="选择保存路径")
args = parse.parse_args()

if __name__ == "__main__":
    def main():
        banner_help()
        if args.shell:
            
            try:
                terminal().cmdloop()
            except KeyboardInterrupt as e:
                print("成功退出")
                exit()

    main()






# terminal().cmdloop()