import re

def NumberAddition(str):

    nums = re.findall('\d+',str)
    output = list(map(int, nums))
    return sum(output)

print(NumberAddition("75Number9"))
















