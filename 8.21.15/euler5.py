#submitted on hackerrank, handles 3 of 5 test cases

import fileinput
for line in fileinput.input():
    if not fileinput.isfirstline():
        inpu = int(line)
        up = int(inpu + inpu)
        down = int(inpu)
        while down >= 0:
            if down==0:
                break
            elif up%down!=0:
                up = up + inpu
                down = inpu
                continue
            elif down==1:
                print(up)
            down = down - 1


        