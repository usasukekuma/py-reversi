def p():
    s = [(8,8)]
    return s
n = [8]
x = 9
print(set([(8,7)]) & set(p()))
if not list(set([(9,8)]) & set(p())) == []:
    print('OK')
else:
    print('ERROR')