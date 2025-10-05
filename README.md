#  Hybrid Steganography — Ultra Pro Max Edition

[![Release](https://img.shields.io/github/v/release/paarthkaringula2004/Hybrid_Stegnography)](https://github.com/paarthkaringula2004/Hybrid_Stegnography/releases)
[![License](https://img.shields.io/github/license/paarthkaringula2004/Hybrid_Stegnography)](LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/paarthkaringula2004/Hybrid_Stegnography)](https://github.com/paarthkaringula2004/Hybrid_Stegnography/issues)

---

##  About

**Hybrid Steganography** is a **secure and user-friendly GUI tool** to hide **text messages** inside **image (.png)** and **audio (.wav)** files. It combines multiple steganography techniques for **enhanced data concealment** while maintaining an intuitive interface.

---

## ⚙️ Features

- Hide and reveal **text messages** in **images** (`.png`) and **audio** (`.wav`).  
- Switch seamlessly between **image** and **audio** modes.  
- **Live preview** for images and audio filenames.  
- GUI built with **Tkinter + TTK Themes** for a modern interface.  
- Handles messages intelligently in audio files with **termination marker (`###`)**.  
- Clear workspace with one click for fresh operations.

---

##  Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/paarthkaringula2004/Hybrid_Stegnography.git


2. **Install dependencies:**

   ```bash
   pip install pillow pydub stegano ttkthemes
   ```

3. Ensure **ffmpeg** is installed and available in PATH, or keep `ffmpeg.exe` inside the `ffmpeg` folder.

4. **Run the application:**

   ```bash
   python Hybrid_Stegnography.py
   ```

> Or use the prebuilt executable `Hybrid_Stegnography.exe` from the [Releases page](https://github.com/paarthkaringula2004/Hybrid_Stegnography/releases).

---

##  Usage

1. **Open the application**.
2. Click **Switch Mode** to select `image` or `audio`.
3. Click **Open File** to select the carrier file (`.png` or `.wav`).
4. Enter the text message you want to hide.
5. Click **Hide Data** to embed your message.
6. Click **Reveal Data** to extract hidden messages.
7. Click **Clear All** to reset the workspace.

>  Ensure you use the software in a **safe environment**.

---

##  Example

```text
Mode: Image
Carrier file: cover.png
Message: "Secret mission details"
Output file: cover_stego.png

Mode: Audio
Carrier file: secret.wav
Message: "Confidential message"
Output file: secret_stego.wav
```

---

##  Notes

* Supports **only `.png` images** and **`.wav` audio files** in this version.
* Audio messages have a **size limit** based on carrier length.
* GUI theme: `equilux` via `ttkthemes`.
* Future releases may include **video support**, **encryption**, and more.



##  Contact / Support

* GitHub Issues: [Report bugs or request features](https://github.com/paarthkaringula2004/Hybrid_Stegnography/issues)
* Author: Paarth Karingula

*Made with ❤️ by Paarth – Cybersecurity & Ethical Hacking Enthusiast*

