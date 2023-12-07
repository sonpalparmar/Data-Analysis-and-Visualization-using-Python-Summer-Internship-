class area:
    def check_triangle(a, b, c):
        if (a+b <= c or c+b <= a or c+a <= b):
            return False
        else:
            return True

    def cal(a, b=None, c=None, d=None):
        if (b == c == d == None):
            return 3.14*(a**2)
        elif (d == None and a != None and b != None and c != None):
            if (area.check_triangle(a,b,c)):
                p = (a+b+c)/2
                return format(((p*(p-a)*(p-b)*(p-c))**0.5),'.2f')
        else:
            if (a == b == c == d == a):
                return a*a
            elif ((a == b and c == d) or (a == c and b == d)):
                return a*d
            elif ((b == c or d == a)):
                return a*b
            elif (c == d == None):
                return a*b

print(area.cal(10))
print(area.cal(1, 30))
print(area.cal(6, 5, 3))
print(area.cal(1, 2, 2, 1))
print(area.cal(1, 1, 1, 1))
