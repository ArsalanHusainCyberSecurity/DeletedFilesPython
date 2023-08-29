import os

def detect_deleted_files(directory, baseline_files):
    current_files = set(os.listdir(directory))
    deleted_files = baseline_files - current_files
    return deleted_files

if __name__ == "__main__":
    # Replace this with the path to the directory you want to monitor
    target_directory = "/path/to/target/directory"

    # Baseline list of files before any deletion
    baseline_files = set(os.listdir(target_directory))

    input("Perform the deletion in the target directory and press Enter...")

    # Detect deleted files
    deleted_files = detect_deleted_files(target_directory, baseline_files)

    if deleted_files:
        print("Deleted files:")
        for file in deleted_files:
            print(file)
    else:
        print("No files were deleted.")
