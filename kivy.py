# 1. Force the mobile window simulation profile right at the start
from kivy.config import Config

Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '640')
Config.set('graphics', 'resizable', False)

import sys
import regex as re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.switch import Switch
from kivy.uix.scrollview import ScrollView

# Import your incredibly powerful library!
import ifranlp

# --- Your exact data structures preserved perfectly ---
version_number = "2.1.4"
itra = ifranlp.transliterate
ipro = ifranlp.pronunciate

category_languages = {
    "African": ["Adlam", "N'Ko"],
    "Asian": ["Baybayin", "Burmese", "Chinese", "Khmer", "Japanese", "Korean", "Thai"],
    "Dravidian": ["Kannada", "Malayalam", "Tamil"],
    "Indic": ["Hindi", "Punjabi"],
    "Indo-European": [
        "Armenian", "Belarusian", "Bulgarian", "Greek",
        "Macedonian", "Russian", "Serbian", "Tajik",
        "Ukrainian"
    ],
    "Kartvelian": ["Asomtavruli", "Mkhedruli", "Nuskhuri"],
    "Mongolic": ["Buryat", "Mongolian"],
    "Semitic": ["Amharic", "Arabic", "Hebrew", "Syriac"],
    "Turkic": ["Kazakh", "Kyrgyz", "Uyghur"]
}

language_styles = {
    "Asomtavruli": ["Standard"], "Mkhedruli": ["Standard"], "Nuskhuri": ["Standard"],
    "Adlam": ["Standard"], "Amharic": ["Standard"],
    "Arabic": ["Standard", "ASCII", "Casual", "Formal"], "Armenian": ["Standard"],
    "Baybayin": ["Standard"], "Belarusian": ["Standard"], "Bulgarian": ["Standard"],
    "Buryat": ["Standard"], "Burmese": ["Standard"], "Chinese": ["Standard"],
    "French": ["Standard", "Casual"], "German": ["Standard", "Casual"],
    "Greek": ["Standard"], "Hebrew": ["Standard"], "Hindi": ["Standard"],
    "Japanese": ["Standard", "Hepburn", "Kunrei", "Passport"],
    "Kannada": ["Standard", "Casual", "Formal"], "Kazakh": ["Standard"],
    "Khmer": ["Standard"], "Korean": ["Standard"], "Kyrgyz": ["Standard"],
    "Macedonian": ["Standard"], "Malayalam": ["Standard", "Casual", "Formal"],
    "Mongolian": ["Standard"], "N'Ko": ["Standard"], "Punjabi": ["Standard"],
    "Russian": ["Standard"], "Serbian": ["Standard"], "Syriac": ["Standard"],
    "Tajik": ["Standard"], "Tamil": ["Standard", "Casual", "Formal"],
    "Thai": ["Standard"], "Ukrainian": ["Standard"], "Uyghur": ["Standard"]
}

languages_with_number_to_word = ["Arabic", "French", "German", "Hebrew", "Japanese", "Russian", "Thai"]
languages_with_prefix = ["Arabic"]


class LinorMobileScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 10
        self.spacing = 8

        # Track states internally
        self.current_category = "African"
        self.current_language = "Adlam"

        # --- TITLE BAR ---
        self.add_widget(Label(text="Linör Mobile", font_size='20sp', bold=True, size_hint_y=None, height=40))

        # --- TEXT INTERFACE (Top Input, Bottom Output) ---
        self.input_box = TextInput(hint_text="Type here to transliterate...", multiline=True, font_size='16sp')
        # Kivy's equivalent to KeyRelease event binding
        self.input_box.bind(text=self.on_text_type)
        self.add_widget(self.input_box)

        self.output_box = TextInput(hint_text="Result will appear here...", readonly=True, font_size='16sp', bold=True)
        self.add_widget(self.output_box)

        # --- CONFIGURATION BAR (Scrollable so it stays tiny on mobile screens) ---
        config_scroll = ScrollView(size_hint_y=None, height=220)
        config_layout = GridLayout(cols=2, spacing=10, size_hint_y=None)
        config_layout.bind(minimum_height=config_layout.setter('height'))

        # 1. Category Selector (Dropdown / Spinner)
        config_layout.add_widget(Label(text="Category:", halign='left'))
        self.category_spinner = Spinner(text="African", values=list(category_languages.keys()))
        self.category_spinner.bind(text=self.change_category)
        config_layout.add_widget(self.category_spinner)

        # 2. Language Selector
        config_layout.add_widget(Label(text="Language:"))
        self.language_spinner = Spinner(text="Adlam", values=category_languages["African"])
        self.language_spinner.bind(text=self.change_language)
        config_layout.add_widget(self.language_spinner)

        # 3. Capitalization Selector
        config_layout.add_widget(Label(text="Capitalization:"))
        self.case_spinner = Spinner(text="As is",
                                    values=["As is", "Lowercase", "Uppercase", "Sentence case", "Title case"])
        self.case_spinner.bind(text=self.trigger_transliteration)
        config_layout.add_widget(self.case_spinner)

        # 4. Dynamic Style Selector
        self.style_label = Label(text="Style:")
        self.style_spinner = Spinner(text="Standard", values=["Standard"])
        self.style_spinner.bind(text=self.trigger_transliteration)
        config_layout.add_widget(self.style_label)
        config_layout.add_widget(self.style_spinner)

        # 5. Switches Layout (Numbers, Prefixes, Assimilation, Live Mode)
        config_layout.add_widget(Label(text="Numbers:"))
        self.num_switch = Switch(active=False)
        self.num_switch.bind(active=self.trigger_transliteration)
        config_layout.add_widget(self.num_switch)

        self.prefix_label = Label(text="Prefixes:")
        self.prefix_switch = Switch(active=False)
        self.prefix_switch.bind(active=self.trigger_transliteration)
        config_layout.add_widget(self.prefix_label)
        config_layout.add_widget(self.prefix_switch)

        self.assim_label = Label(text="Assimilation:")
        self.assim_switch = Switch(active=False)
        self.assim_switch.bind(active=self.trigger_transliteration)
        config_layout.add_widget(self.assim_label)
        config_layout.add_widget(self.assim_switch)

        config_scroll.add_widget(config_layout)
        self.add_widget(config_scroll)

        # --- BOTTOM ACTION LAYER ---
        bottom_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)

        self.live_switch = Switch(active=True)
        bottom_bar.add_widget(Label(text="Live Mode:"))
        bottom_bar.add_widget(self.live_switch)

        self.run_btn = Button(text="Transliterate!", background_color=(0.5, 0, 0.8, 1))
        self.run_btn.bind(on_press=lambda instance: self.transliterate())
        bottom_bar.add_widget(self.run_btn)

        self.add_widget(bottom_bar)

        # Initial GUI setup sync
        self.update_dynamic_ui()

    def on_text_type(self, instance, value):
        if self.live_switch.active:
            self.transliterate()

    def trigger_transliteration(self, instance, value):
        self.transliterate()

    def change_category(self, spinner, text):
        self.current_category = text
        langs = category_languages.get(text, [])
        self.language_spinner.values = langs
        if langs:
            self.language_spinner.text = langs[0]
            self.change_language(self.language_spinner, langs[0])

    def change_language(self, spinner, text):
        self.current_language = text
        styles = language_styles.get(text, ["Standard"])
        self.style_spinner.values = styles
        if styles:
            self.style_spinner.text = styles[0]

        self.update_dynamic_ui()
        self.transliterate()

    def update_dynamic_ui(self):
        # Handle style visibility safely using Kivy's opacity/disabled settings
        styles = language_styles.get(self.current_language, ["Standard"])
        if len(styles) <= 1:
            self.style_label.opacity = 0
            self.style_spinner.opacity = 0
            self.style_spinner.disabled = True
        else:
            self.style_label.opacity = 1
            self.style_spinner.opacity = 1
            self.style_spinner.disabled = False

        # Handle numbers toggle
        if self.current_language in languages_with_number_to_word:
            self.num_switch.disabled = False
        else:
            self.num_switch.active = False
            self.num_switch.disabled = True

        # Handle prefixes and assimilation
        if self.current_language in languages_with_prefix:
            self.prefix_label.opacity = 1
            self.prefix_switch.opacity = 1
            self.prefix_switch.disabled = False
            self.assim_label.opacity = 1
            self.assim_switch.opacity = 1
            self.assim_switch.disabled = False
        else:
            self.prefix_switch.active = False
            self.assim_switch.active = False
            self.prefix_label.opacity = 0
            self.prefix_switch.opacity = 0
            self.prefix_switch.disabled = True
            self.assim_label.opacity = 0
            self.assim_switch.opacity = 0
            self.assim_switch.disabled = True

    def transliterate(self):
        text = self.input_box.text
        selected_style = self.style_spinner.text.lower()
        number_style = "words" if self.num_switch.active else "keep"
        prefix_style = "on" if self.prefix_switch.active else "off"
        assimilation_style = "on" if self.assim_switch.active else "off"
        case_style = self.case_spinner.text.lower()

        transliteration_functions = {
            "Adlam": itra.adlam.transliterate_adlam,
            "Amharic": itra.amharic.transliterate_amharic,
            "Arabic": itra.arabic.transliterate_arabic,
            "Syriac": itra.aramaic.transliterate_syriac,
            "Armenian": itra.armenian.transliterate_armenian,
            "Baybayin": itra.baybayin.transliterate_baybayin,
            "Belarusian": itra.cyrillic.transliterate_belarusian,
            "Bulgarian": itra.cyrillic.transliterate_bulgarian,
            "Buryat": itra.cyrillic.transliterate_buryat,
            "Burmese": itra.burmese.transliterate_burmese,
            "Chinese": itra.chinese.transliterate_chinese,
            "French": ipro.french.pronunciate_french,
            "Asomtavruli": itra.georgian.transliterate_asomtavruli,
            "Mkhedruli": itra.georgian.transliterate_mkhedruli,
            "Nuskhuri": itra.georgian.transliterate_nuskhuri,
            "German": ipro.german.pronunciate_german,
            "Greek": itra.greek.transliterate_greek,
            "Hebrew": itra.hebrew.transliterate_hebrew,
            "Hindi": itra.hindi.transliterate_hindi,
            "Japanese": itra.japanese.transliterate_japanese,
            "Kannada": itra.kannada.transliterate_kannada,
            "Kazakh": itra.cyrillic.transliterate_kazakh,
            "Khmer": itra.khmer.transliterate_khmer,
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
            "Unidentified": itra.uyghur.transliterate_uyghur,  # Fallback mapping
            "Uyghur": itra.uyghur.transliterate_uyghur,
        }

        if self.current_language in transliteration_functions:
            transliteration_func = transliteration_functions[self.current_language]

            kwargs = {}
            if hasattr(transliteration_func, '__code__') and 'style' in transliteration_func.__code__.co_varnames:
                kwargs['style'] = selected_style

            if self.current_language in languages_with_number_to_word and 'number_style' in transliteration_func.__code__.co_varnames:
                kwargs['number_style'] = number_style

            if self.current_language in languages_with_prefix and 'prefix_style' in transliteration_func.__code__.co_varnames:
                kwargs['prefix_style'] = prefix_style

            if self.current_language in languages_with_prefix and 'assimilation_style' in transliteration_func.__code__.co_varnames:
                kwargs['assimilation_style'] = assimilation_style

            try:
                transliterated_text = transliteration_func(text, **kwargs)
            except Exception as e:
                transliterated_text = f"[Library Error: {e}]"

            # Your beautiful regex capitalization handling preserved exactly!
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

            self.output_box.text = transliterated_text


class LinorMobileApp(App):
    def build(self):
        return LinorMobileScreen()


if __name__ == '__main__':
    LinorMobileApp().run()