def generate_id() -> iter:
    n = 0
    while True:
        yield n
        n += 1


id_generator = generate_id()
