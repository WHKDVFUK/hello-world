squares=[]
'''计算范围内数字的运算并把结果打出列表'''
for value in range(0,11):
    square=value**2
    squares.append(square)
print(squares)


favorite_color = {
    'wk':'pink',
    'ck':'green',
    'gg':'apple',
    'ff':'red',
    'ee':'blue',
    }
for name, color in favorite_color.items():#遍历字典所有的 键-值 
    print(name.title()+"'s favorite color is"+color+'.')

    
favorite_color = {
    'wk':'pink',
    'ck':'green',
    'gg':'apple',
    'ff':'red',
    'ee':'blue',
    }
for name in favorite_color.keys():#这一步是提取字典中的键并返回成列表
    print(name)
