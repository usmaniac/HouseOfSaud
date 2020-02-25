class Lineage:
    def __init__(self,name,sons,died, born = 0,mother="",king=False, description=""):
        self.name = name
        self.sons = sons
        self.born = born
        self.mother = mother
        self.deceased = died
        self.king = king
        self.description = description
