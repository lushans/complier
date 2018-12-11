# Token类
class Tokens:
    #定义构造方法
    def __init__(self, tokens):
        self.tokens = tokens
    #判断字符串是否为token
    def intokens(self,str):
        if str in self.tokens.keys():
            return True
        else:
            return False
    #获得token的key
    def getTag(self,string):
        return self.tokens[string]
