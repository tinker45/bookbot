from stats import get_word_count, get_char_count, sort_on

def get_book_text(book_path):
	with open(book_path) as f:
		file_contents = f.read()
		return file_contents

def main():
	book_path = "books/frankenstein.txt"
	book_text = get_book_text(book_path)

	print("============ BOOKBOT ============\nAnalyzing books found at {book_path}")

	word_count = get_word_count(book_text)
	print(f"----------- Word Count ----------\nFound {word_count} total words")

	char_count = get_char_count(book_text)
	#print(f"{char_count} ")	

	sorted_dict = sort_on(char_count)
	
	print(f"--------- Character Count -------")
	for key, value, in sorted_dict.items():
		print(f"{key}: {value}")

main()
