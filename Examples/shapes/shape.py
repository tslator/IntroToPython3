import math


class IsoscelesError(Exception):
    pass


class RightTriangleError(Exception):
    pass


class ParallelogramError(Exception):
    pass


class SquareError(Exception):
    pass


class TrapezoidError(Exception):
    pass


class RectangleError(Exception):
    pass


class Plane:
    '''
    A surface containing all the straight lines that connect any two points on it.
    '''

    def __str__(self):
        return "Sides: {0}, Angles: {1}".format(", ".join(map(str, self._sides)), ", ".join(map(str, self._angles)))

    def __init__(self, sides, angles):
        self._sides = sides
        self._angles = angles

    def GetSides(self):
        return self._sides

    def GetAngles(self):
        return self._angles


class Polygon(Plane):
    '''
    A closed plane figure bounded by three or more line segments.
    '''
    def __str__(self):
        return "Polygon -> " + Plane.__str__(self)

    def __init__(self, sides, angles):
        Plane.__init__(self, sides, angles)

    def GetNumSides(self):
        return len(self._sides)

    def GetNumAngles(self):
        return len(self._angles)

    def Perimeter(self):
        return sum(self._sides)


class Triangle(Polygon):
    '''
    A closed plane figure formed by connecting three points not in a straight line by straight line segments
    '''
    def __str__(self):
        return "Triangle -> " + Polygon.__str__(self)

    def __init__(self, sides, angles):
        Polygon.__init__(self, sides, angles)

    def Area(self):
        '''
        Heron's Formula for the area of any triangle:

        Given the lengths a, b and c of the sides of a triangle, the area A of the triangle is:

            A = sqrt(s(s-a)(s-b)(s-c))

        where the value s is the semi-perimeter of the triangle. In other words,
            s = (a + b + c)/2
        '''
        s = sum(self._sides) / 2
        a, b, c = self._sides
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class IsoscelesTriangle(Triangle):
    '''
    A triangle with two equal sides
    '''
    def __str__(self):
        return "IsoscelesTriangle -> " + Triangle.__str__(self)

    def __init__(self, sides, angles):
        Triangle.__init__(self, sides, angles)
        if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
            raise IsoscelesError


class RightTriangle(Triangle):
    '''
    A triangle one angle of which is a right angle
    '''
    def __str__(self):
        return "RightTriangle -> " + Triangle.__str__(self)

    def __init__(self, sides, angles):
        Triangle.__init__(self, sides, angles)
        if angles[0] != 90 and angles[1] != 90 and angles[2] != 90:
            raise RightTriangleError


class EquilateralTriangle(IsoscelesTriangle):
    '''
    A triangle with all sides and all angles equal
    '''
    def __str__(self):
        return "EquilateralTriangle -> " + IsoscelesTriangle.__str__(self)

    def __init__(self, side):
        IsoscelesTriangle.__init__(self, [side] * 3, [60] * 3)


class IsoscelesRightTriangle(IsoscelesTriangle, RightTriangle):
    '''
    A right triangle with the two legs (and their corresponding angles) equal
    '''
    def __str__(self):
        return "IsoscelesRightTriangle -> " + IsoscelesTriangle.__str__(self) + ", IsoscelesRightTriangle -> " + RightTriangle.__str__(self)

    def __init__(self, sides):
        IsoscelesTriangle.__init__(self, sides, [90, 45, 45])
        RightTriangle.__init__(self, sides, [90, 45, 45])


class Quadrangle(Polygon):
    '''
     A polygon with four sides and four vertices (also known as a Quadrilateral
    '''
    def __str__(self):
        return "Quadrangle -> " + Polygon.__str__(self)

    def __init__(self, sides, angles):
        Polygon.__init__(self, sides, angles)

    def Area(self):
        '''
        Bretschneider's Formula

        A = sqrt((s-a)(s-b)(s-c)(s-d) - abcdcos((A+B)/2)^2), where
        s = (a + b + c + d)/2
        A and B are opposite angles
        '''
        s = sum(self._sides) / 2
        a, b, c, d = self._sides
        sum_opp_angles = math.radians((self._angles[0] + self._angles[1]))
        cos_opp_angles_squared = math.pow(math.cos(sum_opp_angles / 2), 2)
        return math.sqrt((s - a) * (s - b) * (s - c) * (s - d) - a * b * c * d * cos_opp_angles_squared)


class Parallelogram(Quadrangle):
    '''
    A quadrilateral with opposite sides parallel (and therefore opposite angles equal)
    '''
    def __str__(self):
        return "Parallelogram -> " + Quadrangle.__str__(self)

    def __init__(self, sides, angles):
        Quadrangle.__init__(self, sides, angles)
        if angles[0] != angles[2] or angles[1] != angles[3]:
            raise ParallelogramError


class Rectangle(Parallelogram):
    '''
    A parallelogram with four right angles
    '''
    def __str__(self):
        return "Rectangle -> " + Parallelogram.__str__(self)

    def __init__(self, sides):
        Parallelogram.__init__(self, sides, [90] * 4)
        if sides[0] != sides[2] or sides[1] != sides[3]:
            raise RectangleError


class Square(Rectangle):
    '''
    A rectangle with all sides equal
    '''
    def __str__(self):
        return "Square -> " + Rectangle.__str__(self)

    def __init__(self, sides):
        Rectangle.__init__(self, sides)
        if sides[0] != sides[1] != sides[2] != sides[3]:
            raise SquareError


class Trapezoid(Quadrangle):
    '''
    A quadrilateral with two sides (one pair) parallel
    '''
    def __str__(self):
        return "Trapezoid -> " + Quadrangle.__str__(self)

    def __init__(self, sides, angles):
        Quadrangle.__init__(self, sides, angles)
        if angles[0] != angles[2] and angles[1] != angles[3]:
            raise TrapezoidError


def main():
    rect = Rectangle([4, 5, 4, 5])
    print(rect)
    print(rect.Perimeter())
    print(rect.Area())
    tri = Triangle([3, 4, 5], [30, 60, 90])
    print(tri)
    print(tri.Perimeter())
    print(tri.Area())

    irt = IsoscelesRightTriangle([4, 4, 7])
    print(irt)

    square = Square([10, 10, 10, 10])


if __name__ == "__main__":
    main()
