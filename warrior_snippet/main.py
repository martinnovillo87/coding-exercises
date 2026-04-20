# region module
import tkinter as tk
import widget_test
# endregion

# region root
root = tk.Tk()
root.title("Warrior Snippet")
root.attributes("-topmost", True)
root.attributes("-alpha", 0.75)
root.geometry("500x500")
root.resizable(False, False)
# endregion

ui = widget_test.UI(root)

# region mainloop
root.mainloop()
# endregion

