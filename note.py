class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def to_str(self):
        return f"{self.title}|{self.content}"

    @staticmethod
    def from_str(data):
        title, content = data.split('|', 1)
        return Note(title, content)
