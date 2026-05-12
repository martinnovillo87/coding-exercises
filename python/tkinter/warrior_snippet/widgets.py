# region module
from  slot_funcs import load_images, on_click, loop_letter
from PIL import Image, ImageTk
import tkinter as tk
import random
# endregion

class UI:
    def __init__(self):
        # region root
        self.root = tk.Tk()
        self.root.title("Warrior Snippet")
        self.root.attributes("-topmost", True)
        # root.attributes("-alpha", 0.75)
        self.root.geometry("500x500")
        self.root.resizable(False, False)
        # endregion

        self.canvas_widget = tk.Canvas(self.root, width=500, height=500, highlightbackground="red", highlightthickness=2)
        self.canvas_widget.pack()

        self.loaded_images = {}
        self.current_images = {
            "body": None,
            "head": None,
            "mask": None            
        }
        load_images(self)

        # region slots
        self.body_canvas_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="body", element_kind="slot", x=252, y=341)
                
        self.head_canvas_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="head", element_kind="slot", x=259, y=248)        
        
        self.mask_canvas_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="mask", element_kind="slot", x=263, y=252)
        self.body_arrow_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="left_arrow", element_kind="button", element_target="mask", button_target=self.mask_canvas_object, x=125, y=248)

        self.tshirt_canvas_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="tshirt", element_kind="slot", x=261, y=316)
        self.tshirt_arrow_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="left_arrow", element_kind="button", element_target="tshirt", button_target=self.tshirt_canvas_object, x=125, y=341)
        # endregion
        
        # region BACKGROUND
        img = Image.open("D:/Sofa/Python/coding-exercises/python/tkinter/warrior_snippet/assets/background/bg_new.png").convert("RGBA")
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
        bg1 = self.canvas_widget.create_image(0, 0, anchor="nw", image=tk_img)
        bg2 = self.canvas_widget.create_image(0, -canvas_height, anchor="nw", image=tk_img)
        def scroll_bg():
            self.canvas_widget.move(bg1, 0, 2)
            self.canvas_widget.move(bg2, 0, 2)
            y1 = self.canvas_widget.coords(bg1)[1]
            y2 = self.canvas_widget.coords(bg2)[1]
            if y1 >= img.height:
                self.canvas_widget.coords(bg1, 0, -img.height)
            if y2 >= img.height:
                self.canvas_widget.coords(bg2, 0, -img.height)
            self.canvas_widget.tag_lower(bg1)
            self.canvas_widget.tag_lower(bg2)
            self.root.after(50, scroll_bg)
        scroll_bg()
        # endregion
        
        # region title
        self.title_letters = {}
        self.title_letters["b"] = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="b", element_kind="letter", x=200, y=50)
        self.title_letters["i"] = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="i", element_kind="letter", x=250, y=50)
        self.title_letters["t"] = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="t", element_kind="letter", x=300, y=50)
        loop_letter(self)
        # endregion
    
        self.root.mainloop()

class CanvasElement:
    def __init__(self, ui, canvas, x, y, element_type, element_kind, element_target=None, button_target=None):
        # self.tags = tags
        self.button_target = button_target
        self.ui = ui
        self.canvas = canvas
        self.x = x
        self.y = y
        self.element_type = element_type
        self.element_kind = element_kind
        self.element_target = element_target
        #1 # self.image = random.choice(list(ui.loaded_images[self.element_type]["variant"].values())) if self.element_kind=="slot" else ui.loaded_images[self.element_type]["state"]["default"] 
        
        #2 # self.image = random.choice(list(ui.loaded_images[self.element_type]["variant"].values())) if self.element_kind=="slot" \
        # else ui.loaded_images["letter"][self.element_type]["yellow"] if self.element_kind == "letter" \
        # else ui.loaded_images[self.element_type]["state"]["default"] 
        
        self.image = random.choice(list(ui.loaded_images[self.element_type]["variant"].values())) if self.element_kind=="slot" \
        else random.choice(list(ui.loaded_images["letter"][element_type]["color"].values())) if self.element_kind == "letter" \
        else ui.loaded_images[self.element_type]["state"]["default"] 
        
        self.id = self.canvas.create_image(x, y, anchor="center", image=self.image) 
        if self.element_kind == "button":
            self.canvas.tag_bind(self.id, "<Button-1>", lambda event: on_click(self, event))

        self.set_current_image(ui, self.image)
        
    def set_current_image(self, ui, image):
        ui.current_images[self.element_type] = image

# class Title(CanvasElement):
#     def __init__(self, ui, canvas, x, y, element_kind, element_type=None, element_target=None, button_target=None):
#         super().__init__(ui, canvas, x, y, element_type, element_kind, element_target, button_target)
        
        
    