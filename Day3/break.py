#实时响应用户输入的退出机制
while True:
    cmd = input("请输入指令（q）退出:")
    if cmd == 'q':
        break
    print(f"执行：{cmd}")