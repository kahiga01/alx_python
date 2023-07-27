def best_score(a_dictionary):
    # Create variables to keep track of the current highest score and its corresponding key.
    max_score = None
    max_key = None

    # Iterate through the dictionary to locate the key associated with the highest integer value.
    for key, value in a_dictionary.items():
        if max_score is None or value > max_score:
            max_score = value
            max_key = key

    return max_key
