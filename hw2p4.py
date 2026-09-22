"""HW2P4 — Tuple unpacking and dictionary methods.

DSE I1020, Fall 2026. Fill in every section marked TODO.
Running `python hw2p4.py` must print output for all five tasks without error.
"""

import time

# Shared data for Tasks 1, 2, and 5. Do not change these values.
PAIRS = [
    ("Ada", 91),
    ("Grace", 97),
    ("Katherine", 95),
    ("Dorothy", 88),
    ("Mary", 97),
]


def task1_top_scorer(pairs):
    """Return the (name, score) tuple with the highest score.

    Use tuple unpacking in a for loop. Do NOT call max().
    If two people tie for the highest score, return the one that appears first.
    """
    best_name, best_score = pairs[0]
    for name, score in pairs:
        if score > best_score:
            best_name, best_score = name, score
    return best_name, best_score


def task2_safe_lookup(pairs, missing_key):
    """Build a dict from `pairs` and return `.get(missing_key, <default>)`.

    Pick a sensible default and say in a comment why you chose it.
    """
    scores = dict(pairs)
    # default of 0, a missinhg student doesnt have any score, so 0 is a safe stand in that wont be mistaken for a score.
    return scores.get(missing_key, 0)


def task3_merge(a, b):
    """Merge dicts `a` and `b` and return the result.

    Use dict unpacking ({**a, **b}) or .update().
    """
    # On a key present in both dicts, b's value survives. {**a, **b}  unpacks a first, then b, and later keys overwrite earlier ones.
    return {**a, **b}


def task4_unhashable_key():
    """Demonstrate that a list cannot be used as a dict key.

    Trigger the error inside a try/except, and return the exception message as a string.
    """
    # hashable means an object has a fixed hash value that doesnt change, so it can be used as a dict key or set member. lists are mutable so python gives them no hash at all, since a changing hash would break lookups
    try:
        {[1, 2]: "value"}
    except TypeError as e:
        return str(e)


def task5_timing(pairs, repeats=100000):
    """Time the Task 1 unpacking loop against a manual index-based loop.

    Return (unpacking_seconds, index_seconds, ratio) where
    ratio = index_seconds / unpacking_seconds.
    """
    start = time.time()
    for _ in range(repeats):
        for name, score in pairs:
            pass
    unpacking_seconds = time.time() - start

    start = time.time()
    for _ in range(repeats):
        for i in range(len(pairs)):
            name = pairs[i][0]
            score = pairs[i][1]
    index_seconds = time.time() - start

    ratio = index_seconds / unpacking_seconds
    return unpacking_seconds, index_seconds, ratio


def main():
    print("Task 1 — top scorer:", task1_top_scorer(PAIRS))

    print("Task 2 — safe lookup:", task2_safe_lookup(PAIRS, "Alan"))

    scores_a = {"Ada": 91, "Grace": 97}
    scores_b = {"Grace": 99, "Katherine": 95}
    print("Task 3 — merged:", task3_merge(scores_a, scores_b))

    print("Task 4 — unhashable key error:", task4_unhashable_key())

    unpacking_s, index_s, ratio = task5_timing(PAIRS)
    print(f"Task 5 — unpacking: {unpacking_s:.4f}s  index: {index_s:.4f}s  ratio: {ratio:.2f}")


if __name__ == "__main__":
    main()