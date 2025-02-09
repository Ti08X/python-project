cars = ['audi','bmw','subaru','toyota'] #创建列表cars
for car in cars:  #用for遍历cars中的元素，其中car代表遍历到的具体元素
    if car == 'bmw':  #if条件判断，如果是bmw就转大写后输出，如果不是就首字母转大写后输出
        print(car.upper())
    else:
        print(car.title())
 