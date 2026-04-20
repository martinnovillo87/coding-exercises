# # region module
# from  slot_funcs import load_images, on_click #set_active_slots
# import slot_funcs
# import tkinter as tk
# import random
# # endregion

# class UI:
#     def __init__(self, root):
#         self.canvas_widget = tk.Canvas(root, width=500, height=500, highlightbackground="red", highlightthickness=2)
#         self.canvas_widget.pack()

#         self.loaded_images = {}
#         self.current_images = {
#             "body": None,
#             "head": None,
#             "mask": None            
#         }

#         load_images(self)

       
        

#         self.button_state = {}
        
#         # TAGS -> 0: category,  1:type, 2:id, 3:target 
#         # body_frame_image_id = self.canvas_widget.create_image(252, 341, anchor="center", image=self.loaded_images["body"]["frame"], tags=("ui", "frame", "body"))
#         body_frame_image_id = None

#         body_image_id = self.canvas_widget.create_image(252, 341, anchor="center", image=self.loaded_images["body"]["variant"]["simple"], tags=("character", "slot", "body"))

#         head_frame_image_id = self.canvas_widget.create_image(259, 248, anchor="center", image=self.loaded_images["head"]["frame"], tags=("ui", "frame", "head"))

#         head_image_id = self.canvas_widget.create_image(259, 248, anchor="center", image=self.loaded_images["head"]["variant"]["simple"], tags=("character", "slot", "head"))

#         mask_frame_image_id = self.canvas_widget.create_image(263, 251, anchor="center", image=self.loaded_images["mask"]["frame"], tags=("ui", "frame", "mask"))

#         mask_image_id = self.canvas_widget.create_image(262, 251, anchor="center", image=random.choice(self.loaded_images["mask"]["variant"]), tags=("character", "slot", "mask"))
        
#         left_arrow_frame_image_id = self.canvas_widget.create_image(125, 251, anchor="center", image=self.loaded_images["left_arrow"]["frame"], tags=("ui", "frame", "left_arrow"))

#         left_arrow_image_id = self.canvas_widget.create_image(125, 251, anchor="center", image=self.loaded_images["left_arrow"]["variant"]["simple"], tags=("ui", "button", "left_arrow", "target:mask"))
        
#         self.canvas_widget.tag_bind(left_arrow_image_id, "<Button-1>", lambda event: on_click(self, event))
#         self.slots = [body_image_id, body_frame_image_id, head_image_id, head_frame_image_id, mask_image_id, mask_frame_image_id, left_arrow_image_id, left_arrow_frame_image_id]
#         # set_active_slots(self)
        










