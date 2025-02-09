# Day1
## ==**今日必须掌握**==
- [ ] 变量命名规则(字母/下划线开头，区分大小写)
- [ ] 能用f-string格式化包含变量的字符串
- [ ] 能创建列表并使用append()添加元素
- [ ] 能用input()获取输入并与print()结合

##### 终端清屏命令：cls


## 一.Python的定义
python是一行一行运行的语言，并且可以随时修改变量的值
### 基础数据类型
    name = 'Alice' #字符串(Str)类型
    age = 20 #整数(int)类型
    height = 1.75 #浮点数(float)
    is_student = True #布尔值(bool)


## 二.变量
**变量名命名规则：**
1.只能包括字母，数字和下划线_  
2.变量名能以数字和下划线打头，不能以数字打头
3.变量名中不能含空格，但可以用下划线代替空格 
4.不能将python关键字和函数名用作变量名
5.变量名应简短又具有描述性，例如name比n好，student_name比s_n好，name_length比length_of_person_name好
6.慎用小写字母l和大写字母O，因为他们可能会被看重错成数字1和0

### Python关键字
|and| as| assert| async|await| break|
| :----: | :----: | :----: | :----: | :----: | :----: |
|False|None|True|class|continue|def|
|del|elif|else|except|finally|for|
from|global|if|import|in|is|
|lambda|nonlocal|not|or|pass|raise|
|return|try|while|with|yield|
---
## 三.字符串
### 1.定义
在python中，用引号引起的字符就是字符串，出现引号才有字符串，可以是单引号或者双引号。如

    print('this is python world!')
其中的 'this is python world!'就是一个字符串
- 将字符串转大写，小写，首字母大写的方法
```
    name = 'adv lovelace'
    print(name.title()) #name.title 将字符串转首字母大写的内置函数
    print(name.upper()) #name.upper 将字符串全部转为大写
    name = 'ADV LOVELACE'
    print(name.lower()) #将字符串全部转为小写
``` 
## 四.列表
### 1.定义
列表(list)是由一系列按特定顺序排列的元素组成。类似于集合。列表中每个元素都有其对应的索引数字，例如

```
list = ['妈妈','爸爸','我']
其中妈妈的索引数字是0，爸爸的索引数字是1，我的索引数字是2
list[0] 会返回 '妈妈'
list[1] 会返回 '爸爸'
list[2] 则会返回 '我'
列表中各个元素之间使用逗号隔开
```

## 五.今日练习——BMI计算器
```python
weight = float(input("体重(KG):"))
height = float(input("身高(M)"))
BMI = weight / (height ** 2)
if BMI < 18.5:
    deep = '体重过轻'
elif BMI < 24.9:
    deep = '体重正常'
elif BMI <29.9:
    deep = '体重超重，应该适当运动！'
else:
    deep = '过于肥胖，请努力减肥，保持健康！'
print(f'您的BMI指数为：{BMI:.1F},{deep}')  #:.1F表示保留小数点后一位
```