from csv_processor import CSVProcessor
from result_printer import ResultPrinter

if __name__ == "__main__":
    filename = "shapes.csv"
    shapes = CSVProcessor.process_csv(filename)
    ResultPrinter.print_results(shapes)
