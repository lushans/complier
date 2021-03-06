import re



# Token类 存储
class Tokens:
    #定义构造方法 tokens字典 存储所有token和taken的tag
    def __init__(self, tokens):
        self.tokens = tokens
    #判断字符串是否为token
    def intokens(self,str):
        if str in self.tokens.keys():
            return True
        else:
            return False
    #获得token的tag
    def getTag(self,string):
        return self.tokens[string]



# 词法分析模块

class Token:
    '''记录分析出来的单词'''
    def __init__(self, tag,value):
        self.tag =  tag
        self.value = value
    def getTag(self):
        return self.tag
    def getValue(self):
        return self.value

# 关键字对象(Keyword)
keyword_tokens = {
    'int' : 'KW_INT',
    'main' : 'KW_MAIN',
    'if' : 'KW_IF',
    'else' : 'KW_ELSE',
    'for' : "KW_FOR",
    'return' : "KW_RETURN",
    'print' : "KW_PRINT"
}
KW = Tokens(keyword_tokens)

# 界符对象(Boundary)
boundary_tokens = {
    '{' : 'LBRAC',
    '}' : 'RBRAC',
    '(' : 'LPAREN',
    ')' : 'RPAREN',
    ',' : 'COMMA',
    ';' : 'SEMICON'
}
BD = Tokens(boundary_tokens)

# 运算符对象()
operato_tokens = {
    '=' : 'OP_ASSIGN',
    '-' : 'OP_SUB',
    '+' : 'OP_ADD',
    '++' : 'OP_INC',
    '--' : 'OP_DEC',
    '*' : 'OP_MUL',
    '/' : 'OP_DIV',
    '<' : 'OP_LT',
    '<=' : 'OP_LE',
    '>' : 'OP_GT',
    '>=' : 'OP_GE',
    '==' : 'OP_EQU',
    '!=' : 'OP_NEQU',
    '>>' : 'OP_IN',
    '<<' : 'OP_OUT'
}
OP = Tokens(operato_tokens)

# 子函数
## 判断 是否为运算符
def op(source,index):
    if index < len(source) and (source[index + 1] == "+" or source[index + 1] == "-" or source[index + 1] == "*" or source[index + 1] == "/" or \
        source[index + 1] == ">" or source[index + 1] == "<" or source[index + 1] == "=" or source[index + 1] == "!"):
        tokens.append(Token(OP.getTag(source[index:index + 2]),source[index:index + 2]))
        return index+1
    else:
        tokens.append(Token(OP.getTag(source[index]), source[index]))
        return index

## 判断 是否为界符
def Bou(source, index):
    tokens.append(Token(BD.getTag(source[index]), source[index]))

## 判断 是否为数字
def num(source,index):
    x = 1;
    while index+x < len(source) and ('0' <= source[index+x] <= "9" or source == "."):
        x += 1;
    if "."  in source[index:index+x]:
        tokens.append(Token("NUM_FLOAT",source[index:index+x]))
    else:
        tokens.append(Token("NUM_INT", source[index:index+x]))
    return index+x-1

## 判断 是否为关键字或标识符
def kw(source,index):
    x = 1
    while index+x < len(source) and ("0" <= source[index+x] <= "9" or source[index+x] == "_" or "a" <= source[index+x] <= "z" or "A" <= source[index+x] <= "Z"):
        x += 1
    '查询是否为关键字，若 keyError 则说明不是关键字 存入标识符中'
    try:
        tokens.append(Token(KW.getTag(source[index:index+x]),source[index:index+x]))
    except KeyError:
        tokens.append(Token("IDENTER",source[index:index+x]))
    return index+x-1;


def main(fo):
    global tokens
    global out_lexer
    print("开始词法分析......")
    index = 0
    t = 1
    tokens = []
    source = re.sub("\s+"," ",fo.read())
    while index < len(source):
        # 判定运算符
        if source[index] == "+" or source[index] == "-" or source[index] == "*" or source[index] == "/" or source[index] == ">" or source[index] == "<"   or source[index] == "=" or source[index] == "!":
            index = op(source,index)
        # 判定界符
        elif source[index] == "," or source[index] == ";" or source[index] == "{" or source[index] == "}" or source[index] == "(" or source[index] == ")":
            Bou(source,index)
        # 判定数字
        elif '0' <= source[index] <= "9":
            index = num(source,index)
        # 判定标识符或关键字
        elif source[index] == "_" or "a" <= source[index] <= "z" or "A" <= source[index] <= "Z":
            index = kw(source,index)
        index += 1
    ## 将分析结果输出到控制台 并存入文件 ./output/lexer.txt
    out_lexer = open("./output/lexer.txt","w")
    for index in range(len(tokens)):
        print("{0} ({1}, {2})".format(t,tokens[index].getTag(),tokens[index].getValue()))
        print("{0} ({1}, {2})".format(t,tokens[index].getTag(),tokens[index].getValue()),file=out_lexer)
        t += 1
    out_lexer.close()
    print("\n\n")
    return tokens
