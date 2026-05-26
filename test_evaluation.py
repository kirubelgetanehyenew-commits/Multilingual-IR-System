from evaluation import precision
from evaluation import recall

relevant = [
    "doc1_en.txt",
    "doc3_am.txt"
]

retrieved = [
    "doc1_en.txt",
    "doc2_en.txt"
]

print(
    "Precision:",
    precision(relevant, retrieved)
)

print(
    "Recall:",
    recall(relevant, retrieved)
)