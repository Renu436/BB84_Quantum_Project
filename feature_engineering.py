def extract_features(error_rate, key_length):
    mismatch = error_rate * key_length
    noise = error_rate ** 2
    stability = 1 - error_rate

    return [error_rate, key_length, mismatch, noise, stability]