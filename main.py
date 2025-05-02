import csv
import math
import unittest


def calculate_circle_area(radius):
    return math.pi * radius**2


def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius


def calculate_rectangle_area(width, height):
    return width * height


def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)


def calculate_square_area(side):
    return side**2


def calculate_square_perimeter(side):
    return 4 * side


def calculate_triangle_area(side):
    return (math.sqrt(3) / 4) * side**2


def calculate_triangle_perimeter(side):
    return 3 * side


def process_csv(filename):
    results = []
    try:
        with open(filename, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                shape_type = row["type"].strip().lower()
                param1 = float(row["param1"]) if row["param1"] else None
                param2 = float(row["param2"]) if row["param2"] else None

                if shape_type == "circle" and param1:
                    area = calculate_circle_area(param1)
                    perimeter = calculate_circle_perimeter(param1)
                elif shape_type == "rectangle" and param1 and param2:
                    area = calculate_rectangle_area(param1, param2)
                    perimeter = calculate_rectangle_perimeter(param1, param2)
                elif shape_type == "square" and param1:
                    area = calculate_square_area(param1)
                    perimeter = calculate_square_perimeter(param1)
                elif shape_type == "triangle" and param1:
                    area = calculate_triangle_area(param1)
                    perimeter = calculate_triangle_perimeter(param1)
                else:
                    continue

                results.append((shape_type, area, perimeter))
    except Exception as e:
        print(f"Помилка при обробці файлу: {e}")
    return results


class TestGeometryFunctions(unittest.TestCase):
    def test_circle(self):
        self.assertAlmostEqual(calculate_circle_area(10), math.pi * 100)
        self.assertAlmostEqual(calculate_circle_perimeter(10), 2 * math.pi * 10)

    def test_rectangle(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)
        self.assertEqual(calculate_rectangle_perimeter(5, 10), 30)

    def test_square(self):
        self.assertEqual(calculate_square_area(4), 16)
        self.assertEqual(calculate_square_perimeter(4), 16)

    def test_triangle(self):
        self.assertAlmostEqual(calculate_triangle_area(6), (math.sqrt(3) / 4) * 36)
        self.assertEqual(calculate_triangle_perimeter(6), 18)


if __name__ == "main":
    filename = "shapes.csv"
    results = process_csv(filename)

    for shape, area, perimeter in results:
        print(f"{shape.capitalize()}: Площа = {area:.2f}, Периметр = {perimeter:.2f}")

    unittest.main()
