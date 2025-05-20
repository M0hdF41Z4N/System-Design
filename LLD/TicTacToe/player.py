class Player:
    def __init__(self, name, piece=None):
        self.name = name
        self.piece = piece

    def getName(self):
        return self.name

    def getPlayingPiece(self):
        return self.piece

    def setPlayingPiece(self, piece):
        self.piece = piece

    def setName(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.piece})"
