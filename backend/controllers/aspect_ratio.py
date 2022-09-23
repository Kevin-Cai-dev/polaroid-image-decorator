class AspectRatio:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_portrait(self):
        return (min(self.width, self.height), max(self.width, self.height))

    def get_landscape(self):
        return (max(self.width, self.height), min(self.width, self.height))
