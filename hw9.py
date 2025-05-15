class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def setXY(self, x, y):
        self.x, self.y = x, y

    def getXY(self):
        return (self.x, self.y)

    def show(self):
        print(f'({self.x}, {self.y})')

class Rectangle:
    def __init__(self, ltx=0, lty=0, rbx=0, rby=0):
        lt = Point()
        rb = Point()
        
        self.ltx = ltx
        self.lty = lty

        lt.setXY(self.ltx, self.lty)
        self.leftTop = lt.getXY()
        
        self.rbx = rbx
        self.rby = rby
        
        rb.setXY(self.rbx, self.rby)
        self.rightBottom = rb.getXY()
    
    def set(self, ltx, lty, rbx, rby):
        lt = Point()
        rb = Point()
        
        self.ltx = ltx
        self.lty = lty
        
        lt.setXY(self.ltx, self.lty)
        self.leftTop = lt.getXY()
        
        self.rbx = rbx
        self.rby = rby
        
        rb.setXY(self.rbx, self.rby)
        self.rightBottom = rb.getXY()

    def show(self):
        print(f'좌측 상단 꼭지점이 {self.leftTop}이고 ', end='')
        print(f'우측 하단 꼭지점이 {self.rightBottom}인 사각형입니다.', end='')

    def getWidth(self):
        return self.rbx - self.ltx

    def getHeight(self):
        return self.rby - self.lty

    def getArea(self):
        area = self.getWidth() * self.getHeight()
        return area

    def getPerimeter(self):
        peri = (2*self.getWidth()) + (2*self.getHeight())
        return peri

def test():
    r1 = Rectangle(5, 5, 20, 10)
    a = r1.getArea()
    p = r1.getPerimeter()

    r1.show()
    print(f'\n넓이는 {a}, 둘레는 {p}')

if __name__ == '__main__':
    test()
