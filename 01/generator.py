def search_lines(file, search_words, stop_words):
    search_set = {word.lower() for word in search_words}
    stop_set = {word.lower() for word in stop_words}

    with open(file, encoding='utf-8') if isinstance(file, str) else file as f:
        for line in f:
            words = set(line.strip().lower().split())
            if words & stop_set:
                continue
            if words & search_set:
                yield line.strip()
