def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    result = []
    for word in tokens:
        if word not in stopwords:
            result.append(word)
    return result