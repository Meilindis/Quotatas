import random
import word_collections
import re

vowels = ['a', 'e', 'i', 'o', 'u']

# Only touch the first letter
def capitalize_first_letter_only(phrase):
	return re.sub('([a-zA-Z])', lambda x: x.groups()[0].upper(), phrase, 1)


# Generate a random rule number and whether it applies to the quote or not
def rule():
    result = (random.randrange(1, 8, 1))
    if result !=1:
        return ""
    else:
        return ("Rule " + str(random.randrange(1, 12, 1)) + ":\n\n")

def horoscope():
    result = (random.randrange(1, 8, 1))
    if result !=1:
        return ""
    else:
        return ("Today's horoscope - " + capitalize_first_letter_only(random.choice(word_collections.zodiac)) + ":\n\n")

def a_or_an(text):
    if text[0] in vowels:
        article = "an "
    else:
        article = "a "
    return article

# Repeat a random verb three times
def template_times_three():
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
    return (rule() + "Being " + random.choice(word_collections.adjectives) + "\nis " + random.choice(word_collections.adjectives))

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
    return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.audiences)) + "\nthat you are " + random.choice(word_collections.adjectives) + ".\nStay " + random.choice(word_collections.adjectives) + ".")

# Definition
def template_it_does():
    return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " will " + random.choice(word_collections.verbs) + " you")

# Sharing is caring
def template_share():
    return (rule() + capitalize_first_letter_only(random.choice(word_collections.audiences)) + "\nthat you are " + random.choice(word_collections.adjectives) + "\nand " + random.choice(word_collections.adjectives))

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
    return (rule() + "Don't apologise \nfor being " + random.choice(word_collections.adjectives))

# Reasons
def template_reasons():
    temp = random.choice(word_collections.adjectives)
    return ("The fact that you are\n" + a_or_an(temp) + temp + " " + random.choice(word_collections.nouns_singular) + "\nmakes you " + random.choice(word_collections.adjectives))

# Deserved
def template_deserved():
    return (capitalize_first_letter_only(random.choice(word_collections.verbs)) + ".\nBecause you deserve it.")

# Truth
def template_truth():
    return (capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " tell it like it is")

# Change
def template_change():
    current_noun = random.choice(word_collections.nouns_singular)
    temp1 = random.choice(word_collections.adjectives)
    temp2 = random.choice(word_collections.adjectives)
    return (rule() + "Don't be " + a_or_an(temp1) + "\n" + temp1 + " " + current_noun + ".\nBe " + a_or_an(temp2) + "\n" +  temp2 + " " + current_noun + ".")
    
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
    temp1 = random.choice(word_collections.nouns_singular)
    temp2 = random.choice(word_collections.nouns_singular)
    return (rule() + "Just because you're\n" + a_or_an(temp1) + temp1 + "\nit doesn't mean you're\n" + a_or_an(temp2) + temp2)

# Really
def template_really():
    return (rule() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural + word_collections.concepts)) + "\nActually good\nfor " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Explanation
def template_explanation():
    return (capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are not trying\nto " + random.choice(word_collections.verbs_intransitive) + ",\nthey are just trying\nto " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.concepts))

# No need
def template_no_need():
    return (rule() + "You don't need " + random.choice(word_collections.nouns_plural + word_collections.concepts) + "\nto " + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# Potential
def template_potential():
    adj = random.choice(word_collections.adjectives)
    noun = random.choice(word_collections.nouns_singular)
    choice = random.randrange(0, 1, 1)
    phrase = ""
    if choice == 0:
        phrase = "\nSeriously.\n" + capitalize_first_letter_only(a_or_an(adj)) + adj + " " + noun + "."
    else:
        phrase =  ""
    return (horoscope() + "You have the potential\nto become " + a_or_an(noun) + " " + noun + "." + phrase)

# Results
def template_results():
    return (capitalize_first_letter_only(random.choice(word_collections.concepts)) + "\ncan end in " + random.choice(word_collections.concepts))

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
    return (capitalize_first_letter_only(random.choice(word_collections.situations)) + "\nis pretty much like\n" + random.choice(word_collections.verbs_ing) + " your " + random.choice(word_collections.nouns_singular + word_collections.concepts))

# Truth
def template_true():
    return (capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are the " + random.choice(word_collections.concepts) + "\nof all that is " + random.choice(word_collections.adjectives))

# Right
def template_right():
    return (rule() + "Pursue what is " + random.choice(word_collections.adjectives) + "\ninstead of what is\nmaking you " + random.choice(word_collections.adjectives))
    
# Personality
def template_personality():
    temp = random.choice(word_collections.nouns_singular)
    return (horoscope() + "You are\n" + a_or_an(temp) + temp + " " + random.choice(word_collections.people_singular_sfw))

# The best
def function_the_best():
    selected_word = random.choice(word_collections.nouns_singular)
    temp = random.choice(word_collections.adjectives)
    return (rule() + "The best " + selected_word + "\nis " + a_or_an(temp) + temp + " " + selected_word)

# Just be
def template_be():
    temp1 = random.choice(word_collections.nouns_singular)
    temp2 = random.choice(word_collections.adjectives)
    return ("Be " + a_or_an(temp1) + temp1 + "\nBe " + random.choice(word_collections.adjectives) + "\nBe " + a_or_an(temp2) + temp2 + " " + random.choice(word_collections.nouns_singular_sfw))
    
# Judgement
def template_judgement():
	return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are\n" + random.choice(word_collections.times) + " " + random.choice(word_collections.adjectives))

# Watch out!
def template_watch_out():
	return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + "\nare coming for you!")

# The higher, the fewer
def template_higher():
    return (rule() + "The " + random.choice(word_collections.comparatives) + ", the " + random.choice(word_collections.comparatives))

# More you
def template_you_superlative():
    return (horoscope() + "You can be\nthe " + random.choice(word_collections.superlatives) + " " + random.choice(word_collections.nouns_singular))

# Never
def template_never():
    return (rule() + capitalize_first_letter_only(random.choice(word_collections.times)) + " stop\n" + random.choice(word_collections.situations))

# Needs
def template_need():
    temp = random.choice(word_collections.adjectives)
    return (rule() + "You just need\n" + a_or_an(temp) + temp + " " + random.choice(word_collections.nouns_singular))

# You must
def template_must():
    return (rule() + "If you are the " + random.choice(word_collections.superlatives) + " at\n" + random.choice(word_collections.situations) + ",\nyou " + random.choice(word_collections.verbs_mandatory_sfw) + "\n" + random.choice(word_collections.verbs) + " " + random.choice(word_collections.nouns_plural))

# A good day
def template_day():
    return ("Today is a good day\nto " + random.choice(word_collections.verbs))

# LLAP
def template_llap():
    return (rule() + capitalize_first_letter_only(random.choice(word_collections.verbs)) + " " + random.choice(word_collections.adverbs) + "\nand " + random.choice(word_collections.verbs + word_collections.verbs_intransitive))

# Why?
def template_why():
    return ("Why stop " + random.choice(word_collections.verbs_ing) + "\nif you're " + random.choice(word_collections.adjectives) + "?")

# Never
def template_never_again():
    return (rule() + "Never " + random.choice(word_collections.verbs_intransitive) + "\nunless you're willing\nto " + random.choice(word_collections.verbs + word_collections.verbs_intransitive))

# Excuse me
def template_excuse():
    temp1 = random.choice(word_collections.people_singular)
    temp2 = random.choice(word_collections.nouns_singular)
    return ("Excuse me\nWhat does "+ a_or_an(temp1) + temp1 + " want\nwith " + a_or_an(temp2) + temp2 + "?")

# Outweigh
def template_outweigh():
    return (rule() + "The " + random.choice(word_collections.nouns_plural) + "\nof the " + random.choice(word_collections.nouns_plural) + "\noutweigh the " + random.choice(word_collections.nouns_plural) + "\nof the " + random.choice(word_collections.nouns_plural))

# Today
def template_today():
    return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.sometimes)) + ",\nyou will encounter " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Do it
def template_do_it():
    return (horoscope() + "Start " + random.choice(word_collections.verbs_ing) + "\n" + random.choice(word_collections.sometimes))

# They're gonna
def template_gonna():
	return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.nouns_plural)) + " are gonna\n" + random.choice(word_collections.verbs) + " you!")

# There's coffee...
def template_coffee():
	choice = random.randrange(0, 1, 1)
	item = ""
	if choice == 0:
		temp = random.choice(word_collections.food_singular)
		item = a_or_an(temp) + temp
	else:
		item =  random.choice(word_collections.concepts)
	return ("There's " + item + "\nin that " + random.choice(word_collections.nouns_singular))

# The world
def template_world():
    return (horoscope() + capitalize_first_letter_only(random.choice(word_collections.adjectives)) + " " + random.choice(word_collections.nouns_plural) + " are going\nto rule the world.")
    
# Taskmaster
def template_taskmaster():
	adj = random.choice(word_collections.adjectives)
	return (capitalize_first_letter_only(random.choice(word_collections.verbs)) + " " + a_or_an(adj) + adj + " " + random.choice(word_collections.nouns_singular) + ".\nYou have " + str(random.randrange(2, 30, 1)) + " " + random.choice(["seconds", "minutes", "hours", "days"]) + ".\nYour time starts now.")

# Eufemism
def template_eufemism():
    return ("\"" + capitalize_first_letter_only(random.choice(word_collections.nouns_singular)) + "\"\nis just a eufemism for\n\"" + random.choice(word_collections.nouns_singular) + "\"")

# Embrace
def template_embrace():
    temp = random.choice(word_collections.nouns_singular)
    return ("Embrace " + a_or_an(temp) + temp + "\nNot " + random.choice(word_collections.concepts))

# Different people
def template_diff_people():
    people = random.choice(word_collections.people_plural)
    return (capitalize_first_letter_only(random.choice(word_collections.adjectives)) + " " + people + " " + random.choice(word_collections.verbs) + ",\n" + capitalize_first_letter_only(random.choice(word_collections.adjectives)) + " " + people + " " + random.choice(word_collections.verbs))

# Our part
def template_our_part():
    return ("If we all do our part\nwe can\nmake " + random.choice(word_collections.adjectives) + " " + random.choice(word_collections.nouns_plural + word_collections.people_plural) + "\n" + random.choice(word_collections.verbs))

# How to
def template_how_to():
    return (capitalize_first_letter_only(random.choice(word_collections.verbs + word_collections.verbs_intransitive)) + " " + random.choice(word_collections.adverbs))

# You know it
def template_you_know():
    return ("If you know how to\n" + random.choice(word_collections.verbs) + " it,\nyou know how to\n" + random.choice(word_collections.verbs) + " it.")

# Don't avoid
def template_avoid():
    return ("Any " + random.choice(word_collections.people_singular) + "\nwho avoids " + random.choice(word_collections.nouns_plural + word_collections.concepts) + "\n avoids " + random.choice(word_collections.nouns_plural + word_collections.concepts))

# Behind
def template_behind():
    temp = random.choice(word_collections.adjectives)
    return ("Behind every " + random.choice(word_collections.people_singular) + "\nstands\n" + a_or_an(temp) + temp + " " + random.choice(word_collections.people_singular))

# Somebody
def template_somebody():
    return ("Somebody has to " + random.choice(word_collections.verbs + word_collections.verbs_intransitive) + ".\nBe that somebody.")

# You can
def template_you_can():
    temp = random.choice(word_collections.verbs)
    return (rule() + "You can " + temp + "\nwhom you want to " + temp + ".\n" + capitalize_first_letter_only(random.choice(word_collections.people_plural)) + " love you.")

# It be like that
def template_like():
    noun1 = random.choice(word_collections.nouns_singular)
    noun2 = random.choice(word_collections.nouns_singular)
    end = random.choice([capitalize_first_letter_only(a_or_an(noun2) + noun2), capitalize_first_letter_only(random.choice(word_collections.concepts))])
    return (capitalize_first_letter_only(random.choice(word_collections.concepts)) + " is often\nlike " + a_or_an(noun1) + noun1 + ":\n" + end + ".")

# Effect
def template_effect_again():
    noun = random.choice(word_collections.nouns_singular)
    end = random.choice([a_or_an(noun) + noun, random.choice(word_collections.concepts)])
    return (capitalize_first_letter_only(random.choice(word_collections.concepts)) + "\nis usually followed\nby " + end)

# Common
def template_common():
    temp = random.choice(word_collections.nouns_singular)
    return ("What do " + random.choice(word_collections.concepts) + ", " + a_or_an(temp) + " " + temp + ",\nand " + random.choice(word_collections.nouns_plural) + " have in common?\n" + capitalize_first_letter_only(random.choice(word_collections.concepts)) + ".")

# Yes
def template_yes():
    return ("Yes. You are " + random.choice(word_collections.adjectives) + ".")

# Less and more
def template_less_more():
    return (rule() + "The less " + random.choice(word_collections.adjectives) + ",\nthe more " + random.choice(word_collections.adjectives) + ".")

# Almost the same
def template_almost():
    return (capitalize_first_letter_only(random.choice(word_collections.situations)) + "\ncan be quite similar to\n" + random.choice(word_collections.situations))

# Answer
def template_answer():
    return ("The answer to\n" + random.choice(word_collections.situations) + "\nis " + random.choice(word_collections.concepts))

# Cliches
def template_cliches():
    return ("\"" + capitalize_first_letter_only(random.choice(word_collections.cliches)) + "\"\nis just another way to say\n\"" + capitalize_first_letter_only(random.choice(word_collections.cliches)) + "\".")

# Just say it
def template_sayit():
    return ("Sometimes,\nit just needs to be said:\n" + capitalize_first_letter_only(random.choice(word_collections.cliches)))

# List of defined templates (don't forget to add new templates here or they won't be used!)
template_list = [template_times_three, 
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
                 template_gonna,
                 template_coffee,
                 template_world,
                 template_taskmaster,
                 template_eufemism,
                 template_embrace,
                 template_diff_people,
                 template_our_part,
                 template_how_to,
                 template_you_know,
                 template_avoid,
                 template_behind,
                 template_somebody,
                 template_you_can,
                 template_like,
                 template_effect_again,
                 template_common,
                 template_yes,
                 template_less_more,
                 template_almost,
                 template_answer,
                 template_cliches,
                 template_sayit,
                 ]

