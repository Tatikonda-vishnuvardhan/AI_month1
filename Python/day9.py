# words count in sentence
def word_count(x):
    words = x.lower().split()
    word_freq = {}

    for word in words:
        word = word.strip(",.;:?!")
        if word in word_freq.keys():
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return word_freq


sentence = input("Enter the sentence to count words:")
unique_words = set(word_count(sentence).keys())
print(f" Unique count in the given sentence :{unique_words}")
print(f" Word count in given sentence :{word_count(sentence)}")
