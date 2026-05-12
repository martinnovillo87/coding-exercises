# region IMPORTS
import tkinter as tk
from PIL import Image, ImageTk
from main import root
# endregion

# region CANVAS
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()
# canvas.image_refs = []
    # region BACKGROUND
img = Image.open("clouds.jpg").convert("RGBA")
canvas_width, canvas_height = 500, 500
scale = max(canvas_width / img.width, canvas_height / img.height)
new_width = int(img.width * scale)
new_height = int(img.height * scale)
img_resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

# Crear un lienzo del tamaño del canvas y centra la imagen redimensionada
img_final = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 0))  # fondo transparente
x_offset = (canvas_width - new_width) // 2
y_offset = (canvas_height - new_height) // 2
img_final.paste(img_resized, (x_offset, y_offset))
# Crear PhotoImage
tk_img = ImageTk.PhotoImage(img_final)
# Dibujar en canvas
bg1 = canvas.create_image(0, 0, anchor="nw", image=tk_img)
bg2 = canvas.create_image(0, -canvas_height, anchor="nw", image=tk_img)
def scroll_bg():
    canvas.move(bg1, 0, 2)
    canvas.move(bg2, 0, 2)
    y1 = canvas.coords(bg1)[1]
    y2 = canvas.coords(bg2)[1]
    if y1 >= img.height:
        canvas.coords(bg1, 0, -img.height)
    if y2 >= img.height:
        canvas.coords(bg2, 0, -img.height)
    root.after(50, scroll_bg)
    # endregion
# endregion