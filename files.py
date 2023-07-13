def create(file_name: str, content: str = None):
    """Create a new text file

    Args:
        file_name (str): File name or path
        content (str, optional): Text file content. Defaults to None.
    """
    mode = "w" if content else "x"

    file = open(file_name, mode)

    if content:
        file.write(content)

    file.close()
