import csv
import re
import os

# Get the directory of the current script
MODULE_DIR = os.path.dirname(__file__)

# Define full paths to your data files
PHRASE_FILE = os.path.join(MODULE_DIR, 'phrases.csv')
WORD_FILE = os.path.join(MODULE_DIR, 'words.csv')


def _load_replacements(filename):
    """
    Loads replacement pairs from a CSV file into a dictionary.
    This is a private helper function.
    """
    replacements = {}
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            # Skip the header row
            next(reader, None)
            for row in reader:
                if len(row) == 2:
                    original, replacement = row
                    replacements[original.strip()] = replacement.strip()
    except FileNotFoundError:
        print(
            f"Error: The file '{filename}' was not found. Please ensure it is in the same directory as diacritizer.py.")
        print("Continuing without these replacements.")
    return replacements


# Pre-load the replacement data when the module is imported
_phrase_replacements = _load_replacements(PHRASE_FILE)
_word_replacements = _load_replacements(WORD_FILE)


def diacritize(text):
    """
    Applies diacritization (tashkil) to a given Arabic text using
    pre-loaded phrase and word replacement rules, while preserving newlines and all whitespace.

    Args:
        text (str): The input Arabic text to be diacritized.

    Returns:
        str: The diacritized text.
    """
    if not isinstance(text, str):
        return ""

    # Step 1: Apply phrase-level replacements on the entire text first.
    # We do this before splitting to correctly handle phrases that span newlines or complex whitespace.
    sorted_phrases = sorted(_phrase_replacements.keys(), key=len, reverse=True)
    for phrase in sorted_phrases:
        text = text.replace(phrase, _phrase_replacements[phrase])

    # Step 2: Apply word-level replacements while preserving all whitespace.
    # The regex pattern (\\s+) splits the text by whitespace but keeps the whitespace in the list.
    tokens = re.split(r'(\s+)', text)
    processed_tokens = []

    for token in tokens:
        # Check if the token is an Arabic word (not just whitespace)
        if token and not token.isspace():
            if token in _word_replacements:
                processed_tokens.append(_word_replacements[token])
            else:
                processed_tokens.append(token)
        else:
            # If it's whitespace, just append it back
            processed_tokens.append(token)

    return "".join(processed_tokens)


# Example usage within the module for testing
if __name__ == "__main__":
    test_text = "صباح الخير  يا صديقي،   كيف حالك؟\nأين بيتك؟  مع السلامة!"
    diacritized_text = diacritize(test_text)
    print(f"Original Text:\n---\n{test_text}\n---")
    print(f"Diacritized Text:\n---\n{diacritized_text}\n---")