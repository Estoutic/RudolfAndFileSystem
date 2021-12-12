class FileSystemElement:
    def __init__(self, el_type, name, parent, size) -> None:
        super().__init__()
        self.type = el_type
        self.name = name
        self.parent = parent
        self.size = size
        self.children = []
