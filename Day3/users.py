#首先，创建一个待验证用户列表和
#一个用于存储已验证用户的空列表
unconfirmed_users = ['jack','bide','pake']
#unconfirmed_users:未经验证的
confirmed_users = []
#验证每个用户，直到没有未验证用户为止
#将每个经过验证的用户都在未验证用户列表中删除
#并返回给current_user这个变量，此处用到pop()方法
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f'Verifying user:{current_user.title()}')
    confirmed_users.append(current_user)
    #用append()方法向已验证用户列表添加用户
print('\nThe following users have been confirmed:')
#输出一段话，意思是：已确认以下用户
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
#用for循环遍历已验证用户列表中的每一个用户，并将他们逐一输出出来


