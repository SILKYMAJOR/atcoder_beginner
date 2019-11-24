class OrgTime:
    def __init__(self, hour=0, minute=0, second=0):
        self.second = second
        self.minute = minute
        self.hour = hour

    def print_time(self):
        print("{:02}:{:02}:{:02}".format(self.hour, self.minute, self.second))

    def plus_arg_second(self, diff_second):
        self.second += diff_second
        self.check()

    def check(self):
        self.minute += self.second // 60
        self.hour += self.minute // 60

        self.second = self.second % 60

        if self.second < 0:
            self.second += 60

        self.minute = self.minute % 60
        if self.minute < 0:
            self.minute += 60

        self.hour = self.hour % 24
        if self.hour < 0:
            self.hour += 24


def main():
    hour, minute, second = map(int, input().split())
    diff_second = int(input())

    time = OrgTime(hour=hour, minute=minute, second=second)
    time.print_time()
    time.plus_arg_second(diff_second)
    time.print_time()


if __name__ == '__main__':
    main()

