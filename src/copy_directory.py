import os
import shutil

def copy_directory(source_path, dest_path):
    if os.path.exists(dest_path):
        print(f"Deleting {dest_path} directory...")
        shutil.rmtree(dest_path)
    os.mkdir("public", mode = 0o777)
    print(f"Copying {source_path} files to {dest_path} directory...")
    helper(source_path, dest_path)

def helper(source_path, dest_path):
      if not os.path.exists(dest_path):
          os.mkdir(dest_path)
      ls = os.listdir(source_path)
      for item in ls:
        item_path = f"{source_path}{item}"
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest_path)
            print(f"{item} copied to {dest_path}")
            pass
        else:
            helper(f"{item_path}/", dest_path+item+"/")