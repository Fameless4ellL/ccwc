import os
from argparse import Namespace


class WordCounter(object):
    def __init__(self, args: Namespace):
        self.__filename = args.filename
        self.args = {
            "bytes": self._bytes,
            "chars": self._chars,
            "lines": self._lines,
            "words": self._words
        }
        self.__data = None
        self.open_file()

    def count(self, **kwargs: dict[str, bool]) -> str:
        """Count the number of words in the file"""
        return "\n".join([f"{method}: {self.args[method]()}" for method in self.args if kwargs[method]])

    def _words(self) -> int:
        """Count the number of bytes in the file"""
        return len(self.__data.split())

    def _bytes(self) -> int:
        """Count the number of characters in the file"""
        return len(self.__data.encode("utf8"))

    def _lines(self) -> int:
        """Count the number of lines in the file"""
        return len(self.__data.splitlines())

    def _chars(self) -> int:
        """Count the number of characters in the file"""
        return len(self.__data)

    def __str__(self):
        return f"WordCounter({self.__filename})"

    def __repr__(self):
        return f"WordCounter({self.__filename})"

    def open_file(self):
        # Check if the file exists
        if not os.path.exists(self.__filename):
            raise FileNotFoundError(f"File {self.__filename} not found")

        with open(self.__filename, "r", encoding="utf8") as f:
            self.__data = f.read()
        return self
