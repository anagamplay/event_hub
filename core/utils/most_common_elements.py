from collections import Counter

def most_common_elements(data_list):
    if not data_list:
        return []

    counts = Counter(data_list)
    max_count = max(counts.values())
    most_common = [item for item, count in counts.items() if count == max_count]
    return most_common