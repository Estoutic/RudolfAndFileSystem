class FileSystemElement:
    def __init__(self, type_of_element, name_of_element, parent, size) -> None:
        super().__init__()
        self.type = type_of_element
        self.name = name_of_element
        self.parent = parent
        self.size = size
        self.childes = []
