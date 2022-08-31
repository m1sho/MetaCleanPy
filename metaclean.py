import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import PIL
from PIL import Image




metadata_Erase = False


root = tk.Tk()
root.title('Tkinter')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    metadata_Erase=True
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')

    )

    filenames = fd.askopenfilename(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)



    showinfo(
        title='Metadata deleted for the following file:',
        message=filenames


    )

    if metadata_Erase == True:
        im = Image.open(filenames)
        # this clears all exif data
        im.getexif().clear()
        im.save(filenames)


# open button
open_button = ttk.Button(
    root,
    text='Open Files, Images to Clear Metadata ',
    command=select_files




)





open_button.pack(expand=True)

root.mainloop()


