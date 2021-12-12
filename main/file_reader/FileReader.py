from main.sample.FileSystemElement import FileSystemElement


class FileReader:

    def __init__(self) -> None:
        super().__init__()
        self.input_data = []
        self.system_elements = {}

    def read_file(self):
        filepath = '/Users/estoutic/projects/RudolfAndFileSystem/resources/input_data'
        with open(filepath, "r") as f:
            for line in f:
                self.input_data.append(line)

    def update_elements_meta_info(self):
        for element in self.system_elements:
            if self.system_elements.get(element).parent is not None:
                file_system_element: FileSystemElement = self.system_elements.get(self.system_elements.get(element).parent)
                file_system_element.size += int(self.system_elements.get(element).size)
                file_system_element.children.append(element)

    def create_system_entities(self):
        root = self.input_data.pop(0)[:-1]
        self.system_elements[root] = FileSystemElement(3, root, None, 0)

        elements_count = int(self.input_data.pop(0))

        for index in range(elements_count - 1, -1, -1):  # count/limit/step
            split_element = self.input_data[index].split()
            el_name = split_element[1]
            el_type = split_element[0]
            el_parent_name = split_element[2]

            if el_type == '0':
                file_system_el: FileSystemElement = FileSystemElement(el_type, el_name, el_parent_name, 0)
            else:
                el_size = split_element[3]
                file_system_el: FileSystemElement = FileSystemElement(el_type, el_name, el_parent_name, el_size)

            self.system_elements[el_name] = file_system_el

    def execute_commands(self):
        for index in range(len(self.system_elements), len(self.input_data)):
            command_info = self.input_data[index].split()
            arg1 = command_info[1]
            command = command_info[0]
            if command == '0':
                print(self.system_elements.get(arg1).size)
            elif command == '1':
                file_info: FileSystemElement = self.system_elements.get(arg1)
                if file_info.parent is not None:
                    parent_of_file = file_info.parent
                    while parent_of_file is not None:
                        self.system_elements.get(parent_of_file).size -= int(file_info.size)
                        parent_of_file = self.system_elements.get(parent_of_file).parent

                new_dir = command_info[2]
                parent_of_file = file_info.parent
                self.system_elements.get(new_dir).children.append(arg1)
                self.system_elements.get(new_dir).size += int(file_info.size)

                while parent_of_file is not None:
                    self.system_elements.get(parent_of_file).size += int(file_info.size)
                    parent_of_file = self.system_elements.get(parent_of_file).parent
