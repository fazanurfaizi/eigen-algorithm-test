def find_longest_word(input: str):
    words = input.split()

    longest_word = ''
    max_length = 0

    for word in words:
        if len(word) > max_length:
            longest_word = word
            max_length = len(word)

    return longest_word, max_length

sentences = 'Saya sangat senang mengerjakan soal algoritma'
longest_word, length = find_longest_word(sentences)
print(f'{longest_word}: {length} character')