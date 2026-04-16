import random
import word_collections
import re

# COMPONENT FUNCTIONS

# Define short names for common components to simplify the templates and save typing time
def noun_singular():
    return random.choice(word_collections.nouns_singular)

def noun_plural():
    return random.choice(word_collections.nouns_plural)

def verb():
    return random.choice(word_collections.verbs)

def verb_intransitive():
    return random.choice(word_collections.verbs_intransitive)

def verb_ing():
    return random.choice(word_collections.verbs_ing)

def verb_mandatory():
    return random.choice(word_collections.verbs_mandatory_sfw)

def adjective():
    return random.choice(word_collections.adjectives)

def adjective_positive():
    return random.choice(word_collections.adjectives_positive)

def adverb():
    return random.choice(word_collections.adverbs)

def times():
    return random.choice(word_collections.times)

def sometimes():
    return random.choice(word_collections.sometimes)

def people_singular():
    return random.choice(word_collections.people_singular)

def people_plural():
    return random.choice(word_collections.people_plural)

def audiences():
    return random.choice(word_collections.audiences)

def prepositions():
    return random.choice(word_collections.prepositions)

def concept():
    return random.choice(word_collections.concepts)

def situation():
    return random.choice(word_collections.situations)

def situation_active():
    return random.choice(word_collections.situations_active)

def comparative():
    return random.choice(word_collections.comparatives)

def superlative():
    return random.choice(word_collections.superlatives)

def food_singular():
    return random.choice(word_collections.food_singular)

def food_plural():
    return random.choice(word_collections.food_plural)

def food_concept():
    return random.choice(word_collections.food_concepts)

def cliche():
    return random.choice(word_collections.cliches)

def amplifier():
    return random.choice(word_collections.amplifiers)

def royalty():
    return random.choice(word_collections.royalty)

def meal():
    return random.choice(word_collections.meals)

def time_unit():
    return random.choice(word_collections.time_units)

# -------------------------------------------------------------------------------------------------------------------

# HELPER FUNCTIONS

# Only touch the first letter
def capitalize_first_letter(phrase):
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
        return ("Today's horoscope - " + capitalize_first_letter(random.choice(word_collections.zodiac)) + ":\n\n")

vowels = ['a', 'e', 'i', 'o', 'u']

def a_or_an(text):
    if text[0] in vowels:
        article = "an "
    else:
        article = "a "
    return article

# --------------------------------------------------------------------------------------------------------------------

# TEMPLATES

# Repeat a random verb three times
def template_times_three():
    current_verb = verb()
    return (current_verb.capitalize() + ", " + current_verb + ", " + current_verb)

# Produce 3 random verbs
def template_three_verbs():
    return (capitalize_first_letter(verb()) + "\n" + verb().capitalize() + "\n" + verb().capitalize())
    
# Row, row, row your boat
def template_row():
    current_verb = verb()
    return (capitalize_first_letter(current_verb) + ", " + current_verb + ", " + current_verb) + "\nyour " + random.choice([noun_singular(), noun_plural()])

# Give three random compliments
def template_three_compliments():
    return (horoscope() + "You are " + adjective_positive() + "\nYou are " + adjective_positive() + "\nYou are " + adjective_positive())

# Give three random characteristics:
def template_three_characteristics():
    return (horoscope() + "You are " + adjective() + "\nYou are " + adjective() + "\nYou are " + adjective())

# Give one random compliment
def template_one_compliment():
    return (horoscope() + capitalize_first_letter(random.choice([times(), sometimes()])) + " forget that \nyou are " + adjective_positive())

# General statement
def template_general():
    return (rule() + "Being " + adjective() + "\nis " + adjective())

# Surprise
def template_surprise_singular():
    return ("Here comes the " + people_singular() + "!")
    
# Surprise 2
def template_surprise_plural():
    return ("Here come the " + people_plural() + "!")

# Call to action
def template_call_to_action():
    return (capitalize_first_letter(people_plural()) + ", rise up!")

# Spread the word
def template_spread_the_word():
    return (horoscope() + capitalize_first_letter(audiences()) + "\nthat you are " + adjective() + ".\nStay " + adjective() + ".")

# Definition
def template_it_does():
    return (horoscope() + capitalize_first_letter(noun_plural()) + " will " + verb() + " you")

# Sharing is caring
def template_share():
    return (rule() + capitalize_first_letter(audiences()) + "\nthat you are " + adjective() + "\nand " + adjective())

# Oh you
def template_you():
    return (horoscope() + "You " + noun_singular())

# Oh adjective you
def template_you_adjective():
    return (horoscope() + "You " + adjective() + " " + noun_singular())

# It can be
def template_can_be():
    return (capitalize_first_letter(noun_plural()) + " can be so\n" + adverb() + " " + adjective())

# No sorry
def template_no_sorry():
    return (rule() + "Don't apologise \nfor being " + adjective())

# Reasons
def template_reasons():
    temp = adjective()
    return ("The fact that you are\n" + a_or_an(temp) + temp + " " + noun_singular() + "\nmakes you " + adjective())

# Deserved
def template_deserved():
    return (capitalize_first_letter(verb()) + ".\nBecause you deserve it.")

# Truth
def template_truth():
    return (capitalize_first_letter(noun_plural()) + " tell it like it is")

# Change
def template_change():
    current_noun = noun_singular()
    temp1 = adjective()
    temp2 = adjective()
    return (rule() + "Don't be " + a_or_an(temp1) + "\n" + temp1 + " " + current_noun + ".\nBe " + a_or_an(temp2) + "\n" +  temp2 + " " + current_noun + ".")
    
# Possibilities
def template_possible():
	return (rule() + "If we can " + verb() + " " + noun_plural() + ",\nwe can " + verb() + " " + noun_plural())

# Effect
def template_effect():
	return (capitalize_first_letter(prepositions()) + " " + noun_plural() + ",\nwe " + verb() + " " + noun_plural() + ".")

# Encouragement
def template_encouragement():
	return (rule() + "Challenge " + random.choice([noun_plural(), people_plural()]) + "\nand act " + adverb() + ".")

# Strangely true
def template_strangely_true():
    temp1 = noun_singular()
    temp2 = noun_singular()
    return (rule() + "Just because you're\n" + a_or_an(temp1) + temp1 + "\nit doesn't mean you're\n" + a_or_an(temp2) + temp2)

# Really
def template_really():
    return (rule() + capitalize_first_letter(random.choice([noun_plural(), concept()])) + ".\nActually good\nfor " + random.choice([noun_plural(), concept()]) + ".")

# Explanation
def template_explanation():
    return (capitalize_first_letter(noun_plural()) + " are not trying\nto " + verb_intransitive() + ",\nthey are just trying\nto " + verb() + " " + concept())

# No need
def template_no_need():
    return (rule() + "You don't need " + random.choice([noun_plural(), concept()]) + "\nto " + verb() + " " + noun_plural())

# Potential
def template_potential():
    adj = adjective()
    noun = noun_singular()
    choice = random.randrange(0, 1, 1)
    phrase = ""
    if choice == 0:
        phrase = "\nSeriously.\n" + capitalize_first_letter(a_or_an(adj)) + adj + " " + noun + "."
    else:
        phrase =  ""
    return (horoscope() + "You have the potential\nto become " + a_or_an(noun) + " " + noun + "." + phrase)

# Results
def template_results():
    return (capitalize_first_letter(concept()) + "\ncan end in " + concept())

# Causation
def template_causation():
    return ("Being " + adjective() + "\ncan cause " + random.choice([noun_plural(), concept()]))

# Two needs
def template_two_needs():
    return (horoscope() + "The two things you need\nin order to live " + adverb() + "\nare " + random.choice([noun_plural(), concept()]) + " and " + random.choice([noun_plural(), concept()]))

# Maybe?
def template_maybe():
    return ("Maybe " + random.choice([noun_plural(), concept()]) + "\ncan turn into " + random.choice([noun_plural(), concept()]) + "\nwhen you get older?")

# Orders
def template_orders():
    return (rule() + "They can order you\nto " + verb() + " " + noun_plural() + ",\nbut they can't order you\nto " + verb() + " " + noun_plural())

# Family
def template_family():
    return (capitalize_first_letter(situation()) + "\nis pretty much like\n" + verb_ing() + " your " + random.choice([noun_singular(), concept()]))

# Truth
def template_true():
    return (capitalize_first_letter(noun_plural()) + " are the " + concept() + "\nof all that is " + adjective())

# Right
def template_right():
    return (rule() + "Pursue what is " + adjective() + "\ninstead of what is\nmaking you " + adjective())
    
# Personality
def template_personality():
    temp = noun_singular()
    return (horoscope() + "You are\n" + a_or_an(temp) + temp + " " + people_singular())

# The best
def function_the_best():
    selected_word = noun_singular()
    temp = adjective()
    return (rule() + "The best " + selected_word + "\nis " + a_or_an(temp) + temp + " " + selected_word)

# Just be
def template_be():
    temp1 = noun_singular()
    temp2 = adjective()
    return ("Be " + a_or_an(temp1) + temp1 + "\nBe " + adjective() + "\nBe " + a_or_an(temp2) + temp2 + " " + noun_singular())
    
# Judgement
def template_judgement():
	return (horoscope() + capitalize_first_letter(noun_plural()) + " are\n" + times() + " " + adjective())

# Watch out!
def template_watch_out():
	return (horoscope() + capitalize_first_letter(noun_plural()) + "\nare coming for you!")

# The higher, the fewer
def template_higher():
    return (rule() + "The " + comparative() + ", the " + comparative())

# More you
def template_you_superlative():
    return (horoscope() + "You can be\nthe " + superlative() + " " + noun_singular())

# Never
def template_never():
    return (rule() + capitalize_first_letter(times()) + " stop\n" + situation())

# Needs
def template_need():
    temp = adjective()
    return (rule() + "You just need\n" + a_or_an(temp) + temp + " " + noun_singular())

# You must
def template_must():
    return (rule() + "If you are the " + superlative() + " at\n" + situation() + ",\nyou " + verb_mandatory() + "\n" + verb() + " " + noun_plural())

# A good day
def template_day():
    return ("Today is a good day\nto " + verb())

# LLAP
def template_llap():
    return (rule() + capitalize_first_letter(verb()) + " " + adverb() + "\nand " + random.choice([verb(), verb_intransitive()]))

# Why?
def template_why():
    return ("Why stop " + verb_ing() + "\nif you're " + adjective() + "?")

# Never
def template_never_again():
    return (rule() + "Never " + verb_intransitive() + "\nunless you're willing\nto " + random.choice([verb(), verb_intransitive()]))

# Excuse me
def template_excuse():
    temp1 = people_singular()
    temp2 = noun_singular()
    return ("Excuse me\nWhat does "+ a_or_an(temp1) + temp1 + " want\nwith " + a_or_an(temp2) + temp2 + "?")

# Outweigh
def template_outweigh():
    return (rule() + "The " + noun_plural() + "\nof the " + noun_plural() + "\noutweigh the " + noun_plural() + "\nof the " + noun_plural())

# Today
def template_today():
    return (horoscope() + capitalize_first_letter(sometimes()) + ",\nyou will encounter " + random.choice([noun_plural(), concept()]))

# Do it
def template_do_it():
    return (horoscope() + "Start " + verb_ing() + "\n" + sometimes())

# They're gonna
def template_gonna():
	return (horoscope() + capitalize_first_letter(noun_plural()) + " are gonna\n" + verb() + " you!")

# There's coffee...
def template_coffee():
	choice = random.randrange(0, 1, 1)
	item = ""
	if choice == 0:
		temp = food_singular()
		item = a_or_an(temp) + temp
	else:
		item =  concept()
	return ("There's " + item + "\nin that " + noun_singular())

# The world
def template_world():
    return (horoscope() + capitalize_first_letter(adjective()) + " " + noun_plural() + " are going\nto rule the world.")
    
# Taskmaster
def template_taskmaster():
	return (capitalize_first_letter(situation_active()) + ".\nYou have " + str(random.randrange(2, 30, 1)) + " " + time_unit() + ".\nYour time starts now.")

# Eufemism
def template_eufemism():
    return ("\"" + capitalize_first_letter(noun_singular()) + "\"\nis just a eufemism for\n\"" + noun_singular() + "\"")

# Embrace
def template_embrace():
    temp = noun_singular()
    return ("Embrace " + a_or_an(temp) + temp + "\nNot " + concept())

# Different people
def template_diff_people():
    people = people_plural()
    return (capitalize_first_letter(adjective()) + " " + people + " " + verb() + ",\n" + capitalize_first_letter(adjective()) + " " + people + " " + verb())

# Our part
def template_our_part():
    return ("If we all do our part\nwe can make\n" + adjective() + " " + random.choice([noun_plural(), people_plural()]) + " " + verb_intransitive())

# How to
def template_how_to():
    return (capitalize_first_letter(random.choice([verb(), verb_intransitive()])) + " " + adverb())

# You know it
def template_you_know():
    return ("If you know how to\n" + verb() + " it,\nyou know how to\n" + verb() + " it.")

# Don't avoid
def template_avoid():
    return ("Any " + people_singular() + "\nwho avoids " + random.choice([noun_plural(), concept()]) + "\n avoids " + random.choice([noun_plural(), concept()]))

# Behind
def template_behind():
    temp = adjective()
    return ("Behind every " + people_singular() + "\nstands\n" + a_or_an(temp) + temp + " " + people_singular())

# Somebody
def template_somebody():
    return ("Somebody has to " + random.choice([verb(), verb_intransitive()]) + ".\nBe that somebody.")

# You can
def template_you_can():
    temp = verb()
    return (rule() + "You can " + temp + "\nwhom you want to " + temp + ".\n" + capitalize_first_letter(people_plural()) + " love you.")

# It be like that
def template_like():
    noun1 = noun_singular()
    noun2 = noun_singular()
    end = random.choice([capitalize_first_letter(a_or_an(noun2) + noun2), capitalize_first_letter(concept())])
    return (capitalize_first_letter(concept()) + " is often\nlike " + a_or_an(noun1) + noun1 + ":\n" + end + ".")

# Effect
def template_effect_again():
    noun = noun_singular()
    end = random.choice([a_or_an(noun) + noun, concept()])
    return (capitalize_first_letter(concept()) + "\nis usually followed\nby " + end)

# Common
def template_common():
    temp = noun_singular()
    return ("What do " + concept() + ",\n" + a_or_an(temp) + " " + temp + ", and " + noun_plural() + "\nhave in common?\n" + capitalize_first_letter(concept()) + ".")

# Yes
def template_yes():
    return ("Yes. You are " + adjective() + ".")

# Less and more
def template_less_more():
    return (rule() + "The less " + adjective() + ",\nthe more " + adjective() + ".")

# Almost the same
def template_almost():
    return (capitalize_first_letter(situation()) + "\ncan be quite similar to\n" + situation())

# Answer
def template_answer():
    return ("The answer to\n" + situation() + "\nis " + concept())

# Cliches
def template_cliches():
    return ("\"" + capitalize_first_letter(cliche()) + "\"\nis just another way to say\n\"" + capitalize_first_letter(cliche()) + "\".")

# Just say it
def template_sayit():
    return ("Sometimes,\nit just needs to be said:\n" + capitalize_first_letter(cliche()))

# It's hard
def template_hard():
    temp = noun_singular()
    return (capitalize_first_letter(concept()) + " is hard,\n" + random.choice([concept(), a_or_an(temp) + temp]) + " makes it better.")

# Percent
def template_percent():
    return (capitalize_first_letter(noun_plural()) + " are\n" + str(random.randrange(1, 200, 1)) + "% " + concept())

# Becoming
def template_become():
    return (horoscope() + "Make " + random.choice([concept(), noun_plural()]) + "\nbecome " + random.choice([concept(), noun_plural()]))

# Not just
def template_not_just():
    temp1 = noun_singular()
    temp1 = a_or_an(temp1) + temp1
    temp2 = noun_singular()
    temp2 = a_or_an(temp2) + temp2
    return (capitalize_first_letter(temp1) + " is never\njust " + temp1 + ".\n" + capitalize_first_letter(temp2) + " is never\njust " + temp2 + ".")

# Involvement
def template_involvement():
    temp = verb_ing()
    return (capitalize_first_letter(temp) + " each other\ninvolves\n" + temp + " ourselves.")

# Forms
def template_form():
    return (capitalize_first_letter(concept()) + " can be\na form of " + concept() + ".")
    
# Recipe
def template_recipe():
	food = food_singular()
	return ("Mix " + food_plural() + ", " + food_singular() + " slices,\nand " + food_concept() + " with " + a_or_an(food) + food + "\nfor a delicious " + meal())
	
# Contents
def template_contents():
    food = food_singular()
    return (capitalize_first_letter(concept()) + "?\nThat's just " + food_concept() + ",\na " + "tiny bit of " + random.choice([food_singular(), concept()]) + "\nand some " + food_concept() + ".")
	
# Ingredients
def template_ingredients():
	return (capitalize_first_letter(food_concept()) + " is\n" + str(random.randrange(1, 110, 1)) + "%  " + food_plural() + "\nand " + str(random.randrange(1, 110, 1)) + "% " + food_singular() + ".") 
	
# Necessity
def template_necessity():
	temp = noun_singular()
	return (rule() + "You need " + random.choice([noun_plural(), a_or_an(temp) + temp]) + "\nto " + situation_active() + ".")
	
# Peanuts
def template_peanuts():
	return ("Any " + random.choice([people_singular(), noun_singular()]) + "\ncan " + situation_active())

# Ready
def template_ready():
    return ("Get ready for " + random.choice([concept(), noun_plural()]) + "!")

# They do
def template_they_do():
    persons = people_plural()
    return (capitalize_first_letter(adjective()) + " " + persons + " " + verb() + "\nwhat " + adjective() + " " + persons + " " + verb())

# Do both
def template_do_both():
    return (capitalize_first_letter(random.choice([verb(), verb_intransitive()])) + " and " + random.choice([verb(), verb_intransitive()]))

# Irish insult
def template_irish_insult():
    return ("You " + amplifier() + " " + noun_singular() + "!")

# Weirdness
def template_weird():
    noun = noun_singular()
    return ("You are " + a_or_an(noun) + noun + "-" + verb_ing() + "\n" + noun_singular() + " " + people_singular() + "!")

# Ornate
def template_ornate():
    return ("You are the " + royalty() + "\nof " + concept() + "\nand " + noun_plural())

# Utter
def template_utter():
    return (capitalize_first_letter(concept()) + " is\n" + amplifier() + " " + concept())

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
                 template_hard,
                 template_percent,
                 template_become,
                 template_not_just,
                 template_involvement,
                 template_form,
                 template_recipe,
                 template_contents,
                 template_ingredients,
                 template_necessity,
                 template_peanuts,
                 template_ready,
                 template_they_do,
                 template_do_both,
                 template_irish_insult,
                 template_weird,
                 template_utter,
                 ]

