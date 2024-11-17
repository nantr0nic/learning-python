file = "complete_will.txt"

def count_word(word):
    with open(file, 'r', encoding='utf-8') as file_object:
        file_text = file_object.read()
        file_text_words = file_text.split()
        word_count = file_text_words.count(word)
    return word_count

while True:
    print("Count words in the entire works of Shakespeare.")
    word_input = input("What word do you want to count? >> ").strip().lower()
    try:
        counted = count_word(word_input)
        print(f"The word {word_input} appears {str(counted)} times.")
    except ValueError:
        print("Invalid input.")
