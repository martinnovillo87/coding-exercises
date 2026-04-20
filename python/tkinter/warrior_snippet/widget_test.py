# region module
from  slot_funcs import load_images, on_click #set_active_slots
import slot_funcs
import tkinter as tk
import random
# endregion

class UI:
    def __init__(self, root):
        self.canvas_widget = tk.Canvas(root, width=500, height=500, highlightbackground="red", highlightthickness=2)
        self.canvas_widget.pack()

        self.loaded_images = {}
        self.current_images = {
            "body": None,
            "head": None,
            "mask": None            
        }
        load_images(self)
        
        # body_image = random.choice(list(self.loaded_images["body"]["variant"].values()))
        # body_image  = self.loaded_images["body"]["variant"]["simple"]
        # body_image_id = self.canvas_widget.create_image(252, 341, anchor="center", image=body_image, tags=("character", "slot", "body"))
        # self.body_canvas_object = CanvasElement(self, self.canvas_widget, body_image_id, body_image, "slot", "body", target=None)
        
        self.body_canvas_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="body", element_kind="slot", x=252, y=341)
        
        
        self.head_canvas_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="head", element_kind="slot", x=259, y=248)        
        
        self.mask_canvas_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="mask", element_kind="slot", x=263, y=252)
        self.body_arrow_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="left_arrow", element_kind="button", element_target="mask", button_target=self.mask_canvas_object, x=125, y=248)

        self.tshirt_canvas_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="tshirt", element_kind="slot", x=261, y=316)
        self.tshirt_arrow_object = CanvasElement(ui=self, canvas=self.canvas_widget, element_type="left_arrow", element_kind="button", element_target="tshirt", button_target=self.tshirt_canvas_object, x=125, y=341)
        
        # for img, data in self.loaded_images.items():
        #     print(img, data)
        # print(self.current_images)
        

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
        self.image = random.choice(list(ui.loaded_images[self.element_type]["variant"].values())) if self.element_kind=="slot" else ui.loaded_images[self.element_type]["state"]["default"]
        self.id = self.canvas.create_image(x, y, anchor="center", image=self.image) 
        if self.element_kind == "button":
            self.canvas.tag_bind(self.id, "<Button-1>", lambda event: slot_funcs.on_click(self, event))

        self.set_current_image(ui, self.image)
        
    def set_current_image(self, ui, image):
        ui.current_images[self.element_type] = image
        
        
    