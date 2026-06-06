import ifranlp
import customtkinter
import regex as re

language = "Adlam"
style = "Standard"
itra = ifranlp.transliterate
ipro = ifranlp.pronunciate

category_languages = {
    "African": [
        "Adlam", "N'Ko"
    ],
    "Asian": [
        "Burmese (Beta)", "Chinese", "Khmer (Beta)", "Japanese", "Korean", "Thai"
    ],
    "Dravidian": [
        "Kannada", "Malayalam", "Tamil"
    ],
    "Indic": [
        "Hindi", "Punjabi"
    ],
    "Indo-European": [
        "Armenian", "Belarusian", "Bulgarian", "Greek",
        "Macedonian", "Russian", "Serbian", "Tajik",
        "Ukrainian"
    ],
    "Kartvelian": [
        "Georgian (Asomtavruli)", "Georgian (Mkhedruli)",
        "Georgian (Nuskhuri)"
    ],
    "Mongolic": [
        "Buryat", "Mongolian"
    ],
    "Semitic": [
        "Amharic", "Arabic", "Aramaic (Syriac)", "Hebrew"
    ],
    "Turkic": [
        "Kazakh", "Kyrgyz", "Uyghur"
    ]
}

language_styles = {
    "Adlam": ["Standard"],
    "Amharic": ["Standard"],
    "Arabic": ["Standard", "Casual", "Formal"],
    "Aramaic (Syriac)": ["Standard"],
    "Armenian": ["Standard"],
    "Belarusian": ["Standard"],
    "Bulgarian": ["Standard"],
    "Buryat": ["Standard"],
    "Burmese (Beta)": ["Standard"],
    "Chinese": ["Standard"],
    "French": ["Standard", "Casual"],
    "Georgian (Asomtavruli)": ["Standard"],
    "Georgian (Mkhedruli)": ["Standard"],
    "Georgian (Nuskhuri)": ["Standard"],
    "German": ["Standard", "Casual"],
    "Greek": ["Standard"],
    "Hebrew": ["Standard"],
    "Hindi": ["Standard"],
    "Japanese": ["Standard", "Hepburn", "Kunrei", "Passport"],
    "Kannada": ["Standard", "Casual", "Formal"],
    "Kazakh": ["Standard"],
    "Khmer (Beta)": ["Standard"],
    "Korean": ["Standard"],
    "Kyrgyz": ["Standard"],
    "Macedonian": ["Standard"],
    "Malayalam": ["Standard", "Casual", "Formal"],
    "Mongolian": ["Standard"],
    "N'Ko": ["Standard"],
    "Punjabi": ["Standard"],
    "Russian": ["Standard"],
    "Serbian": ["Standard"],
    "Tajik": ["Standard"],
    "Tamil": ["Standard", "Casual", "Formal"],
    "Thai": ["Standard"],
    "Ukrainian": ["Standard"],
    "Uyghur": ["Standard"]
}

languages_with_number_to_word = ["Arabic", "French", "German", "Hebrew", "Japanese", "Russian", "Thai"]
customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Linör")
        self.geometry(f"{1100}x{580}")
        self.iconbitmap("linor-logo.ico")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.live_mode_on = True

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(11, weight=1)

        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Linör",
                                                 font=customtkinter.CTkFont(family="Segoe UI", size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.text_box = customtkinter.CTkTextbox(self, wrap="word",
                                                 font=customtkinter.CTkFont(family="Segoe UI", size=20))
        self.text_box.grid(row=0, column=1, padx=(20, 10), pady=(10, 10), sticky="nsew")
        self.text_box.bind("<KeyRelease>", self.live_transliterate)

        self.text_box_result = customtkinter.CTkTextbox(self, wrap="word",
                                                        font=customtkinter.CTkFont(family="Segoe UI", size=20,
                                                                                   weight="bold"), state="disabled")
        self.text_box_result.grid(row=0, column=2, padx=(10, 20), pady=(10, 10), sticky="nsew")


        self.catagory_label = customtkinter.CTkLabel(self.sidebar_frame, text="Catagory")
        self.catagory_label.grid(row=1, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.combobox_1 = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                      values=list(category_languages.keys()),
                                                      fg_color="#7F00CD", button_color="#6700AB",
                                                      button_hover_color="#56008C",
                                                      command=self.update_language_options)
        self.combobox_1.grid(row=2, column=0, padx=20, pady=10)

        self.language_label = customtkinter.CTkLabel(self.sidebar_frame, text="Language")
        self.language_label.grid(row=3, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.combobox_2 = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[], fg_color="#7F00CD",
                                                      button_color="#6700AB", button_hover_color="#56008C",
                                                      command=self.on_language_change)
        self.combobox_2.grid(row=4, column=0, padx=20, pady=10)

        self.style_label = customtkinter.CTkLabel(self.sidebar_frame, text="Style")
        self.style_label.grid(row=5, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.style_combobox = customtkinter.CTkOptionMenu(self.sidebar_frame, values=[], fg_color="#7F00CD",
                                                          button_color="#6700AB", button_hover_color="#56008C",
                                                          command=self.on_style_change)
        self.style_combobox.grid(row=6, column=0, padx=20, pady=10)

        self.case_label = customtkinter.CTkLabel(self.sidebar_frame, text="Capitalization")
        self.case_label.grid(row=7, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

        self.case_combobox = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                         values=["As is", "Lowercase", "Uppercase", "Sentence case", "Title case"],
                                                         fg_color="#7F00CD",
                                                         button_color="#6700AB",
                                                         button_hover_color="#56008C",
                                                         command=self.on_case_change
                                                         )
        self.case_combobox.grid(row=8, column=0, padx=20, pady=10)
        self.case_combobox.set("As Is")  # Default to As Is

        self.numbers_as_words_switch = customtkinter.CTkSwitch(self.sidebar_frame,
                                                               progress_color="#7F00CD",
                                                               text="Numbers as Words",
                                                               command=self.on_number_change)
        self.numbers_as_words_switch.grid(row=9, column=0, padx=20, pady=10)
        self.numbers_as_words_switch.deselect()

        self.live_mode_switch = customtkinter.CTkSwitch(self.sidebar_frame, progress_color="#7F00CD",
                                                        text="Live Mode", command=self.change_live_mode)
        self.live_mode_switch.grid(row=10, column=0, padx=20, pady=10)
        self.live_mode_switch.select()

        self.update_language_options("African")

        self.transliterate_button = customtkinter.CTkButton(self.sidebar_frame, text="Transliterate!", width=120,
                                                            height=50, fg_color="#7F00CD", hover_color="#56008C",
                                                            command=self.transliterate)
        self.transliterate_button.grid(row=12, column=0, padx=20, pady=(10, 10))

        self.style_label = customtkinter.CTkLabel(self.sidebar_frame, text="2.1.1")
        self.style_label.grid(row=13, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")

    def on_language_change(self, choice):
        global language
        language = choice
        self.update_style_options()
        self.live_transliterate(None)

    def on_style_change(self, choice):
        global style
        style = choice
        self.live_transliterate(None)

    def on_number_change(self):
        self.live_transliterate(None)

    def on_case_change(self, choice):
        self.live_transliterate(None)

    def update_language_options(self, selected_category):
        langs = category_languages.get(selected_category, [])
        self.combobox_2.configure(values=langs)
        if langs:
            self.combobox_2.set(langs[0])
            self.on_language_change(langs[0])

    def update_style_options(self):
        global language
        styles = language_styles.get(language, ["Standard"])
        self.style_combobox.configure(values=styles)
        if styles:
            self.style_combobox.set(styles[0])
            self.on_style_change(styles[0])

        if len(styles) <= 1:
            self.style_combobox.configure(state="disabled", fg_color="#404040", button_color="#363636")
        else:
            self.style_combobox.configure(state="normal", fg_color="#7F00CD", button_color="#6700AB")
        if language in languages_with_number_to_word:
            self.numbers_as_words_switch.configure(state="normal", text_color="#DCE4EE")
        else:
            self.numbers_as_words_switch.deselect()
            self.numbers_as_words_switch.configure(state="disabled", text_color="#404040")

    def change_live_mode(self):
        self.live_mode_on = self.live_mode_switch.get()

    def live_transliterate(self, event):
        if self.live_mode_on:
            self.transliterate()

    def transliterate(self):
        text = self.text_box.get("1.0", "end-1c")
        selected_style = self.style_combobox.get().lower()
        number_style = "words" if self.numbers_as_words_switch.get() == 1 else "keep"
        case_style = self.case_combobox.get().lower()

        transliteration_functions = {
            "Adlam": itra.adlam.transliterate_adlam,
            "Amharic": itra.amharic.transliterate_amharic,
            "Arabic": itra.arabic.transliterate_arabic,
            "Aramaic (Syriac)": itra.aramaic.transliterate_syriac,
            "Armenian": itra.armenian.transliterate_armenian,
            "Belarusian": itra.cyrillic.transliterate_belarusian,
            "Bulgarian": itra.cyrillic.transliterate_bulgarian,
            "Buryat": itra.cyrillic.transliterate_buryat,
            "Burmese (Beta)": itra.burmese.transliterate_burmese,
            "Chinese": itra.chinese.transliterate_chinese,
            "French": ipro.french.pronunciate_french,
            "Georgian (Asomtavruli)": itra.georgian.transliterate_asomtavruli,
            "Georgian (Mkhedruli)": itra.georgian.transliterate_mkhedruli,
            "Georgian (Nuskhuri)": itra.georgian.transliterate_nuskhuri,
            "German": ipro.german.pronunciate_german,
            "Greek": itra.greek.transliterate_greek,
            "Hebrew": itra.hebrew.transliterate_hebrew,
            "Hindi": itra.hindi.transliterate_hindi,
            "Japanese": itra.japanese.transliterate_japanese,
            "Kannada": itra.kannada.transliterate_kannada,
            "Kazakh": itra.cyrillic.transliterate_kazakh,
            "Khmer (Beta)": itra.khmer.transliterate_khmer,
            "Korean": itra.korean.transliterate_korean,
            "Kyrgyz": itra.cyrillic.transliterate_kyrgyz,
            "Macedonian": itra.cyrillic.transliterate_macedonian,
            "Malayalam": itra.malayalam.transliterate_malayalam,
            "Mongolian": itra.cyrillic.transliterate_mongolian,
            "N'Ko": itra.nko.transliterate_nko,
            "Punjabi": itra.punjabi.transliterate_punjabi,
            "Russian": itra.cyrillic.transliterate_russian,
            "Serbian": itra.cyrillic.transliterate_serbian,
            "Tajik": itra.cyrillic.transliterate_tajik,
            "Tamil": itra.tamil.transliterate_tamil,
            "Thai": itra.thai.thai_syllables,
            "Ukrainian": itra.cyrillic.transliterate_ukrainian,
            "Uyghur": itra.uyghur.transliterate_uyghur,
        }

        if language in transliteration_functions:
            transliteration_func = transliteration_functions[language]

            kwargs = {}
            if hasattr(transliteration_func, '__code__') and 'style' in transliteration_func.__code__.co_varnames:
                kwargs['style'] = selected_style

            if language in languages_with_number_to_word and 'number_style' in transliteration_func.__code__.co_varnames:
                kwargs['number_style'] = number_style

            transliterated_text = transliteration_func(text, **kwargs)

            if case_style == 'lowercase':
                transliterated_text = transliterated_text.lower()
            elif case_style == 'uppercase':
                transliterated_text = transliterated_text.upper()
            elif case_style == 'title case':
                transliterated_text = transliterated_text.title()
            elif case_style == 'sentence case':
                temp_text = transliterated_text

                if temp_text:
                    m = re.search(r"^(\s*)(?:['’ʼʾʿ])*(\p{L})", temp_text)
                    if m:
                        idx = m.start(2)
                        temp_text = temp_text[:idx] + temp_text[idx].upper() + temp_text[idx + 1:]

                transliterated_text = re.sub(
                    r"([.?!·\n])(\s*)((?:[^\p{L}]|['’ʼʾʿ])*)(\p{L})",
                    lambda m: m.group(1) + m.group(2) + m.group(3) + m.group(4).upper(),
                    temp_text
                )

            else: # 'as is'
                transliterated_text = transliterated_text

            self.text_box_result.configure(state="normal")
            self.text_box_result.delete('1.0', 'end')
            self.text_box_result.insert('1.0', transliterated_text)
            self.text_box_result.configure(state="disabled")

app = App()
app.mainloop()