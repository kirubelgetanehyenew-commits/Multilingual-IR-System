from evaluation import (
    precision,
    recall,
    precision_at_k
)

test_cases = [

    {

        "query": "education",

        "relevant": [

            "education_en.txt",
            "education_am.txt"
        ],

        "retrieved": [

            "education_en.txt",
            "technology_en.txt",
            "education_am.txt"
        ]
    },

    {

        "query": "technology",

        "relevant": [

            "technology_en.txt",
            "technology_am.txt"
        ],

        "retrieved": [

            "technology_en.txt",
            "government_en.txt",
            "technology_am.txt"
        ]
    },

    {

        "query": "health",

        "relevant": [

            "health_en.txt",
            "health_am.txt"
        ],

        "retrieved": [

            "health_en.txt",
            "health_am.txt",
            "education_en.txt"
        ]
    },

    {

        "query": "agriculture",

        "relevant": [

            "agriculture_en.txt",
            "agriculture_am.txt"
        ],

        "retrieved": [

            "agriculture_en.txt",
            "government_en.txt",
            "agriculture_am.txt"
        ]
    },

    {

        "query": "government",

        "relevant": [

            "government_en.txt",
            "government_am.txt"
        ],

        "retrieved": [

            "government_en.txt",
            "government_am.txt",
            "technology_en.txt"
        ]
    }

]

for case in test_cases:

    p = precision(
        case["relevant"],
        case["retrieved"]
    )

    r = recall(
        case["relevant"],
        case["retrieved"]
    )

    pk = precision_at_k(
        case["relevant"],
        case["retrieved"],
        2
    )

    print("\n====================")

    print("Query:", case["query"])

    print("Precision:", round(p, 2))

    print("Recall:", round(r, 2))

    print("Precision@2:", round(pk, 2))