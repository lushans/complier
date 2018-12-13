## 词法
```python
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
```

```python
# 界符对象(Boundary)
boundary_tokens = {
    '{' : 'LBRAC',
    '}' : 'RBRAC',
    '(' : 'LPAREN',
    ')' : 'RPAREN',
    ',' : 'COMMA',
    ';' : 'SEMICON'
}
```

```python
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
```

## 语法
1. <程序>→<main关键字>(){<声明序列><语句序列>}
2. <main关键字>→main
3. <声明序列>→<声明语句><声明序列>|<空>
4. <声明语句>→<int关键字><标识符表>;
5. <int关键字>→int
6. <标识符表>→<标识符>
7. <标识符>→<字母>
8. <语句序列>→<语句><语句序列>
9. <语句>→<赋值语句>|<for语句>|<print语句>
10. <赋值语句>→<表达式>;
11. <表达式>→<标识符>=<算数表达式>|<布尔表达式>
12. <算数表达式>→<项>+<算数表达式>|<项>-<算数表达式>|<项>
13. <项>→<因子>
15. <因子>→<无符号整数>|<标识符>
16. <标识符>→<字母>
17. <for语句>→<for关键字>(<表达式>;<表达式>;<表达式>)<复合语句>
18. <for关键字>→for
19. <布尔表达式>→<算数表达式><关系运算符><算数表达式>
20. <关系运算符>→>|<
21. <复合语句>→{<语句序列>}
22. <print语句>→<print关键字><表达式>;
23. <print关键字>→print
