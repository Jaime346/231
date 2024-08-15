import os
import shutil
from_dir="/Users/jaimerosas/Downloads"
to_dir="/Users/jaimerosas/Downloads/Documentos_archivos"
list_of_files= os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extensions=os.path.splitext(file_name)
   