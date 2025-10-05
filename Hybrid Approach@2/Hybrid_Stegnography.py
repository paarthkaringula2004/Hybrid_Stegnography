"""
Hybrid Steganography — Ultra Pro Max^1000000 Edition
Author: Paarth
Version: Ultimate Edition (2025)
Requirements:
    pip install pillow pydub stegano ttkthemes
    ffmpeg installed and available in PATH
"""

import sys, os
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from pydub import AudioSegment
from stegano import lsb
from ttkthemes import ThemedTk

AudioSegment.converter = "ffmpeg/ffmpeg.exe"


if hasattr(sys, "_MEIPASS"):
    ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg.exe")
else:
    ffmpeg_path = os.path.join(os.path.dirname(__file__), "ffmpeg.exe")
AudioSegment.converter = ffmpeg_path


# -----------------------------------
# Main App Class
# -----------------------------------
class HybridStegApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hybrid Steganography ~Paarth")
        self.root.geometry("1050x600")
        self.root.resizable(False, False)

        self.mode = "image"
        self.filename = None
        self.secret_img = None

        self.setup_style()
        self.build_ui()

    # -----------------------------------
    # Custom Style
    # -----------------------------------
    def setup_style(self):
        self.bg_color = "#0e0e10"
        self.accent_color = "#00FFFF"
        self.text_color = "#E0E0E0"
        self.panel_bg = "#16171a"

        self.root.configure(bg=self.bg_color)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TButton",
            font=("Segoe UI", 11, "bold"),
            background=self.accent_color,
            foreground="black",
            padding=6,
        )
        style.map(
            "TButton",
            background=[("active", "#00e6e6")],
            relief=[("pressed", "sunken")],
        )
        style.configure("TLabel", background=self.bg_color, foreground=self.text_color)
        style.configure("Header.TLabel", font=("Orbitron", 20, "bold"), foreground="#00FFFF")

    # -----------------------------------
    # Build UI Layout
    # -----------------------------------
    def build_ui(self):
        # Title Bar
        title = ttk.Label(
            self.root,
            text="🧬 HYBRID STEGANOGRAPHY ~Alpha_Hax",
            style="Header.TLabel",
            anchor="center",
        )
        title.pack(fill=X, pady=10)

        subtitle = Label(
            self.root,
            text="Hide text inside images (.png) or audio (.wav) | Mind-Blowing Hybrid SteganoTech",
            bg=self.bg_color,
            fg="#888",
            font=("Segoe UI", 10),
        )
        subtitle.pack()

        # Panels Layout
        container = Frame(self.root, bg=self.bg_color)
        container.pack(padx=20, pady=20, fill=BOTH, expand=True)

        self.build_left_panel(container)
        self.build_center_panel(container)
        self.build_right_panel(container)

        # Status Bar
        self.status = StringVar(value="💡 Ready")
        Label(
            self.root,
            textvariable=self.status,
            bg=self.bg_color,
            fg="#00FFFF",
            font=("Consolas", 10, "italic"),
            anchor="w",
        ).pack(fill=X, pady=(10, 5), padx=10)

    # -----------------------------------
    # Left Panel — File Preview
    # -----------------------------------
    def build_left_panel(self, parent):
        left = Frame(parent, bg=self.panel_bg, relief="ridge", bd=2)
        left.pack(side=LEFT, padx=10, fill=Y)

        Label(left, text="📁 File Preview", fg="#00FFFF", bg=self.panel_bg, font=("Orbitron", 12, "bold")).pack(pady=10)

        self.preview_frame = Frame(left, bg="black", width=320, height=280)
        self.preview_frame.pack(padx=10, pady=10)

        self.preview_label = Label(self.preview_frame, text="No file selected", bg="black", fg="white", font=("Segoe UI", 12, "bold"))
        self.preview_label.place(relx=0.5, rely=0.5, anchor="center")

        self.filename_label = Label(left, text="File: None", fg="white", bg=self.panel_bg, font=("Consolas", 9))
        self.filename_label.pack(pady=5)

    # -----------------------------------
    # Center Panel — Text Area
    # -----------------------------------
    def build_center_panel(self, parent):
        center = Frame(parent, bg="#f0f0f0", relief="ridge", bd=2)
        center.pack(side=LEFT, padx=10, fill=Y)

        Label(center, text="🧠 Message (text)", bg="#f0f0f0", fg="black", font=("Segoe UI", 11, "bold")).pack(pady=5)

        self.text = Text(center, font=("Consolas", 11), wrap="word", width=38, height=20, bd=0)
        self.text.pack(padx=10, pady=5)

        scrollbar = Scrollbar(center, command=self.text.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.text.configure(yscrollcommand=scrollbar.set)

    # -----------------------------------
    # Right Panel — Controls
    # -----------------------------------
    def build_right_panel(self, parent):
        right = Frame(parent, bg=self.panel_bg, relief="ridge", bd=2)
        right.pack(side=LEFT, padx=10, fill=Y)

        self.mode_label = Label(right, text=f"Mode: {self.mode.upper()}", bg=self.panel_bg, fg="#00FFFF", font=("Orbitron", 12, "bold"))
        self.mode_label.pack(pady=(10, 20))

        buttons = [
            ("🔄 Switch Mode", self.switch_mode),
            ("📂 Open File", self.open_file),
            ("🧩 Hide Data", self.hide_data),
            ("🔍 Reveal Data", self.reveal_data),
            ("💾 Save Hidden File As...", self.save_hidden_file),
            ("🧹 Clear All", self.clear_all),
        ]

        for text, cmd in buttons:
            b = ttk.Button(right, text=text, command=cmd)
            b.pack(pady=8)

    # -----------------------------------
    # Utility Methods
    # -----------------------------------
    def set_status(self, msg):
        self.status.set(f"💡 {msg}")
        self.root.update_idletasks()

    def clear_preview(self):
        for w in self.preview_frame.winfo_children():
            w.destroy()
        self.preview_label = Label(self.preview_frame, text="No file selected", bg="black", fg="white")
        self.preview_label.place(relx=0.5, rely=0.5, anchor="center")

    # -----------------------------------
    # Core Functionalities
    # -----------------------------------
    def switch_mode(self):
        self.mode = "audio" if self.mode == "image" else "image"
        self.mode_label.config(text=f"Mode: {self.mode.upper()}")
        self.clear_all()
        self.set_status(f"Switched to {self.mode} mode")

    def open_file(self):
        types = (
            [("PNG Images", "*.png"), ("All files", "*.*")]
            if self.mode == "image"
            else [("WAV Audio", "*.wav"), ("All files", "*.*")]
        )
        file = filedialog.askopenfilename(title="Select File", filetypes=types)
        if not file:
            return
        self.filename = file
        self.filename_label.config(text=f"File: {os.path.basename(file)}")
        self.set_status(f"Loaded: {file}")

        # Image preview
        if self.mode == "image":
            img = Image.open(file)
            img.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(img)
            self.clear_preview()
            lbl = Label(self.preview_frame, image=photo)
            lbl.image = photo
            lbl.place(relx=0.5, rely=0.5, anchor="center")
        else:
            self.clear_preview()
            self.preview_label.config(text=f"🎵 {os.path.basename(file)}")

    def hide_data(self):
        msg = self.text.get("1.0", END).strip()
        if not self.filename or not msg:
            messagebox.showerror("Error", "Please select a file and enter a message.")
            return

        if self.mode == "image":
            try:
                stego = lsb.hide(self.filename, msg)
                out = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG", "*.png")])
                if out:
                    stego.save(out)
                    self.set_status(f"Hidden message saved to {out}")
                    messagebox.showinfo("Success", f"Hidden message saved:\n{out}")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            try:
                audio = AudioSegment.from_file(self.filename)
                frames = bytearray(audio._data)
                message_bytes = msg.encode() + b"###"

                if len(message_bytes) * 8 > len(frames):
                    messagebox.showerror("Error", "Message too long for this audio file.")
                    return

                bit_index = 0
                for i in range(len(frames)):
                    if bit_index < len(message_bytes) * 8:
                        byte_index = bit_index // 8
                        bit_pos = 7 - (bit_index % 8)
                        message_bit = (message_bytes[byte_index] >> bit_pos) & 1
                        frames[i] = (frames[i] & 0xFE) | message_bit
                        bit_index += 1

                hidden_audio = audio._spawn(bytes(frames))
                out = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV", "*.wav")])
                if out:
                    hidden_audio.export(out, format="wav")
                    self.set_status(f"Hidden audio saved: {out}")
                    messagebox.showinfo("Success", f"Hidden audio saved:\n{out}")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def reveal_data(self):
        if not self.filename:
            messagebox.showerror("Error", "Select a file first.")
            return
        self.text.delete("1.0", END)

        if self.mode == "image":
            try:
                hidden = lsb.reveal(self.filename)
                if hidden:
                    self.text.insert(END, hidden)
                    self.set_status("Message revealed from image")
                else:
                    messagebox.showwarning("No Message", "No hidden message found.")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            try:
                audio = AudioSegment.from_file(self.filename)
                frames = bytearray(audio._data)
                message_bits = []
                bit_acc = 0
                count = 0

                for b in frames:
                    bit_acc = (bit_acc << 1) | (b & 1)
                    count += 1
                    if count == 8:
                        message_bits.append(bit_acc)
                        bit_acc = 0
                        count = 0
                        if message_bits[-3:] == [35, 35, 35]:
                            break

                message_bytes = bytes(message_bits[:-3])
                text = message_bytes.decode("utf-8")
                self.text.insert(END, text)
                self.set_status("Message revealed from audio")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def save_hidden_file(self):
        messagebox.showinfo("Info", "Hidden file is already saved during the process!")

    def clear_all(self):
        self.text.delete("1.0", END)
        self.clear_preview()
        self.filename_label.config(text="File: None")
        self.filename = None
        self.set_status("Cleared all fields")


# -----------------------------------
# Main Execution
# -----------------------------------
if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    app = HybridStegApp(root)
    root.mainloop()
