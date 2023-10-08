import sys
import os


def du(file):
    """
    From the given directory produce output similar to the Linux command: du -ac.
    However, rather than the number of blocks, the size of the files and directories
    should be printed.
    
    Returns:
    int: size of the given directory and all of its subdirectories/files
    """
    
    if os.path.isdir(file):  # Check if the input is a directory.
        file_size = os.path.getsize(file)  # Get the size of the directory.
        total_size = file_size  # Initialize the total size with the size of the directory itself.
        
        # Loop through the items (directories and files) within the directory.
        for dir_name in os.listdir(file):
            dir_path = os.path.join(file, dir_name)  # Create the full path to the item.
            if os.path.isdir(dir_path):  # Check if the item is a directory.
                dir_size = du(dir_path)  # Recursively calculate the size of the subdirectory.
                total_size += dir_size  # Add the subdirectory size to the total.
            else:
                dir_size = os.path.getsize(dir_path)  # Get the size of the file.
                total_size += dir_size  # Add the file size to the total.
                print(f"{dir_size}\t{dir_path}")  # Print the size and path of the file.
        
        print(f"{file_size}\t{file}")  # Print the size and path of the directory.
        return total_size  # Return the total size of the directory and its contents.
    else:
        # If the input is a file (not a directory), simply print its size and path.
        file_size = os.path.getsize(file)
        print(f"{file_size}\t{file}")
        return file_size  # Return the size of the file.
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python du.py directory")
        sys.exit(2)
    
    total_size = du(sys.argv[1])
    # print the total line
    print(f"{total_size}\ttotal")
