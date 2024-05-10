import math

from shape.shape import Shape


class Triangle(Shape):
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

        self.set_inner_angles([(angle_A), (angle_B), (angle_C)])


class Isosceles(Triangle):
    # todo implement method to set Isoceles vertices correctly
    # todo implement method to set Isoceles edges correctly

    pass


class Equilateral(Triangle):
    # todo implement method to set Equilateral vertices correctly
    # todo implement method to set Equilateral edges correctly
    pass


class Scalene(Triangle):
    # todo implement method to set Scalene vertices correctly
    # todo implement method to set Scalene correctly
    pass


class TriRectangle(Triangle):
    # todo implement method to set TriRectangle vertices correctly
    # todo implement method to set TriRectangle edges correctly
    pass
