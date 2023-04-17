from tkinter import *
from tkinter import ttk
import os 
import ctypes
import poke_api
import image_lib

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

image_cache_dir = os.path.join(script_dir, 'images')
if not os.path.isdir(image_cache_dir):
    os.makedirs(image_cache_dir)

# Create the main window
root = Tk()
root.title("Pokemon Image Viewer")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.minsize(500, 600)

icon_path = os.path.join(script_dir, 'Great-Ball.ico')
app_id = 'COMP593.PokeImageViewer'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
root.iconbitmap(icon_path)

root.iconbitmap(icon_path)

frame = ttk.Frame(root, relief='ridge')
frame.grid(row=0, column=0, sticky=NSEW)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)


image_path = os.path.join(script_dir, 'pikachu.png')
img_poke = PhotoImage(file=image_path)
lbl_image = ttk.Label(frame, image=img_poke)
lbl_image.grid(padx=10, pady=10)

poke_name_list = sorted(poke_api.get_pokemon_name())
cbox_pokemon = ttk.Combobox(frame, values=poke_name_list, state='readonly')
cbox_pokemon.set("Select a Pokemon")
cbox_pokemon.grid(padx=10, pady=10)

def handle_pokemon(event):
    sel_pokemon = cbox_pokemon.get()
    global image_path
    image_path = poke_api.download_pokemon_artwork(sel_pokemon, image_cache_dir)
    img_poke['file'] = image_path
    if image_path is not None:
        img_poke['file'] = image_path
        btn_set_desktop.state(['!disabled'])

cbox_pokemon.bind('<<ComboboxSelected>>', handle_pokemon)

def handle_set_desktop():
    image_lib.set_desktop_background_image(image_path)

btn_set_desktop = ttk.Button(frame, text='Set as Desktop Image', command=handle_set_desktop)
btn_set_desktop.grid(padx=10, pady=10)

root.mainloop()
