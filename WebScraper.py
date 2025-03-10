import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog, messagebox


def scrape_and_save_text():
    url = url_input.get().strip()
    if not url:
        messagebox.showwarning("Warning", "Please paste a valid URL.")
        return

    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            text_content = soup.get_text(separator='\n')

            file_path = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt")],
                title="Save the extracted text"
            )

            if file_path:
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(text_content)
                messagebox.showinfo("Success", f"Content successfully saved to {file_path}")
            else:
                messagebox.showwarning("Warning", "No save location selected. Operation cancelled.")

        else:
            messagebox.showerror("Error", f"Failed to retrieve content from {url}. Status code: {response.status_code}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


app = tk.Tk()
app.title("Web Scraper")

welcome_label = tk.Label(app, text="Web Scraping Tool", font=("Arial", 16, "bold"), fg="#2E8B57")
welcome_label.pack(pady=10)

instruction_label = tk.Label(
    app,
    text="If you wish to web scrape text from the internet, please paste the link below:",
    font=("Arial", 12),
    wraplength=400,
    justify="center"
)
instruction_label.pack(pady=5)

url_input = tk.Entry(app, width=50, font=("Arial", 12))
url_input.pack(pady=5)

submit_button = tk.Button(
    app,
    text="Submit",
    command=scrape_and_save_text,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049"
)
submit_button.pack(pady=10)

app.mainloop()
