class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.s = "Not right"
        if hyp**2 == leg_1**2 + leg_2**2:
            self.s = 1/2 * leg_1 * leg_2


num = list(map(int,input().split()))
tri = RightTriangle(num[0], num[1], num[2])
print(tri.s)