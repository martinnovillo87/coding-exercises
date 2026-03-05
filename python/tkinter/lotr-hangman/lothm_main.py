import random
import tkinter as tk
from PIL import Image, ImageTk
import lothm_funcs

# root window
root = tk.Tk()
root.title("Lord of the hanged")
root.attributes("-topmost", True)
root.geometry("800x600")
root.resizable(False, False)
root.configure(background="black")



# def start():
#     # random_word = random.choice(list_words).lower()
#     # text_input = tk.Text(root, font=("Ringbearer", 20), fg="white", background="black")
#     # text_input.pack()
#     word = list(random_word)
#     player_word = []
#     used_letters = []
#     failed_attempts = 0
#     for i in range(len(random_word)):
#         player_word.append("_")
#         print(player_word)
#     text_input.insert("1.0",player_word)
#     letter_entry = tk.Entry(root, font=("Ringbearer", 20), fg="white")
#     letter_entry.pack()
#     while True:
#         question_letter = input("Choose a letter: ").lower()
#         letter_entry.delete(0, tk.END)
#         if len(question_letter)>1:
#             print("Choose a valid letter")
#             continue
#         #applicable answer
#         else:
#             for index, letter in enumerate(word):
#                 if question_letter == letter:

#                     print(f"Got {question_letter}")
#                     player_word[index] = question_letter
#                     text_input.insert("1.0", player_word)
#                     continue
#                     # No poner break aca!
#             print(player_word)
#             if "_" not in player_word:
#                 print("You won!")
#                 print(f"{random_word}: {lotr_dict[random_word.title()]}")
#                 break
#             if question_letter not in word:
#                 print(f"{question_letter} not in {word}")
#                 if question_letter in used_letters:
#                     print(f"{question_letter} already used")
#                 else:
#                     used_letters.append(question_letter)
#                     failed_attempts += 1
#                     print(f"Wrong! Used letters: {used_letters}")
#                     print(f"Failed attempts: {failed_attempts}")
#                     if failed_attempts >= 5:
#                         print("GAME OVER")
#                         break
#         # continue
                    

                    

    
      

        
    

lothm_funcs.start(root)
root.mainloop()
