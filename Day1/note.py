#python是一行一行运行的语言，并且可以随时修改变量的值
#变量名命名规则：1，只能包括字母，数字和下划线_  2. 变量名能以数字和下划线打头，不能以数字打头
# 3.变量名中不能含空格，但可以用下划线代替空格 4.不能将python关键字和函数名用作变量名
# 5.变量名应简短又具有描述性，例如name比n好，student_name比s_n好，name_length比length_of_person_name好
# 6.慎用小写字母l和大写字母O，因为他们可能会被看重错成数字1和0
import keyword
print(keyword.kwlist)
