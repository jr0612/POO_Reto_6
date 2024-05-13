import math

from shape.shape import Shape, Point, Line


class Triangle(Shape):
    def __init__(self):
        self.frec = {}

    def compute_area(self):
        # Heron's formula is used
        edge_a = self.get_edges()[0].get_length()
        edge_b = self.get_edges()[1].get_length()
        edge_c = self.get_edges()[2].get_length()

        semiperimeter = (edge_a + edge_b + edge_c) / 2  # semiperimeter
        return round(
            math.sqrt(
                semiperimeter
                * (semiperimeter - edge_a)
                * (semiperimeter - edge_b)
                * (semiperimeter - edge_c)
            ),
            2,
        )

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self.get_edges())

    def compute_inner_angles(self):
        edge_a = self.get_edges()[0].get_length()
        edge_b = self.get_edges()[1].get_length()
        edge_c = self.get_edges()[2].get_length()

        angle_A = math.degrees(
            math.acos((edge_b**2 + edge_c**2 - edge_a**2) /
                      (2 * edge_b * edge_c))
        )
        angle_B = math.degrees(
            math.acos((edge_c**2 + edge_a**2 - edge_b**2) /
                      (2 * edge_c * edge_a))
        )
        angle_C = 180 - angle_A - angle_B

        self.set_inner_angles([round(angle_A), round(angle_B), round(angle_C)])

    # todo implement method to set Triangle vertices correctly
    def create_vertices(self, vertices: list):
        if len(vertices) != 3:
            raise ValueError(
                "Triangle must have 3 vertices"
                # ! raise error if vertices are not 3
            )
        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError(
                "Triangle vertices must be Point objects"
                # ! raise error if vertices are not Point objects
            )
        side_lengths = [
            vertices[0].compute_distance(vertices[1]),
            vertices[1].compute_distance(vertices[2]),
            vertices[2].compute_distance(vertices[0]),
        ]
        for side_length in side_lengths:
            if (side_length) not in self.frec:
                self.frec[side_length] = 1
            else:
                self.frec[side_length] += 1

    # todo implement method to set Triangle edges correctly
    def create_edges(self, edges: list):
        if len(edges) != 3:
            raise ValueError(
                "Triangle must have 3 edges"
                # ! raise error if edges are not 3
            )
        if not all(isinstance(edge, Line) for edge in edges):
            raise TypeError(
                "Triangle edges must be Line objects"
                # ! raise error if edges are not Line objects
            )
        if self.get_vertices():
            self.set_edges(edges)
        else:
            raise ValueError(
                "Triangle edges are not correct"
                # raise error if edges are not correct
            )


class Isosceles(Triangle):
    # todo implement method to set Isoceles vertices correctly
    def create_vertices(self, vertices: list):
        super().create_vertices(vertices)
        if any(count == 2 for count in self.frec.values()):
            self.set_vertices(vertices)
            return True
        else:
            raise ValueError("Isosceles must have 2 equal sides")


class Equilateral(Triangle):
    # todo implement method to set Equilateral vertices correctly
    def create_vertices(self, vertices: list):
        super().create_vertices(vertices)
        if all(count == 3 for count in self.frec.values()):
            self.set_vertices(vertices)
            return True
        else:
            raise ValueError("Equilateral must have 3 equal sides")


class Scalene(Triangle):
    # todo implement method to set Scalene vertices correctly
    def create_vertices(self, vertices: list):
        super().create_vertices(vertices)
        if all(count == 1 for count in self.frec.values()):
            self.set_vertices(vertices)
            return True
        else:
            raise ValueError("Scalene must have 3 unequal sides")


class TriRectangle(Triangle):
    def create_tri_rectangle(
        self,
    ):
        if any(inner_angle == 90 for inner_angle in self.get_inner_angles()):
            return True
        else:
            raise ValueError("TriRectangle must have a 90 degree inner angle")
