#密码生成
'''
import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@!*'
length = int(input('请输入您想生成的密码长度(8-16)：'))
password = []
perv_str = ''
for _ in range(length):
    while True:
        char = random.choice(chars)
        if char != perv_str:
            password.append(char)
            perv_str = char
            break
print("生成密码为："+''.join(password))
'''
'''
#密码要求，八位到十六位，必须包含数字，大写字母，小写字母，特殊符号，并且密码中的字符不能重复并且相邻
import random
nums = '0123456789'
daxies = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
xiaoxies = 'abcdefghijklmnopqrstuvwxyz'
fuhaos = '@!*'
length = int(input('请输入生成密码的长度（8-16）：'))
password = []
perv_str = ''
for _ in range(length):
    while True:
        num = random.choice(nums)
        daxie = random.choice(daxies)
        xiaoxie = random.choice(xiaoxies)
        fuhao = random.choice(fuhaos)  #暂未完成
'''
