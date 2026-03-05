import tkinter as tk
import random
import lothm_words

attempts = 6

def start(root):
    global attempts

    word = lothm_words.char_fromapi()

    random_word = word["name"]
    print(f"NOMBRE DESDE API: {random_word}")
    list_random_word = list(random_word)
    unknown_word = ["_" for _ in list_random_word]

    # word current state ("_ _ _ _ _ _")
    text_area = tk.Entry(root, font=("Ringbearer", 20), fg="white", bg="black", justify="center", borderwidth=0)
    text_area.place(x=400, y=50, anchor="center")
    text_area.insert(0, "".join(unknown_word))
    
    # --- PLAYER ENTRY (input letra)
    player_entry_message = tk.Entry(root, font=("Ringbearer", 30), fg="white", bg="black", justify="center", borderwidth=0)
    player_entry_message.place(x=200, y=100, anchor="center")
    player_entry_message.insert(0, "Insert a letter: ")
    player_entry = tk.Entry(root, font=("Ringbearer", 20), fg="white", bg="black", justify="center", width=1)
    player_entry.place(x=400, y=100, anchor="center")
    player_entry.focus()

    # --- MESSAGE AREA (mensajes)
    message_area = tk.Entry(root, font=("Ringbearer", 20), fg="white", bg="black", justify="center", borderwidth=0, width=40)
    message_area.place(x=400, y=150, anchor="center")

    # --- ALPHABET BOX (letras disponibles)
    alphabet_box = tk.Text(root, font=("Ringbearer", 20), fg="white", bg="black", height=1,width=46, borderwidth=0)
    alphabet_box.place(x=400, y=200, anchor="center")
    for letter in lothm_words.alphabet_max:
        alphabet_box.insert("end", letter + " ")  
    alphabet_box.config(state="disabled")

    # --- FUNCIÓN PARA MARCAR LETRAS
    def mark_letter(letter, color):
        alphabet_box.config(state="normal")  # abrir para modificar
        start = "1.0"
        while True:
            # Buscar letra en todo el contenido
            pos = alphabet_box.search(letter, start, stopindex="end")
            if not pos:
                break
            end_pos = f"{pos}+1c"
            alphabet_box.tag_add(letter, pos, end_pos)
            alphabet_box.tag_config(letter, foreground=color)
            start = end_pos
        alphabet_box.config(state="disabled")  # bloquear nuevamente

    # --- CHECK LETTER
    def check_letter(event=None):
        global attempts
        player_input = player_entry.get().lower()
        player_entry.delete(0, tk.END)

        if len(player_input) != 1 or not player_input.isalpha():
            message_area.delete(0, tk.END)
            message_area.insert(0, "INSERT A VALID LETTER")
            return

        if player_input in list_random_word:
            message_area.delete(0, tk.END)
            message_area.insert(0, f"OBTUVISTE '{player_input}'")
            for index, letter in enumerate(list_random_word):
                if player_input == letter:
                    unknown_word[index] = player_input
            text_area.delete(0, tk.END)
            text_area.insert(0, "".join(unknown_word))
            mark_letter(player_input.upper(), "green")
            if "_" not in unknown_word:
                print(f"Haz ganado con {unknown_word}")
                win(unknown_word)
        else:
            attempts -= 1
            message_area.delete(0, tk.END)
            message_area.insert(0, f"WRONG, {attempts} LEFT")
            mark_letter(player_input.upper(), "red")
            if attempts <= 0:
                message_area.delete(0, tk.END)
                message_area.insert(0, "HAZ PERDIDO, JUEGO TERMINADO!")
                player_entry.config(state="disabled")

    # --- BOTÓN
    button_check_letter = tk.Button(root, text="CHECK LETTER", font=("Ringbearer", 15), command=check_letter)
    button_check_letter.place()

    def win(word):
        pass


    # --- BIND ENTER KEY
    root.bind("<Return>", check_letter)