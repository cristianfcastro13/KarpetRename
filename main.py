import os
import argparse #Here in case I come back to using this

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