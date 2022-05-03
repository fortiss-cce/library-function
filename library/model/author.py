class Author:

    firstname: str
    lastname: str

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname

    def get_firstname(self) -> str:
        return self.firstname

    def get_lastname(self) -> str:
        return self.lastname

    def get_fullname(self) -> str:
        return f"{self.firstname} {self.lastname}"

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Author):
            return self.get_fullname() == other.get_fullname()
        return NotImplemented
