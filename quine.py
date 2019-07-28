s = [ 'print("s = [", repr(s[0]))',
'print("s = [", repr(s[0]))',
'for i in range(0, len(s)):',
'    if not i == 0:',
'       print(repr(s[i]))',
'    if i == len(s):',
'       print(repr(s[i]) = "]")',
'for i in range(0, len(s)):',
'    if not i == 0:',
'       print(s[i])',
'    if i == len(s):',
'       print(s[i])']
print("s = [", repr(s[0]))
for i in range(0, len(s)):
    if not i == 0:
        print(repr(s[i]))
    if i == len(s):
        print(repr(s[i]) + "]")
for i in range(0, len(s)):
    if not i == 0:
        print(s[i])
    if i == len(s):
        print(s[i])