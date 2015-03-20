
def read_dictionary_file(filename):
	"Returns dict from characters tuple to anagrams found in dictionary."

	# Assuming we have a plain text file
	fp = open(filename)

	characters_to_anagrams_dict = {}
	for line in fp:
		word = line.strip()
		if word:
			lowercase_word = word.lower()
			word_characters = list(lowercase_word)
			word_characters.sort()
			word_characters = tuple(word_characters)
			word_anagrams = characters_to_anagrams_dict.setdefault(word_characters,[])
			word_anagrams.append(word)

	fp.close()

	return characters_to_anagrams_dict

def get_anagrams(word, anagrams_dict):

	lowercase_word = word.lower()
	search_key = list(lowercase_word)
	search_key.sort()
	search_key = tuple(search_key)

	anagrams = anagrams_dict.get(search_key,[])

	return anagrams

if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser("Finds all anagrams in dictionary for supplied word.")
	parser.add_argument('--dictionary-file', '-d',
		                help="File containing dictionary words, one word per line.")
	parser.add_argument('--words', '-w', nargs='+',
		                help="Source word for anagram search")

	args = parser.parse_args()

	characters_to_anagrams_dict = read_dictionary_file(args.dictionary_file)

	for word in args.words:
		anagrams = get_anagrams(word, characters_to_anagrams_dict)

		# We do not check that the supplied word is, in fact, a dictionary word itself.
		lowercased_word = word.lower()
		anagrams_other_than_the_word = [anagram for anagram in anagrams if lowercased_word != anagram.lower()]
		print "{0}: {1}".format(word, anagrams_other_than_the_word)