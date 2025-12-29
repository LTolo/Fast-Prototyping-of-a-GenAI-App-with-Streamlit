def retrieve_top_k(documents, query, k=2):
    """
    Dummy retrieval logic:
    returns documents that contain the query
    """
    matches = [doc for doc in documents if query.lower() in doc.lower()]
    return matches[:k]


def test_retrieve_top_k_basic():
    docs = [
        "Snowflake supports Cortex",
        "Streamlit is used for UI",
        "RAG combines retrieval and generation"
    ]

    results = retrieve_top_k(docs, "rag", k=1)

    assert len(results) == 1
    assert "RAG" in results[0]
