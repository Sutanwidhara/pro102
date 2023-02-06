import os
import shutil

# .exe , .msi,  .gif, .png .jpg, .jpeg, .csv, .pdf , .xls , .xlsx , .ppt , .pptx

from_dir = ":/Users/sukan/DropboxPC/Desktop/Automation"
to_dir = "C:/Users/sukan/Dropbox/PC/Desktop/Segregation"

list_of_files = os.listdir(from_dir)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:

        path1 = from_dir + '/' + file_name                             
        path2 = to_dir + '/' + "Image_Files"                          
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name   
        
        if os.path.exists(path2):
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)