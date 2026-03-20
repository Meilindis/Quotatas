import random
import word_collections

def rule():
    result = (random.randrange(1, 10, 1))
    if result !=1:
        return ""
    else:
        return ("Rule " + str(random.randrange(1, 13, 1)) + ":\n")

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
    return ("You are " + random.choice(word_collections.adjectives_positive) + "\nYou are " + random.choice(word_collections.adjectives_positive) + "\nYou are " + random.choice(word_collections.adjectives_positive))

# Give three random characteristics:
def function_three_characteristics():
    return ("You are " + random.choice(word_collections.adjectives) + "\nYou are " + random.choice(word_collections.adjectives) + "\nYou are " + random.choice(word_collections.adjectives))

# Give one random compliment
def function_one_compliment():
    return (random.choice(word_collections.times).capitalize() + " forget that you are " + random.choice(word_collections.adjectives_positive))

# General statement
def function_general():
    return (rule() + "Being " + random.choice(word_collections.adjectives) + " is " + random.choice(word_collections.adjectives))

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
    return (rule() + random.choice(word_collections.audiences).capitalize() + "you are " + random.choice(word_collections.adjectives) + " and " + random.choice(word_collections.adjectives))

# Oh you
def function_you():
    return ("You " + random.choice(word_collections.nouns_sfw_singular))

# Oh adjective you
def function_you_adjective():
    return ("You " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_sfw_singular))

# It can be
def function_can_be():
    return (random.choice(word_collections.nouns_plural).capitalize() + " can be so " + random.choice(word_collections.adverbs) + " " + random.choice(word_collections.adjectives))

# No sorry
def function_no_sorry():
    return (rule() + "Don't apologise for being " + random.choice(word_collections.adjectives))

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
    return (rule() + "Don't be a " + random.choice(word_collections.adjectives) + " " + current_noun + ".\nBe a " + random.choice(word_collections.adjectives) + " " + current_noun + ".")
    
# Possibilities
def function_possible():
	return (rule() + "If we can " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ", we can " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Effect
def function_effect():
	return ("Through " + random.choice(word_collections.nouns_plural) + ", we " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ".")

# Encouragement
def function_encouragement():
	return (rule() + "Challenge " + random.choice(word_collections.nouns_plural) + " and act " + random.choice(word_collections.adverbs) + ".")

# Strangely true
def function_strangely_true():
    return (rule() + "Just because you're a " + random.choice(word_collections.nouns_singular) + " it doesn't mean you're a " + random.choice(word_collections.nouns_singular))

# Really
def function_really():
    return (rule() + random.choice(word_collections.nouns_plural + word_collections.concepts).capitalize() + "\nActually good for " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Explanation
def function_explanation():
    return (random.choice(word_collections.nouns_plural).capitalize() + " are not trying to " + random.choice(word_collections.verbs) + ", they are just trying to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.concepts))

# No need
def function_no_need():
    return (rule() + "You don't need " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Potential
def function_potential():
    return ("You have the potential to become a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular))

# Results
def function_results():
    return (random.choice(word_collections.concepts).capitalize() + " can end in " + random.choice(word_collections.concepts))

# Causation
def function_causation():
    return ("Being " + random.choice(word_collections.adjectives) + " can cause " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Two needs
def function_two_needs():
    return ("The two things you need in order to live " + random.choice(word_collections.adverbs) + " are " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " and " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Maybe?
def function_maybe():
    return ("Maybe " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " can turn into " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " when you get older?")

# Orders
def function_orders():
    return (rule() + "They can order you to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ", but they can't order you to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Family
def function_family():
    return ("Being part of a family is pretty much like " + random.choice(word_collections.verbs_ing) + " your " + random.choice(word_collections.nouns_singular + word_collections.nouns_plural + word_collections.concepts))

# Truth
def function_true():
    return (random.choice(word_collections.nouns_plural).capitalize() + " are the " + random.choice(word_collections.concepts) + " of all that is " + random.choice(word_collections.adjectives))

# Right
def function_right():
    return (rule() + "Pursue what is " + random.choice(word_collections.adjectives) + " instead of what is making you " + random.choice(word_collections.adjectives))
    
# Personality
def function_personality():
	return ("You are a " + random.choice(word_collections.nouns_singular) + " " + random.choice(word_collections.people_singular))

# The best
def function_the_best():
    selected_word = random.choice(word_collections.nouns_singular)
    return (rule() + "The best " + selected_word + " is a " + random.choice(word_collections.adjectives) + " " + selected_word)

# Just be
def function_be():
    return ("Be a " + random.choice(word_collections.nouns_sfw_singular) + "\nBe " + random.choice(word_collections.adjectives) + "\nBe a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_sfw_singular))

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
                 function_potential,
                 function_results,
                 function_causation,
                 function_two_needs,
                 function_maybe,
                 function_orders,
                 function_family,
                 function_true,
                 function_right,
                 function_personality,
                 function_the_best,
                 function_be]

