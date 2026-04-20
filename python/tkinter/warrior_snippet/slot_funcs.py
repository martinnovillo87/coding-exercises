# region module
from PIL import Image, ImageTk
import random
import slots
# endregion

def load_images(self):
    self.loaded_images = {
        "head": {
            "frame": None,
            "variant": {
                "simple": None}
            },
        "body": {
            "frame": None,
            "variant":{
                "simple": None,}
                # "inverted": None}
                },
        "mask": {
            "frame": None,
            "variant": {
                "simple": None,
                "jason": None,
                "skull": None}
                },
        "left_arrow": {
            "frame": None,
            "state": {
                "default": None,
                "pressed": None}
            },
        "tshirt": {
            "variant": {
                "yellow": None,
                "red": None,
            }
        }
    }
    
    for slot, slot_data in self.loaded_images.items():
        if "frame" in slot_data and slot_data["frame"] is None:
            image = Image.open(f"assets/sprites/{slot}_frame.png")
            slot_data["frame"] = ImageTk.PhotoImage(image)

        if "variant" in slot_data:
            for variant_name, variant_img in slot_data["variant"].items():
                if variant_img is None:
                    image = Image.open(f"assets/sprites/{slot}_{variant_name}.png")
                    slot_data["variant"][variant_name] = ImageTk.PhotoImage(image)
        
        if "state" in slot_data:
            for state_name, state_img in slot_data["state"].items():
                if state_img is None:
                    image = Image.open(f"assets/sprites/{slot}_{state_name}.png")
                    slot_data["state"][state_name] = ImageTk.PhotoImage(image)

        

# def set_active_slots(self):
#     self.canvas_widget.addtag_withtag("active", "slot")

def on_click(self, event=None):
    animate_click(self)
    swap_slot(self)

def animate_click(self):
    item = self.canvas.find_withtag("current")[0]
    # tags = self.canvas.gettags(item)
    item_type = self.element_type
    images = self.ui.loaded_images[item_type]
    self.canvas.itemconfig(item, image=images["state"]["pressed"])
    self.canvas.after(
        100,
        lambda: self.canvas.itemconfig(item, image=images["state"]["default"])
    )

# def swap_slot(self):
#     for name, data in self.ui.loaded_images[self.element_target]["variant"].items():
#         if data != self.ui.current_images[self.element_target]:
#             self.canvas.itemconfigure(self.button_target.id, image=data)
#             self.ui.current_images[self.element_target] = data
#             break
                #     print(name, data)

def swap_slot(self):
    variants = list(self.ui.loaded_images[self.element_target]["variant"].values())
    current = self.ui.current_images[self.element_target]

    index = variants.index(current)
    next_index = (index + 1) % len(variants)
    next_image = variants[next_index]

    self.canvas.itemconfigure(self.button_target.id, image=next_image)
    self.ui.current_images[self.element_target] = next_image

    print(index)
    


                
        

        


