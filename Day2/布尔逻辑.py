#组合条件判断：掌握and和or
score = float(input('请输入分数(0-100):')) #score分数
attendance = float(input('请输入出勤(0-1):')) #attendance出勤
if score>=80 and attendance>=0.9:
    print('获得申请奖学金资格！')
if score<60 or attendance<0.8:
    print('将面临学业预警！！！')