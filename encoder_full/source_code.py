import tkinter as tk
from tkinter import ttk
from base64 import b64encode, b64decode
import pyperclip

# Функція для шифрування методом Цезаря
def caesar_cipher(text, shift):
    result = []
    for letter in text:
        if letter.isalpha():
            is_upper = letter.isupper()  # Визначаємо, чи є літера в верхньому регістрі
            letter = letter.upper()  # Переводимо літеру у верхній регістр
            start, end = ord('А'), ord('Я')  # Значення початку та кінця діапазону українських великих літер
            if 'А' <= letter <= 'Я':  # Якщо літера - українська велика літера
                start, end = ord('А'), ord('Я')
            elif 'а' <= letter <= 'я':  # Якщо літера - українська мала літера
                start, end = ord('а'), ord('я')
            elif 'A' <= letter <= 'Z':  # Якщо літера - латинська велика літера
                start, end = ord('A'), ord('Z')
            elif 'a' <= letter <= 'z':  # Якщо літера - латинська мала літера
                start, end = ord('a'), ord('z')
            elif 'Ґ' <= letter <= 'Щ':  # Якщо літера - українська велика літера
                start, end = ord('Ґ'), ord('Щ')
            elif 'ґ' <= letter <= 'щ':  # Якщо літера - українська мала літера
                start, end = ord('ґ'), ord('щ')
            elif 'Ь' <= letter <= 'Я':  # Якщо літера - українська велика літера
                start, end = ord('Ь'), ord('Я')
            elif 'ь' <= letter <= 'я':  # Якщо літера - українська мала літера
                start, end = ord('ь'), ord('я')
            elif letter == 'І':  # Якщо літера - українська літера І
                start, end = ord('І'), ord('І')
            elif letter == 'i':  # Якщо літера - латинська літера i
                start, end = ord('i'), ord('i')
            elif letter == 'Є':  # Якщо літера - українська літера Є
                start, end = ord('Є'), ord('Є')
            elif letter == 'Ї':  # Якщо літера - українська літера Ї
                start, end = ord('Ї'), ord('Ї')
            elif letter == 'Ґ':  # Якщо літера - українська літера Ґ
                start, end = ord('Ґ'), ord('Ґ')

            new_letter = chr((ord(letter) - start + shift) % (end - start + 1) + start)  # Зсуваємо літеру
            result.append(new_letter if is_upper else new_letter.lower())  # Додаємо літеру у результуючий список
        else:
            result.append(letter)  # Якщо символ - не літера, додаємо його без змін

    return ''.join(result)  # Повертаємо результат у вигляді строки

# Функція для шифрування тексту
def encrypt():
    text = input_field.get()  # Отримуємо текст зі введеного поля
    if mode == "base64":  # Якщо обраний метод шифрування - Base64
        text = b64encode(text.encode("utf-8")).decode("utf-8")  # Кодуємо текст у формат Base64
    elif mode == "caesar":  # Якщо обраний метод шифрування - Цезаря
        text = caesar_cipher(text, 3)  # Застосовуємо шифр Цезаря з ключем 3

    output_field.config(state="normal")  # Розблоковуємо поле для виводу результату
    output_field.delete(0, tk.END)  # Очищуємо поле виводу
    output_field.insert(0, text)  # Вставляємо зашифрований текст у поле виводу
    output_field.config(state="readonly")  # Блокуємо поле виводу для редагування
    output_field.focus_set()  # Встановлюємо фокус на поле виводу
    copy_button.config(command=lambda: pyperclip.copy(text))  # Налаштовуємо кнопку "Копіювати" для копіювання тексту

# Функція для дешифрування тексту
def decrypt():
    text = input_field.get()  # Отримуємо текст зі введеного поля
    if mode == "base64":  # Якщо обраний метод шифрування - Base64
        text = b64decode(text).decode("utf-8")  # Декодуємо текст з формату Base64
    elif mode == "caesar":  # Якщо обраний метод шифрування - Цезаря
        text = caesar_cipher(text, -3)  # Застосовуємо шифр Цезаря з ключем -3 (для дешифрування)

    output_field.config(state="normal")  # Розблоковуємо поле для виводу результату
    output_field.delete(0, tk.END)  # Очищуємо поле виводу
    output_field.insert(0, text)  # Вставляємо дешифрований текст у поле виводу
    output_field.config(state="readonly")  # Блокуємо поле виводу для редагування
    output_field.focus_set()  # Встановлюємо фокус на поле виводу
    copy_button.config(command=lambda: pyperclip.copy(text))  # Налаштовуємо кнопку "Копіювати" для копіювання тексту

# Функція для оновлення методу шифрування
def update_mode(new_mode):
    global mode
    mode = new_mode

# Функція для очищення полів вводу та виводу
def clear_fields():
    input_field.delete(0, tk.END)  # Очищуємо поле вводу
    output_field.config(state="normal")  # Розблоковуємо поле для виводу результату
    output_field.delete(0, tk.END)  # Очищуємо поле виводу
    output_field.config(state="readonly")  # Блокуємо поле виводу для редагування

# Створення головного вікна програми
window = tk.Tk()
window.title("Шифрувальник")

window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
window.geometry("+%d+%d" % (x_coordinate, y_coordinate))

window.resizable(False, False)

frame = ttk.Frame(window)
frame.grid(row=0, column=0, padx=10, pady=10)

input_label = ttk.Label(frame, text="Введіть текст:")
input_label.grid(row=1, column=0, padx=5, pady=5)

input_field = ttk.Entry(frame)
input_field.grid(row=1, column=1, padx=5, pady=5)

output_label = ttk.Label(frame, text="Зашифрований текст:")
output_label.grid(row=2, column=0, padx=5, pady=5)

output_field = ttk.Entry(frame, state="readonly")
output_field.grid(row=2, column=1, padx=5, pady=5)

encrypt_button = ttk.Button(frame, text="Зашифрувати", command=encrypt)
encrypt_button.grid(row=3, column=0, columnspan=1, padx=5, pady=5)

decrypt_button = ttk.Button(frame, text="Розшифрувати", command=decrypt)
decrypt_button.grid(row=3, column=1, columnspan=1, padx=5, pady=5)

method_label = ttk.Label(frame, text="Метод шифрування:")
method_label.grid(row=4, column=0, padx=5, pady=5)

mode_switch_base64 = ttk.Radiobutton(frame, text="Base64", value="base64", command=lambda: update_mode("base64"))
mode_switch_base64.grid(row=5, column=0, padx=5, pady=5)

mode_switch_caesar = ttk.Radiobutton(frame, text="Шифр Цезаря", value="caesar", command=lambda: update_mode("caesar"))
mode_switch_caesar.grid(row=5, column=1, padx=5, pady=5)

mode = "base64"
mode_switch_base64.invoke()

copy_button = ttk.Button(frame, text="📋", command=lambda: pyperclip.copy(output_field.get()))
copy_button.grid(row=2, column=2)

clear_button = ttk.Button(frame, text="✖", command=clear_fields)
clear_button.grid(row=1, column=2)

style = ttk.Style()
style.configure("Rounded.TEntry", borderwidth=5, relief="ridge", padding=10)
style.configure("Rounded.TButton", borderwidth=5, relief="ridge", padding=10)

input_field.config(style="Rounded.TEntry")
output_field.config(style="Rounded.TEntry")
encrypt_button.config(style="Rounded.TButton")
decrypt_button.config(style="Rounded.TButton")
copy_button.config(style="Rounded.TButton")
clear_button.config(style="Rounded.TButton")

window.mainloop()
