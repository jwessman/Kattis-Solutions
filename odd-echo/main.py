if __name__ == '__main__':
    nr_words: int = int(input())
    to_output = 0
    for i in range(nr_words):
        current_word = input()
        if to_output == 0:
            print(current_word)
        to_output ^= 1
