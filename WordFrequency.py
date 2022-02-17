def main():
    text = open('AI.txt', 'r')
    word_counter = {}
    
    for line in text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        
        for i in words:
            if i in word_counter:
                word_counter[i] = word_counter[i] + 1
            else:
                word_counter[i] = 1
    print(word_counter)
    
main()