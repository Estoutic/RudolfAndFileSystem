from main.sample.FileSystemElement import FileSystemElement


class FileReader:

    def __init__(self) -> None:
        super().__init__()
        self.input_data = []
        self.general_dir_name = ''
        self.system_elements = {}
        self.last_index_of_elements = 0

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

    def pretty_input_data(self):
        self.general_dir_name = self.input_data.pop(0)
        self.system_elements[self.general_dir_name[:-1]] = FileSystemElement(3, self.general_dir_name[:-1], None, 0)
        last_index_of_elements = int(self.input_data.pop(0))
        self.last_index_of_elements = last_index_of_elements
        for index in range(last_index_of_elements - 1, -1, -1):
            split_element = self.input_data[index].split()
            if split_element[0] == '0':
                file_system_el:FileSystemElement = FileSystemElement(split_element[0], split_element[1], split_element[2], 0)
            else:
                file_system_el:FileSystemElement = FileSystemElement(split_element[0], split_element[1], split_element[2], split_element[3])
            self.system_elements[split_element[1]] = file_system_el

    def get_commands(self):
        for index in range(self.last_index_of_elements + 1, len(self.input_data)):
            command_info = self.input_data[index].split()
            if command_info[0] == '0':
                print(self.system_elements.get(command_info[1]).size)
            elif command_info[0] == '1':
                file_info:FileSystemElement = self.system_elements.get(command_info[1])
                if file_info.parent is not None:
                    parent_of_file = file_info.parent
                    while parent_of_file is not None:
                        self.system_elements.get(parent_of_file).size -= int(file_info.size)
                        parent_of_file = self.system_elements.get(parent_of_file).parent
                new_dir = command_info[2]
                parent_of_file = file_info.parent
                self.system_elements.get(new_dir).childes.append(command_info[1])
                self.system_elements.get(new_dir).size += int(file_info.size)
                while parent_of_file is not None:
                    self.system_elements.get(parent_of_file).size += int(file_info.size)
                    parent_of_file = self.system_elements.get(parent_of_file).parent


        # for el in self.system_elements:
        #     print(f'name: {self.system_elements.get(el).name}\nsize: {self.system_elements.get(el).size}\n')