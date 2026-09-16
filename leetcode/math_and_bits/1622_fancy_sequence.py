class Fancy:
    def __init__(self):
        self.MOD = 10**9 + 7
        self.vals = []
        self.a = 1
        self.b = 0

    def append(self, val: int) -> None:
        inv_a = pow(self.a, self.MOD - 2, self.MOD)
        x = (val - self.b) * inv_a % self.MOD
        self.vals.append(x)

    def addAll(self, inc: int) -> None:
        self.b = (self.b + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.a = (self.a * m) % self.MOD
        self.b = (self.b * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.vals):
            return -1
        return (self.a * self.vals[idx] + self.b) % self.MOD
