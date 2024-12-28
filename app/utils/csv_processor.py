import csv

class CSVProcessor:
    @staticmethod
    def read_csv(file_path):
        with open(file_path, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)

    @staticmethod
    def write_csv(file_path, data, fieldnames):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

    @staticmethod
    def append_csv(file_path, data, fieldnames):
        with open(file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writerows([data])