class Remocon:
    def __init__(self):
        self.buttons = list(range(10))

    def distroy(self, b):
        self.buttons.remove(b)

    def __getitem__(self, n):
        l = len(self.buttons)
        result, digit = 0, 1
        while n >= l:
            result += self.buttons[n % l] * digit
            n //= l
            if self.buttons[0]:
                n -= 1
            digit *= 10
        result += self.buttons[n % l] * digit
        return result

    def least_button_push(self, target):
        if not self.buttons:
            result = float('inf')
        elif self.buttons == [0, ]:
            result = target + 1
        elif self[0] > target:
            result = self[0] - target + 1
        else:
            lo, hi = 0, 10
            while self[hi] <= target:
                hi *= 10
            while hi - lo > 1:
                m = (lo + hi) // 2
                if self[m] < target:
                    lo = m
                else:
                    hi = m
            lower, higher = self[lo], self[hi]
            result = min(len(str(lower)) + abs(lower - target),
                         len(str(higher)) + abs(higher - target))
        return min(result, abs(target - 100))


remocon = Remocon()
target = int(input())
if int(input()):
    for button in map(int, input().split()):
        remocon.distroy(button)
print(remocon.least_button_push(target))