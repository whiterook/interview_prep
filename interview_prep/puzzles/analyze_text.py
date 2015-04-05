__author__ = 'Sergey'


def analyze_text(file_name):
    """Calculates the number of lines and characters in a file

    Args:
        file_name: the name of the file

    Raises:
        IOError: If ''file_name'' doesn't exists or can't be read.

    Returns: the number of line and the numbers of characters in a line for the given file
    """

    lines = 0
    chars = 0
    with open(file_name, 'r') as f:
        for line in f:
            lines += 1
            chars += len(line)
    return (lines, chars)





