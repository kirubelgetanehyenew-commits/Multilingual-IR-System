from googletrans import Translator

translator = Translator()

def translate_text(text, target_language):

    try:

        translated = translator.translate(
            text,
            dest=target_language
        )

        print(
            "Translated:",
            translated.text
        )

        return translated.text

    except Exception as e:

        print(
            "Translation Error:",
            e
        )

        # fallback dictionary
        dictionary = {

            "education": "ትምህርት",
            "technology": "ቴክኖሎጂ",
            "health": "ጤና",
            "government": "መንግስት",
            "agriculture": "ግብርና",

            "ትምህርት": "education",
            "ቴክኖሎጂ": "technology",
            "ጤና": "health",
            "መንግስት": "government",
            "ግብርና": "agriculture"
        }

        return dictionary.get(text.lower(), text)