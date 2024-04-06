import customtkinter
import tkinter
from tkinter import filedialog
import random
import string 
window = customtkinter.CTk()
window.title("Генератор паролей")
window.geometry('600x600')
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")
# Создаем поля для ввода длины и кол-ва паролей
customtkinter.CTkLabel(window, text = "Кол-во паролей:").place(x = 200, y=30)
e_count = customtkinter.CTkEntry(window, width = 50)
e_count.place(x = 300, y =30)
customtkinter.CTkLabel(window, text = "Длина паролей:").place(x = 200, y=60)
e_len = customtkinter.CTkEntry(window, width = 50)
e_len.place(x = 300, y =60)
chars = 'qwertyuiopasdfghjklzxcvbnm'
symbols = '!@#$%^&*'
numbers = '1234567890'
chars = list(chars + chars.upper()+symbols+numbers) 
def generate():
    count = int(e_count.get())
    length = int(e_len.get())
    passwords = []
    
    chosen_chars = ''
    if var_letters.get():
        chosen_chars += string.ascii_letters
    if var_digits.get():
        chosen_chars += string.digits
    if var_symbols.get():
        chosen_chars += '!@#$%^&*'
    
    if not chosen_chars:
        text_field.delete(0.0, customtkinter.END)  # Очистить текстовое поле
        text_field.insert(0.0, "Пожалуйста, выберите хотя бы один тип символов.")
    else:
        for _ in range(count):
            password = ''.join(random.choice(chosen_chars) for _ in range(length))
            passwords.append(password)
        text_field.delete(0.0, customtkinter.END)  # Очистить текстовое поле
        text_field.insert(0.0, "\n".join(passwords))
      


     
    
def clear():
    text_field.delete(0.0, customtkinter.END)

var_letters = customtkinter.IntVar()
var_digits = customtkinter.IntVar()
var_symbols = customtkinter.IntVar()

def save_to_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'a') as file:
            file.write(text_field.get("1.0", "end"))


# создание флажков и меток для выбора типа пароля
letters_checkbox = customtkinter.CTkCheckBox(window, text="Буквы", variable=var_letters)
letters_checkbox.grid(row=0, column=0, sticky='w')
digits_checkbox = customtkinter.CTkCheckBox(window, text="Цифры", variable=var_digits)
digits_checkbox.grid(row=1, column=0, sticky='w')
symbols_checkbox = customtkinter.CTkCheckBox(window, text="Спец. символы", variable=var_symbols)
symbols_checkbox.grid(row=2, column=0, sticky='w')
#Создаем кнопки, чтобы генерировать и стирать пароли
btn_clear = customtkinter.CTkButton(window, text = "Очистить",command = clear)
btn_clear.place(x =350, y =100)
btn_gen = customtkinter.CTkButton(window, text = "Сгенерировать",command=generate)
btn_gen.place(x =200, y =100)
btn_save = customtkinter.CTkButton(window, text="Добавить в файл", command=save_to_file)
btn_save.place(x=200, y=130)

text_field = customtkinter.CTkTextbox(window, width =500, height = 300)
text_field.place(x = 20, y = 170)
window.mainloop()