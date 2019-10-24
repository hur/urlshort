class URLOperations():
    # Omitting characters that can cause confusion: 1 l I o O 0
    # Idea to omit from https://stackoverflow.com/a/1119769/
    ALPHABET = "23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ"

    BASE = 56 # Equal to len(ALPHABET)

    # Shorten URLs based on auto-incremented database id value.
    # This function takes the id, converts it into base 56 and
    # returns a string representing the base 56 converted value.
    # See: https://stackoverflow.com/a/742047/
    def shorten(key:int, BASE=BASE, ALPHABET=ALPHABET):
        numbers = []
        result = ""
        if key == 0:
            return ALPHABET[0]
        while key > 0:
            quot_and_rem = divmod(key, BASE)
            numbers.append(quot_and_rem[1]) # Append with remainder
            key = quot_and_rem[0] # quotient is the new key
        numbers.reverse()
        for number in numbers:
            result += ALPHABET[number]
        return result

    # Convert shortened URL to database id value.
    # Takes each character of input string, finds its index and then
    # calculates index*BASE^0 + ... + index*BASE^(n-1) to 
    # convert back to base 10
    def lengthen(short:str, BASE=BASE, ALPHABET=ALPHABET):
        numbers = []
        n = len(short) - 1
        result = 0
        for character in short:
            numbers.append(ALPHABET.index(character))
        for number in numbers:
            result += number*((BASE)**(n))
            n -= 1
        return result
