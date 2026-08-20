import pickle


def encode(cache: dict) -> bytes:
    """Serialize a results cache to bytes."""
    return pickle.dumps(cache)
