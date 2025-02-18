score = int(input('请输入成绩：'))  #获取用户输入
if score >= 90:   #条件判断语句成绩大于等于90时把字符串'A'赋给grade
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

if grade != 'F':   #条件判断语句筛选出大于60的情况则继续执行下面的语句
    last_digit = score % 10   #last：最近的；digit：字符 
                              #将score除以10取余数，将这个余数赋给变量last_digit
    if last_digit >= 7:   #条件判断语句当last_digit大于等于7时，0211
        grade += "+"
    elif last_digit <= 3:
        grade += "-"

print(f"成绩等级：{grade}")
