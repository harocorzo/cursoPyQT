#coding=utf-8
import math

## Parte 0
## Temas:
# - Basics de objetos:
#     - Métodos y atributos
# - Constructores
# - Métodos mágicos
# - Herencia
# - Miembros estáticos

class Point2D:
    # Constructor
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def dist(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    # Operator less than
    def __lt__(self, other):
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    # Magic Method to print
    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

class Polygon:
    # Constructor
    def __init__(self, num_vertex, vertex_list):
        self.n = num_vertex
        self.vertex = sorted(vertex_list)
        print(f"Polygon created with {self.n} vertex")

    # Magic method
    def __repr__(self):
        return f"Polygon({self.vertex})"


# SubClass of Polygon
class Square(Polygon):
    # Static attribute
    className = "Polygon Square"

    # Constructor
    def __init__(self, vertex_list):
        super().__init__(4, vertex_list)

    # Method override
    def getArea(self):
        return self.vertex[0].dist(self.vertex[1])**2

    @staticmethod
    def unitSquare():
        return Square([Point2D(0, 0), Point2D(1, 0), Point2D(0, 1), Point2D(1, 1)])


if __name__ == "__main__":
    S = Square.unitSquare()
    print(S.className)
    print(S)
    print(S.getArea())
    print(isinstance(S, Square))
    print(isinstance(S, Polygon))
