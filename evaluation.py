def precision(relevant, retrieved):

    return len(
        set(relevant) & set(retrieved)
    ) / len(retrieved)


def recall(relevant, retrieved):

    return len(
        set(relevant) & set(retrieved)
    ) / len(relevant)


def precision_at_k(
    relevant,
    retrieved,
    k
):

    retrieved_at_k = retrieved[:k]

    relevant_count = len(

        set(relevant)
        &
        set(retrieved_at_k)

    )

    return relevant_count / k