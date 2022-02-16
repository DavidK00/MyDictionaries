def main():
    text = open('AI.txt', 'r')
    word_counter = {}
    
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        
        for word in words:
            if word in word_counter:
                word_counter[word] = word_counter[word] + 1
            else:
                word_counter[word] = 1
    print(word_counter)
    
main()