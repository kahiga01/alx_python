def raise_exception():
    try:
        raise TypeError("This is a type exception.")
    except TypeError as te:
        raise te

