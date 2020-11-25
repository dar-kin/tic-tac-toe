prime_numbers = [x for x in range(2, 1000) if not any([x % n == 0 for n in range(2, x - 1)])]
