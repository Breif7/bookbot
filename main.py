from stats import count_words, count_characters,sort_dic
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    characters = count_characters(text)
    print("--------- Character Count -------")
    sorted_dic=sort_dic(characters)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()

