def generate_spoof(freq_map):
    spoof = []

    for pos in sorted(freq_map.keys()):
        best_token = max(freq_map[pos].items(), key=lambda x: x[1]["z"])[0]
        spoof.append(best_token)

    return " ".join(spoof)
