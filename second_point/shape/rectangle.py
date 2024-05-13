from shape.shape import Line, Point, Shape


class Rectangle(Shape):
    def compute_area(self):
        return self.get_edges()[0].get_length() * self.get_edges()[1].get_length()

    def compute_perimeter(self):
        return 2 * (self.get_edges()[0].get_length() + self.get_edges()[1].get_length())

    def compute_inner_angles(self):
        self.set_inner_angles([90, 90, 90, 90])

    # todo implement method to set Rectangle vertices correctly
    def create_vertices(self, vertices: list):
        if len(vertices) != 4:
            raise ValueError(
                "Rectangle must have 4 vertices"
            )  # ! raise error if vertices are not 4

        if not all(isinstance(vertex, Point) for vertex in vertices):
            raise TypeError(
                "Rectangle vertices must be Point objects"
                # ! raise error if vertices are not Point objects
            )

        if (
            vertices[0].get_x() == vertices[3].get_x()
            and vertices[0].get_y() == vertices[1].get_y()
            and vertices[1].get_x() == vertices[2].get_x()
            and vertices[2].get_y() == vertices[3].get_y()
        ):
            self.set_vertices(vertices)  # set vertices
        else:
            raise ValueError(
                "Rectangle vertices are not correct"
            )  # raise error if vertices are not correct

    # todo implement method to set Rectangle edges correctly
    def create_edges(self, edges: list):
        if len(edges) != 4:
            raise ValueError(
                "Rectangle must have 4 edges"
            )  # ! raise error if edges are not 4
        if not all(isinstance(edge, Line) for edge in edges):
            raise TypeError(
                "Rectangle edges must be Line objects"
                # ! raise error if edges are not Line objects
            )
        if (
            edges[0].get_length() == edges[2].get_length()
            and edges[1].get_length() == edges[3].get_length()
        ):
            self.set_edges(edges)  # set edges
        else:
            raise ValueError(
                "Rectangle edges are not correct"
            )  # raise error if edges are not correct


class Square(Rectangle):
    # todo implement method to set Square vertices correctly
    def create_vertices(self, vertices: list):
        super().create_vertices(vertices)

    def create_edges(self, edges: list):
        super().create_edges(edges)
        if (
            self.get_edges()[0].get_length()
            == self.get_edges()[1].get_length()
            == self.get_edges()[2].get_length()
            == self.get_edges()[3].get_length()
        ):
            self.set_edges(edges)

        else:
            raise ValueError("Square edges are not correct")
