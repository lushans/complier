#!venv/bin/python3
import argparse
import re
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
    fo = open('myc.c', "r")
    lexer = lexer.main(fo)
    parse.main(lexer)




    




