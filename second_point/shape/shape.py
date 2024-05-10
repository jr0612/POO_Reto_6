class Point:
    definition: str = (
        "Entidad geometrica abstracta que representa una ubicación en un espacio."
    )

    def __init__(self, x: float = 0, y: float = 0):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def set_x(self, x: float):
        self._x = x

    def set_y(self, y: float):
        self._y = y

    def compute_distance(self, point) -> float:
        distance = ((self._x - point._x) ** 2 +
                    (self._y - point._y) ** 2) ** 0.5
        return distance


class Line:
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end
        self._length = start.compute_distance(end)

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def get_length(self):
        return self._length

    def set_start(self, start: Point):
        self._start = start

    def set_end(self, end: Point):
        self._end = end

    def compute_length(self):
        return self._start.compute_distance(self._end)


class Shape:
    def __init__(self) -> None:
        self.__is_regular = False
        self.__vertices = [Point]
        self.__edges = [Line]
        self.__inner_angles = [float]

    def get_vertices(self):
        return self.__vertices

    def get_edges(self):
        return self.__edges

    def get_inner_angles(self):
        return self.__inner_angles

    def get_is_regular(self):
        return self.__is_regular

    def set_vertices(self, vertices: list):
        self.__vertices = vertices

    def set_edges(self, edges):
        self.__edges = edges

    def set_inner_angles(self, inner_angles):
        self.__inner_angles = inner_angles

    def set_is_regular(self, is_regular: bool):
        self.__is_regular = is_regular

    def compute_area(self):
        raise NotImplementedError("Subclass should implement compute_area()")

    def compute_perimeter(self):
        raise NotImplementedError(
            "Subclass should implement compute_perimeter()")

    def compute_inner_angles(self):
        raise NotImplementedError(
            "Subclass should implement compute_inner_angles()")

    def create_vertices(self, vertices: list):
        """
        veryfiy if the vertices are valid
        """
        raise NotImplementedError(
            "Subclass should implement create_vertices()")

    def create_edges(self, vertices: list):
        """
        create edges if the vertices are valid
        """
        raise NotImplementedError("Subclass should implement create_edges()")
