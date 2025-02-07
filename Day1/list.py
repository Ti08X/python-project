# 列表创建与操作
fruits = ["apple", "banana", "orange"]  #索引访问(正向从0开始，反向从-1开始)⭐
print(fruits[0])
fruits[0] = 'grape' #修改元素⭐
print(fruits[0])
fruits.append('peach') #添加元素⭐⭐
print(fruits[0:])
fruits.pop() #删除末尾元素⭐
print(fruits[0:])

'''
print(fruits[0])       # 索引访问（正向从0开始） ⭐⭐
fruits[1] = "grape"    # 修改元素 ⭐
fruits.append("peach") # 添加元素 ⭐⭐
fruits.pop()           # 删除末尾元素 ⭐
'''