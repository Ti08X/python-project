year = int(input('请输入年份：'))
#通过input()获取用户输入并转换为int类型，最后把这个int型的数字赋给year
is_leap = (year % 4 == 0 and year % 100 != 0)or(year % 400 == 0)
#leap year是闰年，闰年的判断有两种，满足其一即为闰年
#1.能被4整除不能被100整除 2.能被400整除
print(f"{year}是闰年"if is_leap else f'{year}年不是闰年')
#这里实际运用了python中的三元运算符，它的结构类似
#max=a if a>b else b;  这个语句中如果a>b为True则返回if前面的语句，如果为False则返回else后的语句