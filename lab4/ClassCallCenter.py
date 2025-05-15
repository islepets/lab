import csv
import os

class Call:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{self.key}: {self.value}"

    def __setattr__(self, key, value):
        if key in ['key', 'value']:
            object.__setattr__(self, key, value)
        else:
            raise AttributeError("Ошибка записи значений в свойства")


class CallCenter:
    def __init__(self):
        self.calls = {}

    def __iter__(self):
        return iter(self.calls.values())

    def __getitem__(self, item):
        return self.calls[item]

    def __setitem__(self, key, value):
        self.calls[key] = value

    def __repr__(self):
        return f"CallCenter with {len(self.calls)} calls"

    @staticmethod
    def count_files(directory):
        count = sum(os.path.isfile(os.path.join(directory, el)) for el in os.listdir(directory))
        return count

    @staticmethod
    def load_calls_from_csv(file_path):
        call_center = CallCenter()
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) > 3:
                        key = row[0]
                        value = row[1:]
                        call_center[key] = Call(key, value)
        except FileNotFoundError:
            print('Файл не найден')
        return call_center

    def sort_ch(self):
        sorted_by_ch = dict(sorted(self.calls.items(), key=lambda item: item[1].value[0], reverse=True))
        return sorted_by_ch

    def sort_str(self):
        sorted_by_str = dict(sorted(self.calls.items(), key=lambda item: item[1].value[1]))
        return sorted_by_str

    def sort_param(self, param):
        sorted_by_param = {k: v for k, v in self.calls.items() if v.value[2] == param}
        return sorted_by_param