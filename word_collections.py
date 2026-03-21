from pathlib import Path
import os

adjectives_positive = []
adjectives_neutral = []
adjectives_negative = []
colours = []
nouns_singular_sfw = []
nouns_plural_sfw = []
people_singular = []
people_plural = []
animals_singular = []
animals_plural = []
food_singular = []
food_plural = []
verbs_sfw = []
verbs_intransitive_sfw = []
verbs_third_person_sfw = []
verbs_active_sfw = []
verbs_ing_sfw = []
verbs_mandatory_sfw = []
times = []
audiences = []
adverbs = []
concepts_positive = []
concepts_neutral = []
concepts_negative = []
concepts_nsfw = []
nouns_singular_nsfw = []
nouns_plural_nsfw = []
adjectives_nsfw = []
verbs_nsfw = []
verbs_intransitive_nsfw = []
verbs_third_person_nsfw = []
verbs_active_nsfw = []
verbs_ing_nsfw = []
comparative_sfw = []
comparative_nsfw = []
superlative_sfw = []
superlative_nsfw = []
 

nouns_singular = nouns_singular_sfw + animals_singular + verbs_active_sfw + food_singular
nouns_plural = animals_plural + people_plural + nouns_plural_sfw + food_plural
adjectives = adjectives_positive + adjectives_neutral + comparative_sfw
verbs = verbs_sfw
verbs_third_person = verbs_third_person_sfw
verbs_ing = verbs_ing_sfw
verbs_intransitive = verbs_intransitive_sfw
concepts = concepts_neutral + concepts_positive
comparative = comparative_sfw
superlative = superlative_sfw
  

def import_list(filename):
    word_list = []
    path = Path(__file__).parent.absolute()
    location = os.path.join(path, 'word_lists')
    location = os.path.join(location, filename)
    infile = open(location,'r')
    for word in infile:
        word_list.append(word.rstrip())

    infile.close()
    return word_list


# Exports the list with the name list_name to the subfolder word_lists of the project alphabetically
def export_list(list, list_name):
    sorted_list = sorted(list)
    path = Path(__file__).parent.absolute()
    filename = list_name + '.txt'
    location = os.path.join(path, 'word_lists')
    location = os.path.join(location, filename)
    with open(location, 'w') as f:
        for item in sorted_list:
            f.write(f"{item}\n")
