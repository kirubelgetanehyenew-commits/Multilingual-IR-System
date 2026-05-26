from langdetect import detect

def detect_language(text):

    # Check Amharic Unicode range
    for char in text:

        if '\u1200' <= char <= '\u137F':
            return "Amharic"

    # If English letters exist
    if any(char.isalpha() for char in text):

        try:

            lang = detect(text)

            if lang == "en":
                return "English"

        except:

            pass

        # fallback
        return "English"

    return "Unknown"