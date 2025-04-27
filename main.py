import tkinter as tk
import threading
import pyperclip
import keyboard
import time

class ClipboardManager:
    def __init__(self):
        self.history = []
        self.root = None
        self.listbox = None
        self.max_history = 20  # en fazla 20 öğe tut
        self.running = True

    def start_clipboard_listener(self):
        previous_text = ""
        while self.running:
            try:
                current_text = pyperclip.paste()
                if current_text != previous_text and current_text.strip() != "":
                    if current_text not in self.history:
                        self.history.insert(0, current_text)
                        if len(self.history) > self.max_history:
                            self.history.pop()
                    previous_text = current_text
            except Exception as e:
                print("Clipboard error:", e)
            time.sleep(0.5)

    def show_popup(self):
        if self.root is not None:
            return  # pencere zaten açık

        self.root = tk.Tk()
        self.root.title("Clipboard Manager")
        self.root.geometry("400x300")
        self.root.attributes("-topmost", True)

        self.listbox = tk.Listbox(self.root, font=("Arial", 12))
        self.listbox.pack(fill=tk.BOTH, expand=True)

        for item in self.history:
            self.listbox.insert(tk.END, item)

        self.listbox.bind("<Double-Button-1>", self.on_item_select)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.root.mainloop()

    def on_item_select(self, event):
        selection = self.listbox.curselection()
        if selection:
            selected_text = self.listbox.get(selection[0])
            pyperclip.copy(selected_text)
            self.root.destroy()
            self.root = None

    def on_close(self):
        self.root.destroy()
        self.root = None

    def start(self):
        threading.Thread(target=self.start_clipboard_listener, daemon=True).start()
        keyboard.add_hotkey('ctrl+shift+v', self.show_popup)
        print("Clipboard Manager çalışıyor... (CTRL+SHIFT+V ile açılır)")
        keyboard.wait()  # Programı açık tut

if __name__ == "__main__":
    manager = ClipboardManager()
    manager.start()
