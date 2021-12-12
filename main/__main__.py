from main.file_reader.FileReader import FileReader

if __name__ == '__main__':
    file_reader = FileReader()
    file_reader.read_file()
    file_reader.create_system_entities()
    file_reader.update_elements_meta_info()
    file_reader.execute_commands()