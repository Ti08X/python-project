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