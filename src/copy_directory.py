import os
import shutil

def copy_directory(source_path, dest_path):
    if os.path.exists(dest_path):
        print("Deleting public directory...")
        shutil.rmtree(dest_path)
    os.mkdir("public", mode = 0o777)
    print("Copying static files to public directory...")
    helper(source_path, dest_path)

def helper(source_path, dest_path):
    ls = os.listdir(source_path)
    desination_path = dest_path + source_path.removeprefix("static/")
    for item in ls:
        item_path = f"{source_path}{item}"
        if os.path.isfile(item_path):
            shutil.copy(item_path, desination_path)
            print(f"{item} copied to {desination_path}")
            pass
        else:
            os.mkdir(desination_path+item, mode = 0o777)
            helper(f"{item_path}/", desination_path)