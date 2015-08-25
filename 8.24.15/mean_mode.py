import statistics

def MeanMode(arr):

    mode = statistics.mode(arr)
    mean = statistics.mean(arr)

    if mean == mode:
        return 1
    else:
        return 0

zero = [1, 1, 2, 3]
one = [4, 4, 4, 6, 2]

# keep this function call here
# to see how to enter arguments in Python scroll down
print(MeanMode(one))
print(MeanMode(zero))
