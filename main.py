import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import PIL
from PIL import Image






root = tk.Tk()
root.title('Tkinter')
root.resizable(False, False)
root.geometry('300x150')


def select_files():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)


    showinfo(
        title='Metadata deleted for the following file:',
        message=filenames

    )



# open button
open_button = ttk.Button(
    root,
    text='Open Files, Images to Clear Metadata ',
    command=select_files


)




open_button.pack(expand=True)

root.mainloop()
# next 3 lines strip exif
m=select_files()
im = Image.open(m)
    # this clears all exif data
im.getexif().clear()
im.save('some-image-without-exif.jpg')

