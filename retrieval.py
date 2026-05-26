import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = []

document_names = []

folder_path = "documents"

for filename in os.listdir(folder_path):

    file_path = os.path.join(folder_path, filename)

    with open(file_path, "r", encoding="utf-8") as file:

        content = file.read()

        documents.append(content)

        document_names.append(filename)

vectorizer = TfidfVectorizer()

tfidf_matrix = vectorizer.fit_transform(documents)

def search(query):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        tfidf_matrix
    )

    scores = similarities[0]

    ranked_results = sorted(
        zip(document_names, documents, scores),
        key=lambda x: x[2],
        reverse=True
    )

    return ranked_results