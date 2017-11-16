data = '''Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. You can’t use lists as keys, since lists can be modified in place using index assignments, slice assignments.'''  # NOQA


def main():
    """
    Find 5 most common words in a string
    """
    from collections import Counter
    import re
    cleaned = re.sub(r'“|”|\.|,', ' ', data)
    c = Counter(cleaned.split())
    top = c.most_common(5)
    print(top)


if __name__ == "__main__":
    main()
