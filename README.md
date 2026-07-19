<img width="1918" height="1015" alt="image" src="https://github.com/user-attachments/assets/69162b52-b079-4ed3-a81a-346caf38576a" />

<p align="center"><i>Finally, 100% accurate with Prefixes and Assimilation!</i></p>

## 💖 Linör

Linör is a minimal, soft, and powerful desktop transliteration and pronunciation system. It provides a clean, distraction-free environment to instantly convert complex scripts, romanize texts, and hear the written word across dozens of global language families.

## ✨ Features

* A smooth, dark purple aesthetic that is gentle on your eyes during long working sessions.
* Transliterates your text instantly in real-time as you type, completely fluidly.
* Organizes over 30 global scripts by geographic and linguistic families.
* Toggle custom linguistic styles, sentence case formatting, and dynamically convert numeric digits directly into fully written localized words.

## 😍 Downloads and releases

If you just want to run the app without messing with any code or terminals, you can grab the ready-to-use version!

1. Go to the "Releases" section on the right side of this GitHub page.
2. Download the latest version.
3. Run the installer, launch Linör, and transliterate away!

## 🌟 Setup and installation

### Prerequisites

Before running the application from source, make sure you have **Python** installed on your computer.

### 1. Clone the Repository

Open your terminal or command prompt and run:

```bash
git clone [https://github.com/AmethystNiita/Linor.git](https://github.com/AmethystNiita/Linor.git)
cd Linor

```

### 2. Install Dependencies

Run the following command to automatically pull all the required linguistic pipelines and engine modules:

```bash
pip install -r requirements.txt

```

### 3. Run the Application

Start Linör with:

```bash
python main.py

```

## 🛠️ Built with

Linör is powered by an incredible stack of open-source language models and UI frameworks:

* **CustomTkinter** - Modern, custom-themed desktop interface framework.
* **ifranlp** - Custom-tailored core linguistic processing, transliteration, and pronunciation library.
* **PyThaiNLP / LaoNLP / PyPinyin / PyKakasi / Num2Words** - Specialized regional tokenizers and phonetic translation layers.
* **Scikit-learn & Python-CRFsuite** - Sequential machine learning tagging for data structural accuracy.
* **Regex** - High-performance recursive Unicode sequence string handling.
