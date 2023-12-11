import os


def create_files(directory_path, num_files=11200):
    """
    Creates a specified number of text files within a given directory.

    This function is useful for generating a large number of files
    for testing or other purposes.
    Each file will be named in the format 'file_x.txt',where 'x' is the file number.
    The content of each file will be a simple string stating the file number.

    Parameters:
    directory_path (str): The path to the directory where files will be created.
                          If the directory does not exist, it will be created.
    num_files (int): Optional. The number of files to create. Default is 11,200.

    Returns:
    None. The function will print a message indicating the number of files created and the directory path.

    Usage Example:
    create_files('path/to/directory', 500)  # Creates 500 files in 'path/to/directory'
    """

    # Create the directory if it doesn't exist
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)

    for i in range(1, num_files + 1):
        file_name = f"file_{i}.txt"
        full_path = os.path.join(directory_path, file_name)

        with open(full_path, "w") as file:
            file.write(f"This is file number {i}")

    print(f"Created {num_files} files in {directory_path}.")


# Usage Example
create_files("./test_files")
