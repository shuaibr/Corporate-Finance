class Cashflow:
    def __init__(self, val, t, r):
        self.val = val
        self.t = t
        self.r = r
        self.PV = self.valAt(0)

    def valAt(self, time):
        return self.val*(1+self.r)**(time-self.t)


flows = [Cashflow(1000, 1, 0.05), Cashflow(1000, 2, 0.05)]
total = 0
for f in flows:
    total += f.PV
print(total)

total = [f.PV for f in flows]
print(total)
print(sum(total))

total = 0
for f in flows:
    total += f.valAt(3)
print(total)
total = [f.valAt(3) for f in flows]
print(total)
print(sum(total))
