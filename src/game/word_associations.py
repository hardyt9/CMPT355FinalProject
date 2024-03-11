import spacy
from collections import defaultdict
 
def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = file.read().splitlines()
    return words

'''
calculate associations between given adjective and specified nouns.
If which not supplied, defaults to all possible nouns.
Which should be a list of strings if supplied.
'''
def get_adj_associations(adjective, which='all'):

     #Load English tokenizer, tagger, parser, and word vectors
    nlp = spacy.load("en_core_web_md")
    #Create a defaultdict to store associations
    associations = defaultdict(dict)

    #Get associations of all nouns with the supplied adjective
    if which == 'all':
        #Read all adjectives and nouns from files
        nouns = read_words_from_file('../red_deck.txt')


    #Get associations of specified nouns with the supplied adjectives
    else:
        nouns = which

    for noun in nouns:
            similarity = nlp(adjective).similarity(nlp(noun))
            associations[adjective][noun] = similarity

    return associations

'''
calculate associations between given noun and specified adjectives.
If which not supplied, defaults to all possible adjectives.
Which should be a list of strings if supplied.
'''
def get_noun_associations(noun, which='all'):

     #Load English tokenizer, tagger, parser, and word vectors
    nlp = spacy.load("en_core_web_md")
    #Create a defaultdict to store associations
    associations = defaultdict(dict)

    #Get associations of all nouns with the supplied adjective
    if which == 'all':
        #Read all adjectives from file
        adjectives = read_words_from_file('../green_deck.txt')


    #Get associations of specified adjectives with the supplied adjectives
    else:
        adjectives = which

    for adjective in adjectives:
            similarity = nlp(adjective).similarity(nlp(noun))
            associations[adjective][noun] = similarity

    return associations