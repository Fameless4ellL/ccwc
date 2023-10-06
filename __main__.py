import argparse
from wc import WordCounter


class ArgumentParser(object):
    """Argument parser for the command line interface."""

    def __init__(self):
        self.__parser = argparse.ArgumentParser(description="ccwc - a simple word count tool in Python")
        self.__parser.add_argument(
            "filename",
            type=str,
            help="The file to count",
        )
        self.__parser.add_argument(
            "-b",
            "--bytes",
            action="store_true",
            help="Count the number of bytes in the file",
            default=True,
        )
        self.__parser.add_argument(
            "-c",
            "--chars",
            action="store_true",
            help="Count the number of chars in the file",
            default=True
        )
        self.__parser.add_argument(
            "-l",
            "--lines",
            action="store_true",
            help="Count the number of lines in the file",
            default=True
        )
        self.__parser.add_argument(
            "-w",
            "--words",
            action="store_true",
            help="Count the number of words in the file",
            default=True
        )

    def parse(self) -> argparse.Namespace:
        """Parse the command line arguments."""
        return self.__parser.parse_args()


args_parser = ArgumentParser()
args = args_parser.parse()
wc = WordCounter(args).count(**vars(args))
print(wc)
