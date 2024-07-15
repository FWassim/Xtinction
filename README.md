# Welcome to Xtinction main page !

**Xtinction** is a simple application that allow you to remove all the files with the same extension located in a folder or different folder.

# About Xtinction
**Xtinction** is a powerful file management application designed to streamline the process of deleting files based on their extensions. With Extinction, you can effortlessly choose file extensions such as .pdf, .jpg, and more, and select multiple folders from which you want to remove files with the chosen extensions. The primary objective of this tool is to save you valuable time by automating the file deletion process, eliminating the need to manually remove files. This is especially beneficial when dealing with directories containing numerous subfolders; simply select the parent folder, and Extinction will recursively delete the specified files from all subfolders. The application features an intuitive GUI built with Tkinter, a confirmation dialog to review files before deletion, and options to either permanently delete files or move them to the trash bin, ensuring a seamless and efficient file management experience.

# About the code
This version, posted on July 15, 2024, uses Python 3.10.3. The GUI is built with Tkinter, with plans for a shell version in the future. When selecting folders and extensions, they are stored in sets to prevent duplicates. The select_folders function uses a dialog box for folder selection and adds the chosen folder to the set. The select_extensions function stores the entered extension in a variable and adds it to the extensions set.

The delete_files function first checks if any folders or extensions have been selected. It then initializes an empty list to store the paths of files that match the specified extensions. The function iterates over each selected folder, uses os.walk() to traverse the directory tree, and iterates over each file in the current directory. It checks if each file's name ends with any of the specified extensions, and if a match is found, it constructs the full file path and adds it to the list of files to delete.

The action_confirmed function iterates over a list of selected file paths, normalizes each file path, and checks whether the files should be sent to the trash or deleted permanently based on the value of the send_to_bin variable. The action_canceled function clears the global folders and extensions sets, clears the contents of the add_extensions entry widget, and closes the confirmation dialog window by destroying it. For more specific details, please refer to the code itself.





