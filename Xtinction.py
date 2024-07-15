import os
import tkinter.filedialog
from tkinter import *
from tkinter import messagebox
import send2trash
from PIL import Image, ImageTk


bg_color='#171616'
window=Tk()
window.geometry('1200x600')
window.title("Extinction")
window.config(bg=bg_color)

folders=set() #Using a set so we dont have the same element twice
extensions=set()
send_to_bin=BooleanVar(value=True) #Storing the checkbox state
font=('Futura',15,'bold')
style={'font':font,'bg':'#2E2C2C','fg':'#ffffff'}
def select_folders():
    global folders
    folder=tkinter.filedialog.askdirectory()
    if folder and folder not in folders: #Ensure that a folder is selected , and the folder is not in the folders set
        folders.add(folder)
        update_folders_display()
    else:
        messagebox.showwarning('WARNING','Folder already selected or folder not selected')


def update_folders_display(): #Used to update the text
    folders_label.config(text=f"Selected Folders: {', '.join(folders)}")


def select_extensions():
    global extensions
    new_extensions=add_extensions.get() #Get the extension entered by the user
    if new_extensions and new_extensions not in extensions:
        extensions.add(new_extensions)
        update_extensions_display()
    else:
        messagebox.showwarning("WARNING",'Extension already selected or no extension entered.')


def update_extensions_display():
    extensions_label.config(text=f"Selected Extensions: {', '.join(extensions)}")


def delete_files():
    if not folders or not extensions: #To ensure that at least one folder and one extension is selected
        messagebox.showerror("Error", "Please select at least one folder and one extension before deleting files.")
        return
    files_to_delete=[] #This list will store the paths of files that match the specified extensions and are located in the selected folders.
    for folder in folders: #Iterates over each folder in folders
        for root,directories,files in os.walk(folder): #root is the current directory path. directories is a list of directories in the current directory. files is a list of files in the current directory. os.walk() used to traverse the directory tree rooted at folder
            for file in files: #Iterates over each file
                if any(file.endswith(extension) for extension in extensions): #Checks if any file ends with any extension entred by the user
                    file_path=os.path.join(root,file)
                    files_to_delete.append(file_path)
    if not files_to_delete:
        messagebox.showerror("Error", "No files found with the specified extensions.")
        return
    confirmation(files_to_delete)


def confirmation(files_selected):
    confirmation_dialog=Toplevel(window)
    confirmation_dialog.geometry('600x400')
    confirmation_dialog.title('Confirm')

    Label(confirmation_dialog,text='This files will be deleted : ').pack()
    text=Text(confirmation_dialog)
    text.pack(expand=True,fill=BOTH)

    for file_path in files_selected:
        text.insert(END,f'{file_path}\n')

    def action_confirmed():
        for file_path in files_selected:
            file_path = os.path.normpath(file_path)  #Normalise the file path : cleans up the file path by collapsing redundant separators and up-level references.
            if send_to_bin.get():
                send2trash.send2trash(file_path) #Moves the file to the recycle bin

            else:
                os.remove(file_path) #The file is permanently deleted
        if send_to_bin.get():
            success_message = 'Files have been sent to trash successfully'
        else:
            success_message = 'Files have been deleted successfully'

        messagebox.showinfo('Operation Completed', success_message)
        confirmation_dialog.destroy() #Close the confirmation window

    def action_canceled():
        global folders, extensions
        folders.clear() #Removes everything from the folders set
        extensions.clear() #Removes everything from the extension set
        add_extensions.delete(0, END)#Deletes all the text from the entry widget
        confirmation_dialog.destroy()# Close the confirmation window

    button_frame = Frame(confirmation_dialog)
    button_frame.pack(fill=X, pady=10)

    Button(button_frame, text="Yes", command=action_confirmed,**style).pack(side=LEFT, padx=20, pady=20)
    Button(button_frame, text="No", command=action_canceled,**style).pack(side=RIGHT, padx=20, pady=20)

def reset():
    global folders, extensions
    folders.clear()
    extensions.clear()
    add_extensions.delete(0, END)
    update_folders_display()
    update_extensions_display()




logo='XtinctionLogo.png'
logo_image = Image.open(logo)
logo_image = logo_image.resize((120, 50), Image.LANCZOS)  # Resize to 50x50 pixels
logo_image = ImageTk.PhotoImage(logo_image)




logo_frame = Label(window, image=logo_image, bg=bg_color)
logo_frame.pack(pady=5)



select_btn=Button(window,text="Add folder",command=select_folders,**style)
select_btn.pack(anchor='w',pady=10,padx=20)


add_extensions_text=Label(window,font=font,text='Enter the extensions (one by one) : ',bg=bg_color,fg='#ffffff')
add_extensions_text.pack(anchor='w',pady=10,padx=20)

add_extensions=Entry(window,font=font)
add_extensions.pack(anchor='w',pady=10,padx=20)

select_extensions_btn=Button(window,text="Confirm extension",command=select_extensions,**style)
select_extensions_btn.pack(anchor='w',pady=10,padx=20)

send_to_bin_checkbox=Checkbutton(window,text="Send to trash bin",variable=send_to_bin,font=font,fg=bg_color)
send_to_bin_checkbox.pack(anchor='w',pady=10,padx=20)


delete_btn=Button(window,text="Delete files",command=delete_files,**style)
delete_btn.pack(anchor='w',pady=5,padx=20)

reset_btn=Button(text='Reset',command=reset, **style)
reset_btn.pack(anchor='w',pady=10,padx=20)

folders_label = Label(window, text="Selected Folders:",font=font,bg=bg_color,fg='#ffffff')
folders_label.pack(anchor='w',pady=10,padx=20)

extensions_label = Label(window, text="Selected Extensions:",font=font,bg=bg_color,fg='#ffffff')
extensions_label.pack(anchor='w',pady=10,padx=20)

window.mainloop()