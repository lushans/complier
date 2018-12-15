#!venv/bin/python3
import os
import lexer
import parse

# 命令行解析 获得源码文件
#
# def getarg():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("file", help="choose a my_c source file")
#     args = parser.parse_args()
#     return args.file

if __name__ == "__main__":
    #path = getarg()
    try:
        fo = open('myc.c', "r")
    except IOError:
        print("ERROR: FILE NOT FOUND!")
        os._exit(0)
    lexer = lexer.main(fo)
    fo.close()
    parse.main(lexer)






