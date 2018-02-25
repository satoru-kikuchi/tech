import string

s = """\

Hi $name

$contents

Have a good day
"""

t = string.Template(s)
print(t.substitute(name='Mike', contents='How'))
