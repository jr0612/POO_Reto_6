from shape.shape import Shape


class Rectangle(Shape):
    def compute_area(self):
        return self.get_edges()[0].get_length() * self.get_edges()[1].get_length()

    def compute_perimeter(self):
        return 2 * (self.get_edges()[0].get_length() + self.get_edges()[1].get_length())

    def compute_inner_angles(self):
        self.set_inner_angles([90, 90, 90, 90])


class Square(Rectangle):
    pass

