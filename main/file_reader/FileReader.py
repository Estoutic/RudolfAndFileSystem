from main.sample.FileSystem import FileSystemElement


class FileReader:

    def __init__(self) -> None:
        super().__init__()
        self.input_data = []
        self.general_dir_name = ''
        self.system_elements = {}

    def read_file(self):
        filepath = '/Users/estoutic/projects/RudolfAndFileSystem/resources/input_data'
        with open(filepath, "r") as f:
            for line in f:
                self.input_data.append(line)

    def get_info(self):
        for element in self.system_elements:
            if self.system_elements.get(element).parent is not None:
                file_system_element:FileSystemElement = self.system_elements.get(self.system_elements.get(element).parent)
                file_system_element.size += int(self.system_elements.get(element).size)
                file_system_element.childes.append(element)
        print(self.system_elements)

    def pretty_input_data(self):
        self.general_dir_name = self.input_data.pop(0)
        self.system_elements[self.general_dir_name[:-1]] = FileSystemElement(3, self.general_dir_name[:-1], None, 0)
        for index in range(int(self.input_data.pop(0)) - 1, -1, -1):
            split_element = self.input_data[index].split()
            if split_element[0] == '0':
                file_system_el:FileSystemElement = FileSystemElement(split_element[0], split_element[1], split_element[2], 0)
            else:
                file_system_el:FileSystemElement = FileSystemElement(split_element[0], split_element[1], split_element[2], split_element[3])
            self.system_elements[split_element[1]] = file_system_el

    def get_commands(self):
        for el in self.system_elements:
            print(f'name: {self.system_elements.get(el).name}\nsize: {self.system_elements.get(el).size}\n')