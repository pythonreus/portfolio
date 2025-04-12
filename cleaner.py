import os

folder_path = "C:/Users/Lesiba Marcel/Pictures/Projects/Portfolio"

file_ext = set()

for root,dirs,files in os.walk(folder_path):
   for file in files:
      ext = os.path.splitext(file)[1]
      file_ext.add(ext)

for ext in file_ext:
   print(ext)      