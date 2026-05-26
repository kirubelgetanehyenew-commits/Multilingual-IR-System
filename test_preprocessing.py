from preprocessing import preprocess_text

english_text = """
Information retrieval is very important
for search engines and document systems.
"""

amharic_text = """
የመረጃ ፍለጋ ለፍለጋ ስርዓቶች በጣም አስፈላጊ ነው።
"""

print("\n========== ENGLISH ==========\n")

english_tokens = preprocess_text(
    english_text
)

print(english_tokens)

print("\n========== AMHARIC ==========\n")

amharic_tokens = preprocess_text(
    amharic_text
)

print(amharic_tokens)