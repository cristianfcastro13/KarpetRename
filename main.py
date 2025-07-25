import os
import argparse

# Renames files in a sequential numerical order starting from 1
def rename_files(directory, prefix, suffix, dryrun):
    try:
        target_directory_files = os.listdir(directory)
    except:
        print(f"Error: The directory '{directory}' was not found.")
        return
    
    file_count = 1
    print(f"{len(target_directory_files)} files were found in '{directory}'.")

    if dryrun:
        print("This is what the files will be renamed to:")
    else:
        print("Beginning renaming...")

    for filename in target_directory_files:
        current_item = os.path.join(directory, filename)
        if os.path.isfile(current_item):
            _, extension = os.path.splitext(filename)
            new_name = f"{prefix}{file_count}{suffix}{extension}"
            new_destination = os.path.join(directory, new_name)

            if not dryrun:
                try:
                    os.rename(current_item, new_destination)
                    file_count += 1
                except FileNotFoundError:
                    print(f"Error: The file '{current_item}' was not found.")
                except PermissionError:
                    print(f"Error: Permission denied. Cannot rename '{current_item}'.")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
            else:
                print(new_name)
                file_count += 1
        else:
            print(f"Skipping {filename} since it's a directory.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('destination', help='This is the folder in which the items will be renamed.')
    parser.add_argument('--prefix', default='', help='This is the prefix (string) to the ordered number in each item renamed')
    parser.add_argument('--suffix', default='', help='This is the suffix (string) to the ordered number in each item renamed')
    parser.add_argument('--dryrun', action='store_true')
    args = parser.parse_args()
    rename_files(args.destination, args.prefix, args.suffix, args.dryrun)