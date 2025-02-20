#遍历字符串并处理
Text = 'AI Revolution'
for char in Text:
    if char.isupper():   #isupper用来检测字符串中字符是否大写，如果全部大写则True，如果不是则False
        print(f'发现大写字母:{char}')