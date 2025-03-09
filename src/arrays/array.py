def reverse_array(a: list) -> None:
    """Reverse the elements of an array in place."""
    if len(a) == 0:
        return None

    n = len(a)
    halfway = n // 2
    for i in range(halfway):
        # Swap the i-th element with its mirrored element from the other direction.
        a[i], a[n - 1 - i] = a[n - 1 - i], a[i]
    return None
