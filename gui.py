from tkinter import *
import tkinter.filedialog as fd
import zz

def error(msg: str) -> None:
    msg_lbl.configure(text=msg)

def upload_handler() -> None:
    try:
        file_tuple = fd.askopenfilenames(parent=root, title="Choose a file")
        zz.upload(file_tuple)
    except:
        error("No files selected!")

def create_archive() -> None:
    name_entry = archive_name.get()

    if name_entry == "":
        error("Enter a filename, smarty")
    else:
        dest_dir = fd.askdirectory(parent=root, title="Choose destination directory")
        zz.create(name_entry, dest_dir)

def open_archive() -> None:
    archive = fd.askopenfilename(filetypes=[("ZipZorp archives", ".zipzorp")])
    dest_dir = fd.askdirectory(parent=root, title="Choose destination directory")
    
    if archive and dest_dir:
        try:
            zz.unpack(archive, dest_dir)
        except:
            error("Congrats, you broke my code!")
    else:
        error("Something went wrong while unpacking.")

# Window

root = Tk()
root.geometry("700x500")
root.title("ZipZorp Client")
root.iconbitmap("assets/icon.ico")

title = Label(text="ZipZorp Client")
title["font"] = "Segoe-UI 30 bold"
title.pack(pady=10)

msg_lbl = Label(text="", fg="#f00")
msg_lbl["font"] = "Segoe-UI 20 bold"
msg_lbl.pack(pady=5)

btn_upload = Button(text="upload files", command=upload_handler)
btn_upload["font"] = "Segoe-UI 16"
btn_upload.pack(pady=15)

aname_lbl = Label(text="Archive Name:")
aname_lbl["font"] = "Segoe-UI 16 bold"
aname_lbl.pack(pady=5)

archive_name = Entry(root)
archive_name["font"] = "Segoe-UI 16"
archive_name.insert(0, "archive")
archive_name.pack(pady=5)

btn_create = Button(text="create .zipzorp", command=create_archive)
btn_create["font"] = "Segoe-UI 16"
btn_create.pack(pady=15)

btn_create = Button(text="unpack .zipzorp", command=open_archive)
btn_create["font"] = "Segoe-UI 16"
btn_create.pack(pady=15)

root.mainloop()