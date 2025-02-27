def get_word_count(book_text):
	word_count = book_text.split()
	return len(word_count)

def get_char_count(book_text):
	letter_dict = {}
	for character in list(book_text.lower()):
		if character not in letter_dict:
			letter_dict[character] = 1
		else:
			letter_dict[character] += 1
	return letter_dict

def sort_on(dict):
	sorted_items =  sorted(dict.items(), key=lambda item: item[1], reverse = True)
	sorted_dict = {key: value for key, value in sorted_items if key.isalpha()}
	return sorted_dict
