"""File management"""
import os
import json


def create(file_name: str, content: list | dict = None) -> None:
    """Create a new json file

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

    if content and isinstance(content, (list, dict)):
        content = json.dumps(content)
        file.write(content)

    file.close()


def update(file_name: str, content: str, overwrite: bool = False) -> None:
    """Updates an existing file

    Args:
        file_name (str): File name or path
        content (str): Text file content
        overwrite (bool, optional): If True, file will be overwritten. Defaults to False.
    """
    if not isinstance(content, str) or content == "":
        raise ValueError("'content' argument must be specified")

    mode = "w" if overwrite else "a"

    file = open(file_name, mode)
    file.write(content)
    file.close()


def read(file_name: str) -> str:
    """Returns the content of a text file

    Args:
        file_name (str): File name or path

    Returns(str): File content
    """
    file = open(file_name)
    content = file.read()
    file.close()
    return content
