from pathlib import Path
import os

adjectives_positive = []
adjectives_neutral = []
adjectives_negative = []
colours = []
nouns_singular_sfw = []
nouns_plural_sfw = []
people_singular_sfw = []
people_plural_sfw = []
people_singular_neg = []
people_plural_neg = []
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
comparatives_sfw = []
comparatives_nsfw = []
superlatives_sfw = []
superlatives_nsfw = []
situations_sfw = []
situations_nsfw = []
prepositions = []
zodiac = []
sometimes = []
 

# Aggregate lists
nouns_singular = []
nouns_plural = []
adjectives = []
verbs = []
verbs_third_person = []
verbs_ing = []
verbs_intransitive = []
concepts = []
comparatives = []
superlatives = []
situations = []
people_singular = []
people_plural = []
  

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
