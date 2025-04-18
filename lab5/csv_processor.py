import csv
from shape_factory import ShapeFactory
from shape import Shape
from solid_shape import SolidShape

class CSVProcessor:
    @staticmethod
    def process_csv(filename):
        shapes = []
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                shape_type = row['type'].strip().lower()
                params = [float(row[key]) for key in row if key != 'type' and row.get(key) and row[key].strip()]

                shape = ShapeFactory.create_shape(shape_type, params)
                
                if shape:
                    result = {
                        'type': shape_type.capitalize(),
                        'params': params,
                        'area': shape.area(),
                        'perimeter': shape.perimeter() if isinstance(shape, Shape) else 'N/A',
                        'volume': shape.volume() if isinstance(shape, SolidShape) else 'N/A'
                    }
                    shapes.append(result)
        return shapes
