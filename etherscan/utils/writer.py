import os
from pathlib import Path


def write_code(content,file_name,save_path):
  #function for writing code into file
  full_path=f'{save_path}/{file_name}'
  head_tail = os.path.split(full_path)
  dirs=head_tail[0]
  files=head_tail[1]
  if not os.path.exists(dirs):
    os.makedirs(dirs)
  with open(full_path, "w") as file:
        file.write(str(content))
        return full_path
