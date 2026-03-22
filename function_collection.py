import random
import word_collections


# Generate a random rule number and whether it applies to the quote or not
def rule():
    result = (random.randrange(1, 8, 1))
    if result !=1:
        return ""
    else:
        return ("Rule " + str(random.randrange(1, 13, 1)) + ":\n")

# Repeat a random verb three times
def function_times_three():
    current_verb = random.choice(word_collections.verbs)
    return (current_verb.capitalize() + ", " + current_verb + ", " + current_verb)

# Produce 3 random verbs
def template_three_verbs():
    return (random.choice(word_collections.verbs).capitalize() + "\n" + random.choice(word_collections.verbs).capitalize() + "\n" + random.choice(word_collections.verbs).capitalize())
    
# Row, row, row your boat
def template_row():
    current_verb = random.choice(word_collections.verbs)
    return (current_verb.capitalize() + ", " + current_verb + ", " + current_verb) + " your " + random.choice(word_collections.nouns_singular + word_collections.nouns_plural)

# Give three random compliments
def template_three_compliments():
    return ("You are " + random.choice(word_collections.adjectives_positive) + "\nYou are " + random.choice(word_collections.adjectives_positive) + "\nYou are " + random.choice(word_collections.adjectives_positive))

# Give three random characteristics:
def template_three_characteristics():
    return ("You are " + random.choice(word_collections.adjectives) + "\nYou are " + random.choice(word_collections.adjectives) + "\nYou are " + random.choice(word_collections.adjectives))

# Give one random compliment
def template_one_compliment():
    return (random.choice(word_collections.times).capitalize() + " forget that you are " + random.choice(word_collections.adjectives_positive))

# General statement
def template_general():
    return (rule() + "Being " + random.choice(word_collections.adjectives) + " is " + random.choice(word_collections.adjectives))

# Surprise
def template_surprise_singular():
    return ("Here comes the " + random.choice(word_collections.people_singular) + "!")
    
# Surprise 2
def template_surprise_plural():
    return ("Here come the " + random.choice(word_collections.people_plural) + "!")

# Call to action
def template_call_to_action():
    return (random.choice(word_collections.people_plural).capitalize() + ", rise up!")

# Spread the word
def template_spread_the_word():
    return (random.choice(word_collections.audiences).capitalize() + " you are " + random.choice(word_collections.adjectives) + ".\nStay " + random.choice(word_collections.adjectives) + ".")

# Definition
def template_it_does():
    return (random.choice(word_collections.nouns_plural).capitalize() + " will " + random.choice(word_collections.verbs) + " you")

# Sharing is caring
def template_share():
    return (rule() + random.choice(word_collections.audiences).capitalize() + " you are " + random.choice(word_collections.adjectives) + " and " + random.choice(word_collections.adjectives))

# Oh you
def template_you():
    return ("You " + random.choice(word_collections.nouns_singular_sfw))

# Oh adjective you
def template_you_adjective():
    return ("You " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular_sfw))

# It can be
def template_can_be():
    return (random.choice(word_collections.nouns_plural).capitalize() + " can be so " + random.choice(word_collections.adverbs) + " " + random.choice(word_collections.adjectives))

# No sorry
def template_no_sorry():
    return (rule() + "Don't apologise for being " + random.choice(word_collections.adjectives))

# Reasons
def template_reasons():
    return ("The fact that you are the " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular) + " makes you " + random.choice(word_collections.adjectives))

# Deserved
def template_deserved():
    return (random.choice(word_collections.verbs).capitalize() + ".\nBecause you deserve it.")

# Truth
def template_truth():
    return (random.choice(word_collections.nouns_plural).capitalize() + " tell it like it is")

# Change
def template_change():
    current_noun = random.choice(word_collections.nouns_singular)
    return (rule() + "Don't be a " + random.choice(word_collections.adjectives) + " " + current_noun + ".\nBe a " + random.choice(word_collections.adjectives) + " " + current_noun + ".")
    
# Possibilities
def template_possible():
	return (rule() + "If we can " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ", we can " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Effect
def template_effect():
	return (random.choice(word_collections.prepositions).capitalize() + " " + random.choice(word_collections.nouns_plural) + ", we " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ".")

# Encouragement
def template_encouragement():
	return (rule() + "Challenge " + random.choice(word_collections.nouns_plural) + " and act " + random.choice(word_collections.adverbs) + ".")

# Strangely true
def template_strangely_true():
    return (rule() + "Just because you're a " + random.choice(word_collections.nouns_singular) + " it doesn't mean you're a " + random.choice(word_collections.nouns_singular))

# Really
def template_really():
    return (rule() + random.choice(word_collections.nouns_plural + word_collections.concepts).capitalize() + "\nActually good for " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Explanation
def template_explanation():
    return (random.choice(word_collections.nouns_plural).capitalize() + " are not trying to " + random.choice(word_collections.verbs_intransitive) + ", they are just trying to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.concepts))

# No need
def template_no_need():
    return (rule() + "You don't need " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Potential
def template_potential():
    return ("You have the potential to become a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular))

# Results
def template_results():
    return (random.choice(word_collections.concepts).capitalize() + " can end in " + random.choice(word_collections.concepts))

# Causation
def template_causation():
    return ("Being " + random.choice(word_collections.adjectives) + " can cause " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Two needs
def template_two_needs():
    return ("The two things you need in order to live " + random.choice(word_collections.adverbs) + " are " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " and " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Maybe?
def template_maybe():
    return ("Maybe " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " can turn into " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " when you get older?")

# Orders
def template_orders():
    return (rule() + "They can order you to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ", but they can't order you to " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Family
def template_family():
    return (random.choice(word_collections.situations).capitalize() + " is pretty much like " + random.choice(word_collections.verbs_ing) + " your " + random.choice(word_collections.nouns_singular + word_collections.nouns_plural + word_collections.concepts))

# Truth
def template_true():
    return (random.choice(word_collections.nouns_plural).capitalize() + " are the " + random.choice(word_collections.concepts) + " of all that is " + random.choice(word_collections.adjectives))

# Right
def template_right():
    return (rule() + "Pursue what is " + random.choice(word_collections.adjectives) + " instead of what is making you " + random.choice(word_collections.adjectives))
    
# Personality
def template_personality():
	return ("You are a " + random.choice(word_collections.nouns_singular) + " " + random.choice(word_collections.people_singular))

# The best
def function_the_best():
    selected_word = random.choice(word_collections.nouns_singular)
    return (rule() + "The best " + selected_word + " is a " + random.choice(word_collections.adjectives) + " " + selected_word)

# Just be
def template_be():
    return ("Be a " + random.choice(word_collections.nouns_singular_sfw) + "\nBe " + random.choice(word_collections.adjectives) + "\nBe a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular_sfw))
    
# Judgement
def template_judgement():
	return (random.choice(word_collections.nouns_plural).capitalize() + " are " + random.choice(word_collections.times) + " " + random.choice(word_collections.adjectives))

# Watch out!
def template_watch_out():
	return (random.choice(word_collections.nouns_plural).capitalize() + " are coming for you!")

# The higher, the fewer
def template_higher():
    return (rule() + "The " + random.choice(word_collections.comparatives) + ", the " + random.choice(word_collections.comparatives))

# More you
def template_you_superlative():
    return ("You can be the " + random.choice(word_collections.superlatives) + " " + random.choice(word_collections.nouns_singular))

# Never
def template_never():
    return (rule() + random.choice(word_collections.times).capitalize() + " stop " + random.choice(word_collections.situations))

# Needs
def template_need():
    return (random.choice(word_collections.times).capitalize() + " you just need a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular))

# List of defined tepmlates (don't forget to add new templates here or they won't be used!)
template_list = [function_times_three, 
                 template_three_compliments, 
                 template_three_characteristics,
                 template_one_compliment, 
                 template_three_verbs, 
                 template_row,
                 template_general, 
                 template_surprise_singular,
                 template_surprise_plural, 
                 template_call_to_action, 
                 template_spread_the_word,
                 template_it_does,
                 template_share,
                 template_you,
                 template_you_adjective,
                 template_can_be,
                 template_no_sorry,
                 template_reasons,
                 template_deserved, 
                 template_truth,
                 template_change,
                 template_possible,
                 template_effect,
                 template_encouragement,
                 template_strangely_true,
                 template_really,
                 template_explanation,
                 template_no_need,
                 template_potential,
                 template_results,
                 template_causation,
                 template_two_needs,
                 template_maybe,
                 template_orders,
                 template_family,
                 template_true,
                 template_right,
                 template_personality,
                 function_the_best,
                 template_be,
                 template_judgement,
                 template_watch_out,
                 template_higher,
                 template_you_superlative,
                 template_never,
                 template_need]

