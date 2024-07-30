import os
import sys

def files_sort(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    sorted_files = sorted(files, key=lambda x: (x.split('.')[-1], x))
    return sorted_files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python files_sort.py <directory>")
        sys.exit()

    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"{directory} is not a valid directory.")
        sys.exit()

    sorted_files = files_sort(directory)
    for file in sorted_files:
        print(file)