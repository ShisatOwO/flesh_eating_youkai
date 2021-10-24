def generate_id() -> iter:
    """infinite iterator. Starts at 0"""
    n = 0
    while True:
        yield n
        n += 1


# That is the generator that should be used to generate the ids of the custom_components.
# i dont think it'll need anything more complex than simple counting
id_generator = generate_id()
