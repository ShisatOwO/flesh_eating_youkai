def generate_id() -> iter:
    n = 0
    while True:
        yield n
        n += 1