import lexer

# 语法分析部分

def main(lexer):
    i = 0
    j = 0
    t = 1
    ## 将分析结果输出到控制台 并存入文件 ./output/lexer.txt
    out_parse = open("./output/parse.txt","w")
    temp = "<程序>"
    while j<len(lexer):
        print(temp[i:])
        print(lexer[j].getValue())
        if temp == "<程序>":
            temp = temp.replace("<程序>","<main关键字>(){<声明序列><语句序列>}",1)
            print("%d <程序>→<main关键字>(){<声明序列><语句序列>}" % t)
            print("%d <程序>→<main关键字>(){<声明序列><语句序列>}" % t,file=out_parse)
            t += 1
            i -= 1
        elif temp[i:i+9] == "<main关键字>" and lexer[j].getValue() == "main" and lexer[j+1].getValue() == "(" and lexer[j+2].getValue() == ")" and lexer[j+3].getValue() == "{":
            temp = temp.replace("<main关键字>","main",1)
            print("%d <main关键字>→main" % t)
            print("%d <main关键字>→main" % t,file=out_parse)
            i = i+6
            j = j+4
            t += 1
        elif temp[i:i+6] == "<声明序列>":
            if lexer[j].getValue() == "int":
                temp = temp.replace("<声明序列>","<声明语句><声明序列>",1)
                print("%d <声明序列>→<声明语句><声明序列>" % t)
                print("%d <声明序列>→<声明语句><声明序列>" % t,file=out_parse)
                i -= 1
                t += 1
            else:
                temp = temp.replace("<声明序列>","", 1)
                print("%d <声明序列>→<空>" % t)
                print("%d <声明序列>→<空>" % t,file=out_parse)
                i -= 1
                t += 1
        elif temp[i:i+6] == "<声明语句>":
            temp = temp.replace("<声明语句>", "<int关键字><标识符表>;", 1)
            print("%d <声明语句>→<int关键字><标识符表>;" % t)
            print("%d <声明语句>→<int关键字><标识符表>;" % t,file=out_parse)
            i -= 1
            t += 1
        elif temp[i:i+8] == "<int关键字>" and lexer[j].getValue() == "int":
            temp = temp.replace("<int关键字>", "int", 1)
            print("%d <int关键字>→int" % t)
            print("%d <int关键字>→int" % t,file=out_parse)
            t += 1
            i += 2
            j += 1
        elif temp[i:i+6] == "<标识符表>":
            temp = temp.replace("<标识符表>","<标识符>",1)
            print("%d <标识符表>→<标识符>" % t)
            print("%d <标识符表>→<标识符>" % t,file=out_parse)
            t += 1
            i -= 1
        elif temp[i:i+5] == "<标识符>":
            if lexer[j].getTag() == "IDENTER":
                temp = temp.replace("<标识符>", lexer[j].getValue(), 1)
                print("%d <标识符>→<字母>" % t)
                print("%d <标识符>→<字母>" % t,file=out_parse)
                t += 1
                j += 1
        elif temp[i:i+6] == "<语句序列>":
            if  lexer[j].getValue() != "}" and lexer[j].getValue() != ")":
                    temp = temp.replace("<语句序列>", "<语句><语句序列>", 1)
                    print("%d <语句序列>→<语句><语句序列>" % t)
                    print("%d <语句序列>→<语句><语句序列>" % t,file=out_parse)
                    t += 1
                    i -= 1
            else:
                    temp = temp.replace("<语句序列>", "", 1)
                    print("%d <语句序列>→<空>" % t)
                    print("%d <语句序列>→<空>" % t,file=out_parse)
                    t += 1
                    i -= 1
        elif temp[i:i+4] == "<语句>":
            if lexer[j+1].getValue() == "=":
                temp = temp.replace("<语句>", "<赋值语句>", 1)
                print("%d <语句>→<赋值语句>" % t)
                print("%d <语句>→<赋值语句>" % t,file=out_parse)
                t += 1
                i -= 1
            elif lexer[j].getValue() == "for":
                temp = temp.replace("<语句>", "<for语句>", 1)
                print("%d <语句>→<for语句>" % t)
                print("%d <语句>→<for语句>" % t,file=out_parse)
                t += 1
                i -= 1
            elif lexer[j].getValue() == "print":
                temp = temp.replace("<语句>", "<print语句>", 1)
                print("%d <语句>→<print语句>" % t)
                print("%d <语句>→<print语句>" % t,file=out_parse)
                t += 1
                i -= 1
        elif temp[i:i+7] == "<for语句>":
            temp = temp.replace("<for语句>", "<for关键字>(<表达式>;<表达式>;<表达式>)<复合语句>", 1)
            print("%d <for语句>→<for关键字>(<表达式>;<表达式>;<表达式>)<复合语句>" % t)
            print("%d <for语句>→<for关键字>(<表达式>;<表达式>;<表达式>)<复合语句>" % t,file=out_parse)
            t += 1
            i -= 1
        elif temp[i:i+8] == "<for关键字>" and lexer[j].getValue() == "for":
            temp = temp.replace("<for关键字>", "for", 1)
            print("%d <for关键字>→for" % t)
            print("%d <for关键字>→for" % t,file=out_parse)
            t += 1
            i += 2
            j += 1
        elif temp[i:i+6] == "<赋值语句>":
            temp = temp.replace("<赋值语句>", "<表达式>;", 1)
            print("%d <赋值语句>→<表达式>;" % t)
            print("%d <赋值语句>→<表达式>;" % t,file=out_parse)
            t += 1
            i -= 1
        elif temp[i:i+5] == "<表达式>":
            if lexer[j+1].getValue() == "=" or lexer[j+1].getValue() == ")":
                temp = temp.replace("<表达式>", "<标识符>=<算数表达式>", 1)
                print("%d <表达式>→<标识符>=<算数表达式>" % t)
                print("%d <表达式>→<标识符>=<算数表达式>" % t,file=out_parse)
                t += 1
                i -= 1
            elif lexer[j+1].getValue() == "<" or lexer[j+1].getValue() == ">":
                temp = temp.replace("<表达式>", "<布尔表达式>", 1)
                print("%d <表达式>→<布尔表达式>" % t)
                print("%d <表达式>→<布尔表达式>" % t,file=out_parse)
                t += 1
                i -= 1
        elif temp[i:i+7] == "<关系运算符>":
            if lexer[j].getValue() == ">" or lexer[j].getValue() == "<":
                temp = temp.replace("<关系运算符>", lexer[j].getValue(), 1)
                print("%d <布尔表达式>→%s" % (t,lexer[j].getValue()))
                print("%d <布尔表达式>→%s" % (t, lexer[j].getValue()),file=out_parse)
                t += 1
                i -= 1
        elif temp[i:i+6] == "<复合语句>":
            temp = temp.replace("<复合语句>", "{<语句序列>}", 1)
            print("%d  <复合语句>→{<语句序列>}" % t)
            print("%d  <复合语句>→{<语句序列>}" % t,file=out_parse)
            t += 1
            i -= 1
        elif temp[i:i+7] == "<布尔表达式>":
            temp = temp.replace("<布尔表达式>", "<算数表达式><关系运算符><算数表达式>", 1)
            print("%d <布尔表达式>→<算数表达式><关系运算符><算数表达式>" % t)
            print("%d <布尔表达式>→<算数表达式><关系运算符><算数表达式>" % t,file=out_parse)
            t += 1
            i -= 1
        elif temp[i:i+7] == "<算数表达式>":
            if lexer[j+1].getValue() == "+":
                temp = temp.replace("<算数表达式>", "<项>+<算数表达式>", 1)
                print("%d <算数表达式>→<项>+<算数表达式>" % t)
                print("%d <算数表达式>→<项>+<算数表达式>" % t,file=out_parse)
                t += 1
                i -= 1
            elif lexer[j+1].getValue() == "-":
                temp = temp.replace("<算数表达式>", "<项>-<算数表达式>", 1)
                print("%d <算数表达式>→<项>-<算数表达式>" % t)
                print("%d <算数表达式>→<项>-<算数表达式>" % t,file=out_parse)
                t += 1
                i -= 1
            elif lexer[j+1].getValue() == ";" or lexer[j+1].getValue() == "<" or lexer[j+1].getValue() == ")":
                temp = temp.replace("<算数表达式>","<项>", 1)
                print("%d <算数表达式>→<项>" % t)
                print("%d <算数表达式>→<项>" % t,file=out_parse)
                t += 1
                i -= 1
        elif temp[i:i+3] == "<项>":
            temp = temp.replace("<项>", "<因子>", 1)
            print("%d <项>→<因子>" % t)
            print("%d <项>→<因子>" % t,file=out_parse)
            t += 1
            i -= 1
        elif temp[i:i+4] == "<因子>":
            if lexer[j].getValue().isnumeric():
                temp = temp.replace("<因子>", "<无符号整数>", 1)
                print("%d <因子>→<无符号整数>" % t)
                print("%d <因子>→<无符号整数>" % t,file=out_parse)
                t += 1
                i += 6
                j += 1
            else:
                temp = temp.replace("<因子>", lexer[j].getValue(), 1)
                print("%d <因子>→<标识符>" % t)
                print("%d <因子>→<标识符>" % t,file=out_parse)
                t += 1
                j += 1
        elif temp[i:i+5] == "<标识符>":
            temp = temp.replace("<标识符>", lexer[j].getValue(), 1)
            print("%d <标识符>→<字母>" % t)
            print("%d <标识符>→<字母>" % t,file=out_parse)
            t += 1
            j += 1
        elif temp[i:i+9] == "<print语句>":
            temp = temp.replace("<print语句>", "<print关键字><算数表达式>;", 1)
            print("%d <print语句>→<print关键字><表达式>;" % t)
            print("%d <print语句>→<print关键字><表达式>;" % t,file=out_parse)
            t += 1
            i -= 1
        elif temp[i:i+10] == "<print关键字>":
            if lexer[j].getValue() == "print":
                temp = temp.replace("<print关键字>", "print", 1)
                print("%d <print关键字>→print" % t)
                print("%d <print关键字>→print" % t,file=out_parse)
                t += 1
                i += 4
                j += 1
        elif temp[i] == ";" or temp[i] == ")" or temp[i] == "}" or temp[i] == "=" or temp[i] == "+" or temp[i] == "(" or temp[i] == "<" or temp[i] == ">" or temp[i] == "{":
            if lexer[j].getValue() != temp[i]:
                print("Error")
            else:
                j += 1
        i += 1
        print("--------------------------------")

