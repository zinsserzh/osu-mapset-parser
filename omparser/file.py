import os

class File:
    def __init__(self, parser, rel_path):
        self.parser = parser
        self.rel_path = rel_path

    @property
    def mapset_directory(self):
        return self.parser.directory

    @property
    def abspath(self):
        return self.mapset_directory + self.rel_path

    def __hash__(self):
        return hash(self.abspath)

    def __eq__(self, other):
        return (self.mapset_directory == other.mapset_directory
            and self.rel_path == other.rel_path)
