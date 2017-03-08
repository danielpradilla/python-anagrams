'''
Find all anagrams from a dictionary file
Find tuples of anagrams

'''

from collections import defaultdict
from Levenshtein import distance

dictionary = []
anagrams_index = defaultdict(set)
with open('dictionary.txt') as f:
	for line in f:
		word = line.rstrip()
		dictionary.append(word)
		normal = ''.join(sorted(word))
		anagrams_index[normal].add(word)


def get_anagrams_dict(anagrams_index):
	rtn = {}
	for index in anagrams_index:
		# print len(index)
		if len(anagrams_index[index]) > 1:
			rtn[index] = anagrams_index[index]

	return rtn


def get_anagrams_tuples(anagrams_index):
	word_pairs = [[(word1, word2, distance(word1, word2)) for word1 in anagrams_index[index] for word2 in anagrams_index[index] if word1 != word2] for index in anagrams_index if len(anagrams_index[index]) > 1]
	flat_list = [item for sublist in word_pairs for item in sublist]
	rtn = set((w1, w2, d) if w1 <= w2 else (w2, w1, d) for w1, w2, d in flat_list)
	return rtn

all_anagrams = get_anagrams_dict(anagrams_index)

anagrams_tuples = get_anagrams_tuples(anagrams_index)
large_anagrams = sorted(filter(lambda t: t[2] >= 10, anagrams_tuples), key=lambda t: t[2], reverse=True)
print large_anagrams
