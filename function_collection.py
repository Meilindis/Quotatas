import random
import word_collections
import re

# Only touch the first letter
def capitalize_first_letter_only(phrase):
	return re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), phrase, 1)


# Generate a random rule number and whether it applies to the quote or not
def rule():
    result = (random.randrange(1, 8, 1))
    if result !=1:
        return ""
    else:
        return ("Rule " + str(random.randrange(1, 13, 1)) + ":\n")

def horoscope():
    result = (random.randrange(1, 8, 1))
    if result !=1:
        return ""
    else:
        horrorscope = random.choice(word_collections.zodiac).split(' ', 1)
        return (horrorscope[0].capitalize() + "\n" + horrorscope[1] + ":\n")

# Repeat a random verb three times
def function_times_three():
    current_verb = random.choice(word_collections.verbs)
    return (current_verb.capitalize() + ", " + current_verb + ", " + current_verb)

# Produce 3 random verbs
def template_three_verbs():
    return (capitalize_first_letter_only(random.choice(word_collections.verbs)) + "\n" + random.choice(word_collections.verbs).capitalize() + "\n" + random.choice(word_collections.verbs).capitalize())
    
# Row, row, row your boat
def template_row():
    current_verb = random.choice(word_collections.verbs)
    return (capitalize_first_letter_only(current_verb) + ", " + current_verb + ", " + current_verb) + "\nyour " + random.choice(word_collections.nouns_singular + word_collections.nouns_plural)

# Give three random compliments
def template_three_compliments():
    return (horoscope() + "You are " + random.choice(word_collections.adjectives_positive) + "\nYou are " + random.choice(word_collections.adjectives_positive) + "\nYou are " + random.choice(word_collections.adjectives_positive))

# Give three random characteristics:
def template_three_characteristics():
    return (horoscope() + "You are " + random.choice(word_collections.adjectives) + "\nYou are " + random.choice(word_collections.adjectives) + "\nYou are " + random.choice(word_collections.adjectives))

# Give one random compliment
def template_one_compliment():
    return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.times + word_collections.sometimes)) + " forget that \nyou are " + random.choice(word_collections.adjectives_positive))

# General statement
def template_general():
    return (rule() + "Being " + random.choice(word_collections.adjectives) + " is " + random.choice(word_collections.adjectives))

# Surprise
def template_surprise_singular():
    return ("Here comes the " + random.choice(word_collections.people_singular_sfw) + "!")
    
# Surprise 2
def template_surprise_plural():
    return ("Here come the " + random.choice(word_collections.people_plural_sfw) + "!")

# Call to action
def template_call_to_action():
    return (capitalize_first_letter_only(random.choice(word_collections.people_plural_sfw)) + ", rise up!")

# Spread the word
def template_spread_the_word():
    return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.audiences)) + "\nyou are " + random.choice(word_collections.adjectives) + ".\nStay " + random.choice(word_collections.adjectives) + ".")

# Definition
def template_it_does():
    return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " will " + random.choice(word_collections.verbs) + " you")

# Sharing is caring
def template_share():
    return (rule() + capitalize_first_letter_only(random.choice(word_collections.audiences)) + "\nyou are " + random.choice(word_collections.adjectives) + "\nand " + random.choice(word_collections.adjectives))

# Oh you
def template_you():
    return (horoscope() + "You " + random.choice(word_collections.nouns_singular_sfw))

# Oh adjective you
def template_you_adjective():
    return (horoscope() + "You " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular_sfw))

# It can be
def template_can_be():
    return (capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " can be so\n" + random.choice(word_collections.adverbs) + " " + random.choice(word_collections.adjectives))

# No sorry
def template_no_sorry():
    return (rule() + "Don't apologise for being " + random.choice(word_collections.adjectives))

# Reasons
def template_reasons():
    return ("The fact that you are\na " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular) + "\nmakes you " + random.choice(word_collections.adjectives))

# Deserved
def template_deserved():
    return (capitalize_first_letter_only(random.choice(word_collections.verbs)) + ".\nBecause you deserve it.")

# Truth
def template_truth():
    return (capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " tell it like it is")

# Change
def template_change():
    current_noun = random.choice(word_collections.nouns_singular)
    return (rule() + "Don't be a " + random.choice(word_collections.adjectives) + " " + current_noun + ".\nBe a " + random.choice(word_collections.adjectives) + " " + current_noun + ".")
    
# Possibilities
def template_possible():
	return (rule() + "If we can " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ",\nwe can " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Effect
def template_effect():
	return (capitalize_first_letter_only(random.choice(word_collections.prepositions)) + " " + random.choice(word_collections.nouns_plural) + ",\nwe " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ".")

# Encouragement
def template_encouragement():
	return (rule() + "Challenge " + random.choice(word_collections.nouns_plural) + "\nand act " + random.choice(word_collections.adverbs) + ".")

# Strangely true
def template_strangely_true():
    return (rule() + "Just because you're\na " + random.choice(word_collections.nouns_singular) + "\nit doesn't mean you're\na " + random.choice(word_collections.nouns_singular))

# Really
def template_really():
    return (rule() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural + word_collections.concepts)) + "\nActually good for " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Explanation
def template_explanation():
    return (capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are not trying\nto " + random.choice(word_collections.verbs_intransitive) + ",\nthey are just trying\nto " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.concepts))

# No need
def template_no_need():
    return (rule() + "You don't need " + random.choice(word_collections.nouns_plural + word_collections.concepts) + "\nto " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Potential
def template_potential():
    return (horoscope() + "You have the potential\nto become a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular))

# Results
def template_results():
    return (capitalize_first_letter_only(random.choice(word_collections.concepts)) + " can end in " + random.choice(word_collections.concepts))

# Causation
def template_causation():
    return ("Being " + random.choice(word_collections.adjectives) + "\ncan cause " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Two needs
def template_two_needs():
    return (horoscope() + "The two things you need\nin order to live " + random.choice(word_collections.adverbs) + "\nare " + random.choice(word_collections.nouns_plural + word_collections.concepts) + " and " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Maybe?
def template_maybe():
    return ("Maybe " + random.choice(word_collections.nouns_plural + word_collections.concepts) + "\ncan turn into " + random.choice(word_collections.nouns_plural + word_collections.concepts) + "\nwhen you get older?")

# Orders
def template_orders():
    return (rule() + "They can order you\nto " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural) + ",\nbut they can't order you\nto " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Family
def template_family():
    return (capitalize_first_letter_only(random.choice(word_collections.situations)) + "\nis pretty much like\n" + random.choice(word_collections.verbs_ing) + " your " + random.choice(word_collections.nouns_singular + word_collections.nouns_plural + word_collections.concepts))

# Truth
def template_true():
    return (capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are the " + random.choice(word_collections.concepts) + "\nof all that is " + random.choice(word_collections.adjectives))

# Right
def template_right():
    return (rule() + "Pursue what is " + random.choice(word_collections.adjectives) + "\ninstead of\nwhat is making you " + random.choice(word_collections.adjectives))
    
# Personality
def template_personality():
	return (horoscope() + "You are a " + random.choice(word_collections.nouns_singular) + " " + random.choice(word_collections.people_singular_sfw))

# The best
def function_the_best():
    selected_word = random.choice(word_collections.nouns_singular)
    return (rule() + "The best " + selected_word + " is a " + random.choice(word_collections.adjectives) + " " + selected_word)

# Just be
def template_be():
    return ("Be a " + random.choice(word_collections.nouns_singular_sfw) + "\nBe " + random.choice(word_collections.adjectives) + "\nBe a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular_sfw))
    
# Judgement
def template_judgement():
	return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are\n" + random.choice(word_collections.times) + " " + random.choice(word_collections.adjectives))

# Watch out!
def template_watch_out():
	return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are coming for you!")

# The higher, the fewer
def template_higher():
    return (rule() + "The " + random.choice(word_collections.comparatives) + ", the " + random.choice(word_collections.comparatives))

# More you
def template_you_superlative():
    return (horoscope() + "You can be the " + random.choice(word_collections.superlatives) + " " + random.choice(word_collections.nouns_singular))

# Never
def template_never():
    return (rule() + capitalize_first_letter_only(random.choice(word_collections.times)) + " stop " + random.choice(word_collections.situations))

# Needs
def template_need():
    return (rule() + "You just need a " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_singular))

# You must
def template_must():
    return (rule() + "If you are the " + random.choice(word_collections.superlatives) + " at\n" + random.choice(word_collections.situations) + ",\nyou " + random.choice(word_collections.verbs_mandatory_sfw) + " " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# A good day
def template_day():
    return ("Today is a good day to " + random.choice(word_collections.verbs))

# LLAP
def template_llap():
    return (rule() + capitalize_first_letter_only(random.choice(word_collections.verbs)) + " " + random.choice(word_collections.adjectives) + "\nand " + random.choice(word_collections.verbs + word_collections.verbs_intransitive))

# Why?
def template_why():
    return ("Why stop " + random.choice(word_collections.verbs_ing) + " if you're " + random.choice(word_collections.adjectives) + "?")

# Never
def template_never_again():
    return (rule() + "Never " + random.choice(word_collections.verbs_intransitive) + "\nunless you're willing to " + random.choice(word_collections.verbs + word_collections.verbs_intransitive))

# Excuse me
def template_excuse():
    return ("Excuse me\nWhat does a " + random.choice(word_collections.people_singular_sfw) + " want\nwith a " + random.choice(word_collections.nouns_singular) + "?")

# Outweigh
def template_outweigh():
    selected = random.choice(word_collections.nouns_plural)
    return (rule() + "The " + selected + " of the " + random.choice(word_collections.nouns_plural) + "\n" + random.choice(word_collections.verbs) + " the " + selected + "\nof the " + random.choice(word_collections.nouns_plural))

# Today
def template_today():
    return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.sometimes)) + ",\nyou will encounter " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Do it
def template_do_it():
    return (horoscope() + "Start " + random.choice(word_collections.verbs_ing) + " " + random.choice(word_collections.sometimes))

# They're gonna
def template_gonna():
	return (capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are gonna " + random.choice(word_collections.verbs) + " you!")

# List of defined templates (don't forget to add new templates here or they won't be used!)
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
                 template_need,
                 template_must,
                 template_day,
                 template_llap,
                 template_why,
                 template_never_again,
                 template_excuse,
                 template_outweigh,
                 template_today,
                 template_do_it,
                 template_gonna]

