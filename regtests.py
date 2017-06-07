import re
line = input()
def dateinput(line):

    p = re.compile(r"[0-3][0-9]\.[01][0-9]\.[2][0][01][0-9]$")
    if p.search(line):
        print("ok")
    else:
        print("no!")


dateinput(line)