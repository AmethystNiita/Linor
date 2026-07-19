<img width="1918" height="1015" alt="image" src="https://github.com/user-attachments/assets/69162b52-b079-4ed3-a81a-346caf38576a" />

<p align="center"><i>Finally, 100% accurate with Prefixes and Assimilation!</i></p>

## 💖 Linör

Linör is a minimal, and soft desktop transliteration and pronunciation app. It provides a clean environment to convert scripts, romanize texts, and see the written word across many language families.

## ✨ Features

* A smooth, dark purple aesthetic that is gentle on your eyes.
* Transliterates your text in real-time as you type.
* Organizes over 30 global scripts by geographic and linguistic families.
* Toggle custom linguistic styles, sentence case formatting, and convert numbers into written words.

## 😍 Downloads and releases

If you just want to run the app without messing with any code or terminals, you can download the ready-to-use version!

1. Go to the "Releases" section on the right side of this GitHub page.
2. Download the latest version.
3. Run the installer and launch Linör.

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

Linör is powered by open-source language NLP toolkits and UI frameworks:

* **CustomTkinter** - Modern, custom-themed desktop interface framework.
* **ifranlp** - My own custom library for language processing, transliteration, and pronunciation.
* **PyThaiNLP / LaoNLP / PyPinyin / PyKakasi / Num2Words** - Specialized regional tokenizers and phonetic translation layers.
* **Scikit-learn & Python-CRFsuite** - Sequential machine learning tagging for data structural accuracy.
* **Regex** - High-performance recursive Unicode sequence string handling.
