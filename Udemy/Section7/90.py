s = """\
AAA
BBB
CCC
DDD
"""

with open('test.txt', 'w+') as f:
    f.seek(0)
    print(f.read())
    f.write(s)
    