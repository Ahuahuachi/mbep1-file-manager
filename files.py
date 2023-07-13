"""File management"""


def create(file_name: str, content: str = None):
    """Create a new text file

    Args:
        file_name (str): File name or path
        content (str, optional): Text file content. Defaults to None.
    """
    mode = "w" if content else "x"

    try:
        file = open(file_name, mode)

    except FileExistsError as error:
        raise OSError(f"File '{file_name}' already exists") from error

    except PermissionError as error:
        raise OSError(f"You do not hav permisson to create '{file_name}'") from error

    if content:
        file.write(content)

    file.close()


def update(file_name: str, content: str, overwrite: bool = False):
    """Updates an existing file

    Args:
        file_name (str): File name or path
        content (str): Text file content
        overwrite (bool, optional): If True, file will be overwritten. Defaults to False.
    """
    mode = "w" if overwrite else "a"

    file = open(file_name, mode)
    file.write(content)
    file.close()
