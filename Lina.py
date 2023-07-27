import os

ExistedFolderName = "../Assignment/files"
subFoldersPath = "../Assignment/subFolders"

#get all files
file_list = os.listdir(ExistedFolderName)

for file_name in file_list:
    file_path = os.path.join(ExistedFolderName, file_name)
    with open(file_path, "r") as file:
        file_content = file.read()
    
    #get the base name (language name)of the file
    base_name, file_extension = os.path.splitext(file_name)
    subFolderName = base_name.split("-")[0]  
    
    #check if there is a file for this language , if no create one
    if not os.path.exists(os.path.join(subFoldersPath, subFolderName)):
        os.makedirs(os.path.join(subFoldersPath, subFolderName))

    #identify the new path for the new subfolder
    file_path_in_subfolder = os.path.join(subFoldersPath, subFolderName, file_name)

    #write the file in it's new subfolder
    with open(file_path_in_subfolder, "w") as file:
        file.write(file_content)