import tkinter.filedialog as fd
import os, shutil, zipfile

def upload(ft) -> None:
    if "files" in os.listdir(os.curdir):
        shutil.rmtree("files")
    
    os.mkdir("files")
    
    for f in ft:
        fn = f.split("/")[-1]
        shutil.copy(f, f"files/{fn}")

def create(name: str, ddir: str) -> None:
    shutil.make_archive(name, "zip", "files")
    shutil.move(f"{name}.zip", ddir)
    os.rename(f"{ddir}/{name}.zip", f"{ddir}/{name}.zipzorp")

def unpack(archive, ddir) -> None:
    aname = archive.split("/")[-1]
    aname_clean = aname.split(".")[:-1][0]
    unpack_dir = f"{ddir}/{aname_clean}"

    if aname_clean not in os.listdir(ddir):
        os.mkdir(unpack_dir)

    shutil.copy(archive, unpack_dir)
    os.rename(f"{unpack_dir}/{aname}", f"{unpack_dir}/{aname_clean}.zip")

    shutil.unpack_archive(f"{unpack_dir}/{aname_clean}.zip", unpack_dir)

    os.remove(f"{unpack_dir}/{aname_clean}.zip")