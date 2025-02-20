# Day3

## 一.while循环
### 1.定义
与for循环不同，while循环根据指定的条件循环，只有当条件不再满足时，while才会结束循环；而for循环会根据你限制的条件遍历这个条件下集合中的每一个元素。
- while循环适合用于不确定循环次数的情况，比如需要等待某个条件满足时才停止。
- for循环适合用于遍历已知的集合或范围，或者需要明确知道循环次数的情况。
### 2.代码
```
#在列表之间移动元素
unconfirmed_users = ['jack','bide','pake']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user:{current_user.title()}')
    confirmed_users.append(current_user)
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```
- 这个代码实现了将已注册但是未验证的用户转移到已验证用户列表中的操作。**列表之间移动元素**
1.首先，创建了一个含有三个未验证用户的列表，以及一个用来存储已验证用户的空列表。
2.接着建立了条件循环**while**，只要unconfirmed_users这个列表中有元素（True），那么就会执行循环内的语句，如果列表为空（False），那么就会结束循环。
3.然后用**pop方法**将列表中的最后一个元素移除并返回给变量current_user，紧接着输出此变量存储的这个用户
4.最后使用**append方法**将变量存储的用户添加到事先创建好的空列表中，至此第一次循环结束。这里需要注意的是循环下面的语句只有循环结束才会执行，而并非每一次循环都执行一次下面的语句。**循环外部的代码只会在循环完全结束后执行**
5.紧接着开始第二、三次循环，与第一次循环相同，唯一不同的地方是变量current_user的值有所变化，原有的值被现有的值顶替了。
6.循环结束后，用for循环遍历输出已验证用户列表中的每一个用户，用**title方法**将用户的首字母转大写。

## 二.循环与range
```
for i in range(0,9,3):   
    print(f"当前值：{i}")
```
- 这个循环利用range生成一个0到9的整数序列，其中步长为3，如果不指定步长则默认为1，步长可以为负
- for i in range()中如果i在下面的循环不使用，则可以用通配符_取代，这种用法只强调循环次数而不使用每次遍历的变量值，用通配符取代它们意在表示这些变量是无关紧要的

## 三.循环中断控制及与字符串的联动
```
#实时响应用户输入的退出机制
while True:
    cmd = input("请输入指令（q）退出:")
    if cmd == 'q':
        break
    print(f"执行：{cmd}")
```
- 这段代码获取用户的输入，当用户输入q时，循环结束并且程序终止运行，当用户输入非q时，则打印用户的输入并且接着循环直到程序终止运行

```
for char in Text:
    if char.isupper():   
        print(f'发现大写字母:{char}')
```
- 这行代码中的**isupper**方法用来检测字符串中的字母字符是否大写，如果字母字符全部为大写则返回True，如果不是则返回False