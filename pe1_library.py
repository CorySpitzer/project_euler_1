def find_sum(interval1 = 3, interval2 = 5, limit = 1000):
    # print('lib called')
    # finds the sum of the multiples of the intervals below the limit
    sum = 0
    for i in range(interval1, limit):
        if i % interval1 == 0 or i % interval2 == 0:
            sum += i
    return sum

class Multiples:
    def __init__(self, interval1, interval2, limit):
        self.interval1 = interval1
        self.interval2 = interval2
        self.limit = limit
        self.total = 0

    def sum(self):
        for i in range(self.interval1, self.limit):
            if i % self.interval1 == 0 or i % self.interval2 == 0:
                self.total += i
        return self.total
