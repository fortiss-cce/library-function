class Publisher:
    name: str

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Publisher):
            return self.name == other.name
        return NotImplemented
