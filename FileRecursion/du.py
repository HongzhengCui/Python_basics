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
    
    if os.path.isdir(file):
        file_size = os.path.getsize(file)
        total_size = file_size
        for dir_name in os.listdir(file):
            dir_path = os.path.join(file, dir_name)
            
            if os.path.isdir(dir_path):
                dir_size = du(dir_path)
                total_size += dir_size
            else:
                dir_size = os.path.getsize(dir_path)
                total_size += dir_size
                print(f"{dir_size}\t{dir_path}")
        
        print(f"{file_size}\t{file}")
        return total_size
    
    else:
        file_size = os.path.getsize(file)
        print(f"{file_size}\t{file}")
        return file_size
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python du.py directory")
        sys.exit(2)
    
    total_size = du(sys.argv[1])
    # print the total line
    print(f"{total_size}\ttotal")
