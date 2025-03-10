import os
import glob
import tkinter as tk
from tkinter import filedialog, messagebox

def mapping_table(text):
    replacements = {
        '': 'и',
        '': 'Ѣ',
        '': 'Ѣ',
        '': 'Ч',
        '': 'Ѥ',
        'ꙑ': 'Ꙑ',
        '': 'Н',
        '': '҇',
        '': '̛',
        '': '҈',
        '': 'Ѣ',
        '': '҆',
        'ⷢ': '꙲',
        '': '́',
        '': '҄',
        '': 'ъ',
        'ⷮ': 'ᲀ',
        'ⷨ': 'ᲁ',
        'ⷬ': 'ꙮ',
        '⸱': '·',
        '꙼': '꙽',
        '': 'ѡ',
        'ⷣ': 'Ꙩ',
        'ⷯ': 'ⷰ',
        'ⷭ҇': 'ꙭ҇',
        '': 'Н',
        '': 'В',
        'ⷦ҇': 'Ꙧ҇',
        'ᲀ': 'Ꙩ',
        '': ':',
        'ꙗ': 'я',
        'ꙿ': '҃',
        '꙳': '·',
        '꙯': 'ѿ',
        'ꙵ': 'ѧ',
        'ꙶ': 'ѩ',
        'ꙻ': 'ъ',
        '': '·',
        'ъ': 'Чъ',
        'ⷣ': 'Ꙩ҆',
        'а': 'Ча',
        'ⷣ': 'ꙨѢ',
        'ⷮ': '҆ᲀ',
        'ⷯ': 'ⷰ҆',
        '': 'Чѡ',
        '': '¶',
        '': 'Ѥ',
        'Ч': 'ѡЧ',
        'ѧ': 'Чѧ',
        '': '⸰',
        '': 'Ѣ',
        '': 'ꙺ',
        '': 'Ю',
        '': 'ꙻ',
        'ⷤ': '',
        'ⸯ': '',
        'ꙁ': 'з',
        'ⷤ҆': '҆',
    }

    for old_char, new_char in replacements.items():
        text = text.replace(old_char, new_char)

    return text

def process_text(input_text):
    return mapping_table(input_text)

def process_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    txt_files = glob.glob(os.path.join(input_folder, '*.txt'))

    for input_file_path in txt_files:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            input_text = file.read()

        mapped_text = mapping_table(input_text)

        file_name = os.path.basename(input_file_path)
        output_file_path = os.path.join(output_folder, file_name)
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(mapped_text)

def paste_text_handler():
    input_text = input_box.get("1.0", tk.END).strip()
    if input_text:
        mapped_text = process_text(input_text)
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, mapped_text)
    else:
        messagebox.showwarning("Warning", "Please paste text to process.")

def select_folder_handler():
    input_folder = filedialog.askdirectory(title="Select Folder with Input Files")
    output_folder = filedialog.askdirectory(title="Select Folder for Output Files")

    if input_folder and output_folder:
        try:
            process_folder(input_folder, output_folder)
            messagebox.showinfo("Success", f"Files have been processed and saved to {output_folder}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please select both input and output folders.")


app = tk.Tk()
app.title("PUA Handling System for Cyrillomethodiana Text Corpus")


welcome_label = tk.Label(app, text="Welcome to the PUA Handling System for Cyrillomethodiana Text Corpus of Ancient OCS", wraplength=600, font=("Arial", 14))
welcome_label.pack(pady=10)


input_label = tk.Label(app, text="Paste your text below:")
input_label.pack(anchor="w", padx=10)

input_box = tk.Text(app, height=10, width=80)
input_box.pack(padx=10, pady=5)

submit_text_button = tk.Button(app, text="Submit", command=paste_text_handler)
submit_text_button.pack(pady=5)

output_label = tk.Label(app, text="Processed Text:")
output_label.pack(anchor="w", padx=10)

output_box = tk.Text(app, height=10, width=80)
output_box.pack(padx=10, pady=5)


folder_label = tk.Label(app, text="Convert an entire folder of text files:")
folder_label.pack(anchor="w", padx=10, pady=10)

convert_folder_button = tk.Button(app, text="Select Folders and Process", command=select_folder_handler)
convert_folder_button.pack(pady=5)


app.mainloop()
