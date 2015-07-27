def find_sum(interval1 = 3, interval2 = 5, limit = 1000):
    # print('lib called')
    # finds the sum of the multiples of the intervals below the limit
    sum = 0
    for i in range(interval1, limit):
        if i % interval1 == 0 or i % interval2 == 0:
            sum += i
    return sum
