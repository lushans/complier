import lexer

# 语法分析部分

def main(lexer):
    i = 0
    j = 0
    t = 1
    temp = "<程序>"
    while j<len(lexer)-1:
        print(temp[i:])
        print(lexer[j].getValue())
        if temp == "<程序>":
            temp = temp.replace("<程序>","<main关键字>(){<声明序列><语句序列>}",1)
            print("%d <程序>→<main关键字>(){<声明序列><语句序列>}"%t)
            t += 1
            i -= 1
        elif temp[i:i+9] == "<main关键字>" and lexer[j].getValue() == "main" and lexer[j+1].getValue() == "(" and lexer[j+2].getValue() == ")" and lexer[j+3].getValue() == "{":
            temp = temp.replace("<main关键字>","main",1)
            print("%d <main关键字>→main"%t)
            i = i+6
            j = j+4
            t += 1
        elif temp[i:i+6] == "<声明序列>":
            if lexer[j].getValue() == "int":
                temp = temp.replace("<声明序列>","<声明语句><声明序列>",1)
                print("%d <声明序列>→<声明语句><声明序列>"%t)
                i -= 1
                t += 1
            else:
                temp = temp.replace("<声明序列>","", 1)
                print("%d <声明序列>→<空>"%t)
                i -= 1
                t += 1
        elif temp[i:i+6] == "<声明语句>":
            temp = temp.replace("<声明语句>", "<int关键字><标识符表>;", 1)
            print("%d <声明语句>→<int关键字><标识符表>;" % t)
            i -= 1
            t += 1
        elif temp[i:i+8] == "<int关键字>" and lexer[j].getValue() == "int":
            temp = temp.replace("<int关键字>", "int", 1)
            print("%d <int关键字>→int" % t)
            t += 1
            i += 2
            j += 1
        elif temp[i:i+6] == "<标识符表>":
            temp = temp.replace("<标识符表>","<标识符>",1)
            print("%d <标识符表>→<标识符>" %t)
            t += 1
            i -= 1
        elif temp[i:i+5] == "<标识符>":
            if lexer[j].getTag() == "IDENTER":
                temp = temp.replace("<标识符>", lexer[j].getValue(), 1)
                print("%d <标识符>→<字母>"%t)
                t += 1
                j += 1
        elif temp[i:i+6] == "<语句序列>":
            if j+1 < len(lexer):
                if  lexer[j+1].getValue() == "=":
                    temp = temp.replace("<语句序列>", "<语句><语句序列>", 1)
                    print("%d <语句序列>→<语句><语句序列>" % t)
                    t += 1
                    i -= 1
            else:
                print("%d <语句序列>→<空>" % t)
                t += 1
                i -= 1
        elif temp[i:i+4] == "<语句>":
            if lexer[j+1].getValue() == "=":
                temp = temp.replace("<语句>", "<赋值语句>", 1)
                print("%d <语句>→<赋值语句>" % t)
                t += 1
                i -= 1
        elif temp[i:i+6] == "<赋值语句>":
            temp = temp.replace("<赋值语句>", "<表达式>;", 1)
            print("%d <赋值语句>→<表达式>;" % t)
            t += 1
            i -= 1
        elif temp[i:i+5] == "<表达式>":
            temp = temp.replace("<表达式>", "<标识符>=<算数表达式>", 1)
            print("%d <表达式>→<标识符>=<算数表达式>"%t)
            t += 1
            i -= 1
        elif temp[i:i+7] == "<算数表达式>":
            if lexer[j+1].getValue() == "+":
                temp = temp.replace("<算数表达式>", "<项>+<算数表达式>", 1)
                print("%d <算数表达式>→<项>+<算数表达式>" % t)
                t += 1
                i -= 1
            elif lexer[j+1].getValue() == "-":
                temp = temp.replace("<算数表达式>", "<项>-<算数表达式>", 1)
                print("%d <算数表达式>→<项>-<算数表达式>" % t)
                print(j)
                t += 1
                i -= 1
            elif lexer[j+1].getValue() == ";":
                temp = temp.replace("<算数表达式>","<项>", 1)
                print("%d <算数表达式>→<项>" % t)
                t += 1
                i -= 1
        elif temp[i:i+3] == "<项>":
            temp = temp.replace("<项>", "<因子>", 1)
            print("%d <项>→<因子>" % t)
            t += 1
            i -= 1
        elif temp[i:i+4] == "<因子>":
            if lexer[j].getValue().isnumeric():
                temp = temp.replace("<因子>", lexer[j].getValue(), 1)
                print("%d <因子>→<无符号整数>" % t)
                t += 1
                j += 1
            else:
                temp = temp.replace("<因子>", lexer[j].getValue(), 1)
                print("%d <因子>→<标识符>" % t)
                t += 1
                j += 1
        elif temp[i:i+5] == "<标识符>":
            temp = temp.replace("<标识符>", lexer[j].getValue(), 1)
            print("%d <标识符>→<字母>" % t)
            t += 1
            j += 1
        elif temp[i] == ";" or temp[i] == ")" or temp[i] == "}" or temp[i] == "=" or temp[i] == "+":
            if lexer[j].getValue() != temp[i]:
                print("Error")
            else:
                j += 1
        i += 1
        print("--------------------------------")

