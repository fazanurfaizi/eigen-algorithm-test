def count_words(input, query):
    output = {}

    for word in input:
        if word in output:
            output[word] += 1
        else:
            output[word] = 1

    result = []
    messages = []

    for word in query:
        if word in output:
            result.append(output[word])
            messages.append(f"kata '{word}' terdapat {output[word]} pada INPUT")
        else:
            result.append(0)
            messages.append(f"kata '{word}' tidak ada pada INPUT")

    return result, messages

input = ['xc', 'dz', 'bbb', 'dz']
query = ['bbb', 'ac', 'dz']
output, messages = count_words(input, query)
print(f"{output} karena {' '.join(messages)}")