class FileReader:

    def __init__(self) -> None:
        super().__init__()
        self.input_data = []
        self.data_tuple = {}
        self.general_dir_name = ''

    def read_file(self):
        filepath = '/Users/estoutic/projects/RudolfAndFileSystem/resources/input_data'
        with open(filepath, "r") as f:
            for line in f:
                self.input_data.append(line)

    def pretty_input_data(self):
        self.general_dir_name = self.input_data.pop(0)
        for index in range(0,int(self.input_data.pop(0))):
            print(self.input_data[index])