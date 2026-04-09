def build_freq_map(data):
    freq_map = {}

    for tokens in data:
        for i, token in enumerate(tokens):
            if i not in freq_map:
                freq_map[i] = {}

            if token not in freq_map[i]:
                freq_map[i][token] = 0

            freq_map[i][token] += 1

    return freq_map
