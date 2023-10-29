def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    
    print(f"The number of words is: {count_words(text)}")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    number_of_words = len(words)

    return number_of_words
main()