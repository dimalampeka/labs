class ResultPrinter:
    @staticmethod
    def print_results(shapes):
        print("\nРезультати обчислень:")
        for shape in shapes:
            print(f"Фігура: {shape['type']}, Параметри: {shape['params']}, "
                  f"Площа: {shape['area']:.2f}, Периметр: {shape['perimeter']}, "
                  f"Об'єм: {shape['volume']}")
