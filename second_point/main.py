import math

from shape.rectangle import Rectangle, Square
from shape.shape import Line, Point
from shape.triangle import Equilateral, Isosceles, Scalene, TriRectangle


def main():
    point_1 = Point(0, 0)
    point_2 = Point(3, 0)
    point_3 = Point(0, 4)

    line_1 = Line(point_1, point_2)
    line_2 = Line(point_2, point_3)
    line_3 = Line(point_3, point_1)

    # Crear un triángulo escaleno
    triangle_scalene = Scalene()
    triangle_scalene.set_vertices([point_1, point_2, point_3])
    triangle_scalene.set_edges([line_1, line_2, line_3])
    triangle_scalene.compute_inner_angles()

    # Crear un triángulo isósceles
    point_4 = Point(3, 4)
    line_4 = Line(point_2, point_4)
    triangle_isosceles = Isosceles()
    triangle_isosceles.set_vertices([point_1, point_2, point_4])
    triangle_isosceles.set_edges([line_1, line_4, line_3])
    triangle_isosceles.compute_inner_angles()

    # Crear triangulo equilatero
    point_1_equilateral = Point(-1, 0)
    point_2_equilateral = Point(1, 0)
    point_3_equilateral = Point(0, math.sqrt(3))  # Altura calculada

    line_1_equilateral = Line(point_1_equilateral, point_2_equilateral)
    line_2_equilateral = Line(point_2_equilateral, point_3_equilateral)
    line_3_equlateral = Line(point_3_equilateral, point_1_equilateral)

    equilateral_triangle = Equilateral()
    equilateral_triangle.set_vertices(
        [point_1_equilateral, point_2_equilateral, point_3_equilateral]
    )
    equilateral_triangle.set_edges(
        [line_1_equilateral, line_2_equilateral, line_3_equlateral]
    )
    equilateral_triangle.compute_inner_angles()

    # Crear un triángulo rectángulo
    point_6 = Point(3, 4)
    line_7 = Line(point_1, point_2)
    line_8 = Line(point_2, point_6)
    line_9 = Line(point_6, point_1)
    triangle_rect = TriRectangle()
    triangle_rect.set_vertices([point_1, point_2, point_6])
    triangle_rect.set_edges([line_7, line_8, line_9])
    triangle_rect.compute_inner_angles()

    # Crear un rectángulo
    point_1_rectangle = Point(0, 0)
    point_2_rectangle = Point(4, 0)
    point_3_rectangle = Point(4, 3)
    point_4_rectangle = Point(0, 3)

    line_1_rectangle = Line(point_1_rectangle, point_2_rectangle)
    line_2_rectangle = Line(point_2_rectangle, point_3_rectangle)
    line_3_rectangle = Line(point_3_rectangle, point_4_rectangle)
    line_4_rectangle = Line(point_4_rectangle, point_1_rectangle)

    rectangle = Rectangle()
    rectangle.set_vertices(
        [point_1_rectangle, point_2_rectangle,
            point_3_rectangle, point_4_rectangle]
    )
    rectangle.set_edges(
        [line_1_rectangle, line_2_rectangle, line_3_rectangle, line_4_rectangle]
    )
    rectangle.compute_inner_angles()

    # Crear un cuadrado

    point_1_square = Point(0, 0)
    point_2_square = Point(4, 0)
    point_3_square = Point(4, 4)
    point_4_square = Point(0, 4)
    line_1_square = Line(point_1_square, point_2_square)
    line_2_square = Line(point_2_square, point_3_square)
    line_3_square = Line(point_3_square, point_4_square)
    line_4_square = Line(point_4_square, point_1_square)

    square = Square()
    square.set_vertices(
        [point_1_square, point_2_square, point_3_square, point_4_square]
    )
    square.set_edges([line_1_square, line_2_square,
                     line_3_square, line_4_square])
    square.compute_inner_angles()

    # Calcular y mostrar información para cada forma
    for shape in [
        triangle_scalene,
        triangle_isosceles,
        equilateral_triangle,
        triangle_rect,
        rectangle,
        square,
    ]:
        print("\nShape:", shape.__class__.__name__)
        print("Vertices:")
        for vertex in shape.get_vertices():
            print("({}, {})".format(vertex.get_x(), vertex.get_y()))

        print("Edge lengths:")
        for edge in shape.get_edges():
            print(edge.get_length())

        print("Inner angles:")
        for angle in shape.get_inner_angles():
            print(angle)

        print("Area:", shape.compute_area())
        print("Perimeter:", shape.compute_perimeter())


if __name__ == "__main__":
    main()
