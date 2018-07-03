import os


def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            print("Deleting file {}".format(file_path))
            os.remove(file_path)
        else:
            print("File {} does not exist for deletion.".format(file_path))
    except OSError:
        print("Error deleting file {}!".format(file_path))
