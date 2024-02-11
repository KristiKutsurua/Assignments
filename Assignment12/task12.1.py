def word_count(sentence):
    sentence = sentence.lower()
    
    words = sentence.split()

    word_counts = {}

    for word in words:
        word = word.strip('.,!?')
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts

sentence = input("შეიყვანეთ წინადადება: \n")
word_counts = word_count(sentence)
print(word_counts)
