def count_word_frequency(text):
    
    words = text.lower().split()

    
    word_freq = {}

    
    for word in words:
        
        if word in word_freq:
            word_freq[word] += 1
        
        else:
            word_freq[word] = 1

    
    return word_freq


text = "This is a sample text. This text is for demonstrating word frequency counting."
word_freq = count_word_frequency(text)
print(word_freq)