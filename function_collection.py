import random
import word_collections

# Repeat a random verb three times
def function_times_three():
    current_verb = random.choice(word_collections.verbs)
    return (current_verb.capitalize() + ", " + current_verb + ", " + current_verb)

# Produce 3 random verbs
def function_three_verbs():
    return (random.choice(word_collections.verbs).capitalize() + "\n" + random.choice(word_collections.verbs).capitalize() + "\n" + random.choice(word_collections.verbs).capitalize())
    
# Row, row, row your boat
def function_row():
    current_verb = random.choice(word_collections.verbs)
    return (current_verb.capitalize() + ", " + current_verb + ", " + current_verb) + " your " + random.choice(word_collections.nouns_singular + word_collections.nouns_plural)

# Give three random compliments
def function_three_compliments():
    return ("You are " + random.choice(word_collections.positive_adjectives) + "\nYou are " + random.choice(word_collections.positive_adjectives) + "\nYou are " + random.choice(word_collections.positive_adjectives))

# Give three random characteristics:
def function_three_characteristics():
    return ("You are " + random.choice(word_collections.adjectives) + "\nYou are " + random.choice(word_collections.adjectives) + "\nYou are " + random.choice(word_collections.adjectives))

# Give one random compliment
def function_one_compliment():
    return (random.choice(word_collections.times).capitalize() + " forget that you are " + random.choice(word_collections.positive_adjectives))

# General statement
def function_general():
    return ("Being " + random.choice(word_collections.adjectives) + " is " + random.choice(word_collections.adjectives))

# Surprise
def function_surprise_singular():
    return ("Here comes the " + random.choice(word_collections.people_singular) + "!")
    
# Surprise 2
def function_surprise_plural():
    return ("Here come the " + random.choice(word_collections.people_plural) + "!")

# Call to action
def function_call_to_action():
    return (random.choice(word_collections.people_plural).capitalize() + ", rise up!")

# Spread the word
def function_spread_the_word():
    return (random.choice(word_collections.audiences).capitalize() + "you are " + random.choice(word_collections.adjectives) + ".\nStay " + random.choice(word_collections.adjectives) + ".")

# Definition
def function_it_does():
    return (random.choice(word_collections.nouns_plural).capitalize() + " will " + random.choice(word_collections.verbs) + " you")

# Sharing is caring
def function_share():
    return (random.choice(word_collections.audiences).capitalize() + "you are " + random.choice(word_collections.adjectives) + " and " + random.choice(word_collections.adjectives))

# Oh you
def function_you():
    return ("You " + random.choice(word_collections.neutral_nouns_singular))

# Oh adjective you
def function_you_adjective():
    return ("You " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.neutral_nouns_singular))

# It can be
def function_can_be():
    return (random.choice(word_collections.nouns_plural).capitalize() + " can be so " + random.choice(word_collections.adverbs) + " " + random.choice(word_collections.adjectives))

# No sorry
def function_no_sorry():
    return ("Don't apologise for being " + random.choice(word_collections.adjectives))

# Reasons
def function_reasons():
    return ("The fact that you are " + random.choice(word_collections.adjectives) + " makes you " + random.choice(word_collections.adjectives))

# Deserved
def function_deserved():
    return (random.choice(word_collections.verbs).capitalize() + ".\nBecause you deserve it.")

# Truth
def function_truth():
    return (random.choice(word_collections.nouns_plural).capitalize() + " tell it like it is")

# Change
def function_change():
    current_noun = random.choice(word_collections.nouns_singular)
    return ("Don't be a " + random.choice(word_collections.adjectives) + " " + current_noun + ".\nBe a " + random.choice(word_collections.adjectives) + " " + current_noun + ".")
    
# Possibilities
def function_possible():
	return ("If we can " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ", we can " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Effect
def function_effect():
	return ("Through " + random.choice(word_collections.nouns_plural) + ", we " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ".")

# Encouragement
def function_encouragement():
	return ("Challenge " + random.choice(word_collections.nouns_plural) + " and act " + random.choice(word_collections.adverbs) + ".")

# Strangely true
def function_strangely_true():
    return ("Just because you're a " + random.choice(word_collections.nouns_singular) + " it doesn't mean you're a " + random.choice(word_collections.nouns_singular))

# Really
def function_really():
    return (random.choice(word_collections.nouns_plural).capitalize() + "\nActually good for " + random.choice(word_collections.nouns_plural))

# Explanation
def function_explanation():
    return (random.choice(word_collections.nouns_plural).capitalize() + " are not trying to " + random.choice(word_collections.verbs) + ", they are just trying to " + random.choice(word_collections.verbs))

# No need
def function_no_need():
    return ("You don't need " + random.choice(word_collections.nouns_plural) + " to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Potential
def function_potential():
    return ("You have the potential to become a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular))

# List of defined functions (don't forget to add new functions here!)
function_list = [function_times_three, 
                 function_three_compliments, 
                 function_three_characteristics,
                 function_one_compliment, 
                 function_three_verbs, 
                 function_row,
                 function_general, 
                 function_surprise_singular,
                 function_surprise_plural, 
                 function_call_to_action, 
                 function_spread_the_word,
                 function_it_does,
                 function_share,
                 function_you,
                 function_you_adjective,
                 function_can_be,
                 function_no_sorry,
                 function_reasons,
                 function_deserved, 
                 function_truth,
                 function_change,
                 function_possible,
                 function_effect,
                 function_encouragement,
                 function_strangely_true,
                 function_really,
                 function_explanation,
                 function_no_need,
                 function_potential]

