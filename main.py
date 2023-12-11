from dict import morse_dict
from tkinter import *
from tkinter import ttk
import winsound

# Translation Function
def translate(english_input):
    morse_sentence = []
    for letter in english_input:
        morse_text = morse_dict[letter]
        for i in morse_text:
            if i == "*":
                winsound.Beep(short_frequency, short_duration)
            elif i == "-":
                winsound.Beep(long_frequency, long_duration)
        morse_sentence.append(morse_text)
    output_field.insert(END, morse_sentence)
    return morse_sentence


# TKinter stuff

# Window
root = Tk()
root.title("English to Morse Translator")
root.config(padx=100, pady=50)

# Canvas
canvas = Canvas(width=600, height=400, highlightthickness=0)

# Label
translator_label = Label(text="English to Morse Translator", font=("Courier", 36, "bold"))
translator_label.grid(column=1, row=0)

# Input
user_input = Entry()
user_input.get()
user_input.grid(column=1, row=1)
user_input.configure(width=80)

# Translate Button
translate_button = Button(text="Translate", command=lambda: translate(user_input.get()))
translate_button.grid(column=1, row=3)

# Output
output_field = Text(width=80, height=10)
output_field.grid(column=1, row=2)

#Sound
short_frequency = 200
short_duration = 400

long_frequency = 300
long_duration = 1000


root.mainloop()