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

def quantifier():
	return random.choice(word_collections.quantifiers)

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
        return f"Rule {str(random.randrange(1, 12, 1))}:\n\n"

def horoscope():
    result = (random.randrange(1, 8, 1))
    if result !=1:
        return ""
    else:
        return f"Today's horoscope - {capitalize_first_letter(random.choice(word_collections.zodiac))}:\n\n"

vowels = ['a', 'e', 'i', 'o', 'u']

def a_or_an(text):
    if text[0] in vowels:
        article = "an"
    else:
        article = "a"
    return article

# --------------------------------------------------------------------------------------------------------------------

# TEMPLATES

# Repeat a random verb three times
def template_times_three():
    current_verb = verb()
    return f"{current_verb.capitalize()}, {current_verb}, {current_verb}"

# Produce 3 random verbs
def template_three_verbs():
    return f'''{capitalize_first_letter(verb())}
    {verb().capitalize()}
    {verb().capitalize()}'''
    
# Row, row, row your boat
def template_row():
    current_verb = verb()
    return f'''{capitalize_first_letter(current_verb)}, {current_verb}, {current_verb}
    your {random.choice([noun_singular(), noun_plural()])}'''

# Give three random compliments
def template_three_compliments():
    return f'''{horoscope()}You are {adjective_positive()}
    You are {adjective_positive()}
    You are {adjective_positive()}'''

# Give three random characteristics:
def template_three_characteristics():
    return f'''{horoscope()}You are {adjective()}
    You are {adjective()}
    You are {adjective()}'''

# Give one random compliment
def template_one_compliment():
    return f'''{horoscope()}{capitalize_first_letter(random.choice([times(), sometimes()]))} forget that
    you are {adjective_positive()}'''

# General statement
def template_general():
    return f'''{rule()}Being {adjective()}
    is {adjective()}'''

# Surprise
def template_surprise_singular():
    return f"Here comes the {people_singular()}!"
    
# Surprise 2
def template_surprise_plural():
    return f"Here come the {people_plural()}!"

# Call to action
def template_call_to_action():
    return f"{capitalize_first_letter(people_plural())}, rise up!"

# Spread the word
def template_spread_the_word():
    return f'''{horoscope()}{capitalize_first_letter(audiences())}
    that you are {adjective()}.
    Stay {adjective()}.'''

# Definition
def template_it_does():
    return f'''{horoscope()}{capitalize_first_letter(noun_plural())} will {verb()} you.'''

# Sharing is caring
def template_share():
    return f'''{rule()}{capitalize_first_letter(audiences())}
    that you are {adjective()}
    and {adjective()}'''

# Oh you
def template_you():
    return f'''{horoscope()}You {noun_singular()}'''

# Oh adjective you
def template_you_adjective():
    return f'''{horoscope()}You {adjective()} {noun_singular()}'''

# It can be
def template_can_be():
    return f'''{capitalize_first_letter(noun_plural())} can be so
    {adverb()} {adjective()}'''

# No sorry
def template_no_sorry():
    return f'''{rule()}Don't apologise
    for being {adjective()}'''

# Reasons
def template_reasons():
    temp = adjective()
    return f'''The fact that you are
    {a_or_an(temp)} {temp} {noun_singular()}
    makes you {adjective()}'''

# Deserved
def template_deserved():
    return f'''{capitalize_first_letter(verb())}.
    Because you deserve it.'''

# Truth
def template_truth():
    return f'''{capitalize_first_letter(noun_plural()) }
    tell it like it is'''

# Change
def template_change():
    current_noun = noun_singular()
    temp1 = adjective()
    temp2 = adjective()

    return f'''{rule()}Don't be {a_or_an(temp1)}
    {temp1} {current_noun}.
    Be {a_or_an(temp2)}
    {temp2} {current_noun}.'''
    
# Possibilities
def template_possible():
	return f'''{rule()}If we can {verb()} {noun_plural()},
    we can {verb()} {noun_plural()}'''

# Effect
def template_effect():
	return f'''{capitalize_first_letter(prepositions())} {noun_plural()},
    we {verb()} {noun_plural()}.'''

# Encouragement
def template_encouragement():
	return f'''{rule()}Challenge {random.choice([noun_plural(), people_plural()])}
    and act {adverb()}.'''

# Strangely true
def template_strangely_true():
    temp1 = noun_singular()
    temp2 = noun_singular()

    return f'''{rule()}Just because you're
    {a_or_an(temp1)} {temp1}
    it doesn't mean you're
    {a_or_an(temp2)} {temp2}'''

# Really
def template_really():
    return f'''{rule()}{capitalize_first_letter(random.choice([noun_plural(), concept()]))}.
    Actually good
    for {random.choice([noun_plural(), concept()])}.'''

# Explanation
def template_explanation():
    return f'''{capitalize_first_letter(noun_plural())} are not trying
    to {verb_intransitive()},
    they are just trying
    to {verb()} {concept()}'''

# No need
def template_no_need():
    return f'''{rule()}You don't need {random.choice([noun_plural(), concept()])}
    to {verb()} {noun_plural()}'''

# Potential
def template_potential():
    adj = adjective()
    noun = noun_singular()
    choice = random.randrange(0, 1, 1)
    phrase = ""
    if choice == 0:
        phrase = f'''Seriously.
        {capitalize_first_letter(a_or_an(adj))} {adj} {noun}.'''
    else:
        phrase =  ""

    return f'''{horoscope()}You have the potential
    to become {a_or_an(noun)} {noun}.
    {phrase}'''

# Results
def template_results():
    return f'''{capitalize_first_letter(concept())}
    can end in {concept()}'''

# Causation
def template_causation():
    return f'''Being {adjective()}
    can cause {random.choice([noun_plural(), concept()])}'''

# Two needs
def template_two_needs():
    return f'''{horoscope()}The two things you need
    in order to live {adverb()}
    are {random.choice([noun_plural(), concept()])} and {random.choice([noun_plural(), concept()])}'''

# Maybe?
def template_maybe():
    return f'''Maybe {random.choice([noun_plural(), concept()])}
    can turn into {random.choice([noun_plural(), concept()])}
    when you get older?'''

# Orders
def template_orders():
    return f'''{rule()}They can order you
    to {verb()} {noun_plural()},
    but they can't order you
    to {verb()} {noun_plural()}'''

# Family
def template_family():
    return f'''{capitalize_first_letter(situation())}
    is pretty much like
    {verb_ing()} your {random.choice([noun_singular(), concept()])}'''

# Truth
def template_true():
    return f'''{capitalize_first_letter(noun_plural())} are the {concept()}
    of all that is {adjective()}'''

# Right
def template_right():
    return f'''{rule()}Pursue what is {adjective()}
    instead of what is
    making you {adjective()}'''
    
# Personality
def template_personality():
    temp = noun_singular()

    return f'''{horoscope()}You are
    {a_or_an(temp)} {temp} {people_singular()}'''

# The best
def function_the_best():
    selected_word = noun_singular()
    temp = adjective()

    return f'''{rule()}The best {selected_word}
    is {a_or_an(temp)} {temp} {selected_word}'''

# Just be
def template_be():
    temp1 = noun_singular()
    temp2 = adjective()

    return f'''Be {a_or_an(temp1)} {temp1}
    Be {adjective()}
    Be {a_or_an(temp2)} {temp2} {noun_singular()}'''
    
# Judgement
def template_judgement():
	return f'''{horoscope()}{capitalize_first_letter(noun_plural())} are
    {times()} {adjective()}'''

# Watch out!
def template_watch_out():
	return f'''{horoscope()}{capitalize_first_letter(noun_plural())}
    are coming for you!'''

# The higher, the fewer
def template_higher():
    return f"{rule()}The {comparative()}, the {comparative()}"

# More you
def template_you_superlative():
    return f'''{horoscope()}You can be
    the {superlative()} {noun_singular()}'''

# Never
def template_never():
    return f'''{rule()}{capitalize_first_letter(times())} stop
    {situation()}'''

# Needs
def template_need():
    temp = adjective()
    return f'''{rule()}You just need
    {a_or_an(temp)} {temp} {noun_singular()}'''

# You must
def template_must():
    return f'''{rule()}If you are the {superlative()} at
    {situation()},
    you {verb_mandatory()}
    {verb()} {noun_plural()}'''

# A good day
def template_day():
    return f'''Today is a good day
    to {verb()}'''

# LLAP
def template_llap():
    return f'''{rule()}{capitalize_first_letter(verb())} {adverb()}
    and {random.choice([verb(), verb_intransitive()])}'''

# Why?
def template_why():
    return f'''Why stop {verb_ing()}
    if you're {adjective()}?'''

# Never
def template_never_again():
    return f'''{rule()}Never {verb_intransitive()}
    unless you're willing
    to {random.choice([verb(), verb_intransitive()])}'''

# Excuse me
def template_excuse():
    temp1 = people_singular()
    temp2 = noun_singular()

    return f'''Excuse me
    What does {a_or_an(temp1)} {temp1} want
    with {a_or_an(temp2)} {temp2}?'''

# Outweigh
def template_outweigh():
    return f'''{rule()}The {noun_plural()}
    of the {noun_plural()}
    outweigh the {noun_plural()}
    of the {noun_plural()}'''

# Today
def template_today():
    return f'''{horoscope()}{capitalize_first_letter(sometimes())},
    you will encounter {random.choice([noun_plural(), concept()])}'''

# Do it
def template_do_it():
    return f'''{horoscope()}Start {verb_ing()}
    {sometimes()}'''

# They're gonna
def template_gonna():
	return f'''{horoscope()}{capitalize_first_letter(noun_plural())} are gonna
    {verb()} you!'''

# There's coffee...
def template_coffee():
	choice = random.randrange(0, 1, 1)
	item = ""
	if choice == 0:
		temp = food_singular()
		item = f"{a_or_an(temp)} {temp}"
	else:
		item =  concept()

	return f'''There's {item}
    in that {noun_singular()}'''

# The world
def template_world():
    return f'''{horoscope()}{capitalize_first_letter(adjective())} {noun_plural()} are going
    to rule the world.'''
    
# Taskmaster
def template_taskmaster():
	return f'''{capitalize_first_letter(situation_active())}.
    You have {str(random.randrange(2, 30, 1))} {time_unit()}.
    Your time starts now.'''

# Eufemism
def template_eufemism():
    return f'''\"{capitalize_first_letter(noun_singular())}\"
    is just a eufemism for
    \"{noun_singular()}\"'''

# Embrace
def template_embrace():
    temp = noun_singular()
    return f'''Embrace {a_or_an(temp)} {temp}
    Not {concept()}'''

# Different people
def template_diff_people():
    people = people_plural()
    return f'''{capitalize_first_letter(adjective())} {people} {verb()},
    {capitalize_first_letter(adjective())} {people} {verb()}'''

# Our part
def template_our_part():
    return f'''If we all do our part
    we can make
    {adjective()} {random.choice([noun_plural(), people_plural()])} {verb_intransitive()}'''

# How to
def template_how_to():
    return f"{capitalize_first_letter(random.choice([verb(), verb_intransitive()]))} {adverb()}"

# You know it
def template_you_know():
    return f'''If you know how to
    {verb()} it,
    you know how to
    {verb()} it.'''

# Don't avoid
def template_avoid():
    return f'''Any {people_singular()}
    who avoids {random.choice([noun_plural(), concept()])}
    avoids {random.choice([noun_plural(), concept()])}'''

# Behind
def template_behind():
    adj = adjective()
    return f'''Behind every {people_singular()}
    stands
    {a_or_an(adj)} {adj} {people_singular()}'''

# Somebody
def template_somebody():
    return f'''Somebody has to {random.choice([verb(), verb_intransitive()]) }.
    Be that somebody.'''

# You can
def template_you_can():
    temp = verb()
    return f'''{rule()}You can {temp}
    whom you want to {temp}.
    {capitalize_first_letter(people_plural())} love you.'''

# It be like that
def template_like():
    noun1 = noun_singular()
    noun2 = noun_singular()
    end = random.choice([capitalize_first_letter(f"{a_or_an(noun2)} {noun2}"), capitalize_first_letter(concept())])

    return f'''{capitalize_first_letter(concept())} is often
    like {a_or_an(noun1)} {noun1}:
    {end}.'''

# Effect
def template_effect_again():
    noun = noun_singular()
    end = random.choice([f"{a_or_an(noun)} {noun}", concept()])

    return f'''{capitalize_first_letter(concept())}
    is usually followed
    by {end}'''

# Common
def template_common():
    temp = noun_singular()
    return f'''What do {concept()},
    {a_or_an(temp)} {temp}, and {noun_plural()}
    have in common?
    {capitalize_first_letter(concept())}.'''

# Yes
def template_yes():
    return f"Yes. You are {adjective()}."

# Less and more
def template_less_more():
    return f'''{rule()}The less {adjective()},
    the more {adjective()}.'''

# Almost the same
def template_almost():
    return f'''{capitalize_first_letter(situation())}
    can be quite similar to
    {situation()}'''

# Answer
def template_answer():
    return f'''The answer to
    {situation()}
    is {concept()}'''

# Cliches
def template_cliches():
    return f'''\"{capitalize_first_letter(cliche())}\"
    is just another way to say
    \"{capitalize_first_letter(cliche())}\".'''

# Just say it
def template_sayit():
    return f'''Sometimes,
    it just needs to be said:
    {capitalize_first_letter(cliche())}'''

# It's hard
def template_hard():
    temp = noun_singular()
    return f'''{capitalize_first_letter(concept())} is hard,
    {random.choice([concept(), f"{a_or_an(temp)} {temp}"])} makes it better.'''

# Percent
def template_percent():
    return f'''{capitalize_first_letter(noun_plural())} are
    {str(random.randrange(1, 200, 1))}% {concept()}'''

# Becoming
def template_become():
    return f'''{horoscope()}Make {random.choice([concept(), noun_plural()])}
    become {random.choice([concept(), noun_plural()])}'''

# Not just
def template_not_just():
    temp1 = noun_singular()
    temp1 = f"{a_or_an(temp1)} {temp1}"
    temp2 = noun_singular()
    temp2 = f"{a_or_an(temp2)} {temp2}"

    return f'''{capitalize_first_letter(temp1)} is never
    just {temp1}.
    {capitalize_first_letter(temp2)} is never
    just {temp2}.'''

# Involvement
def template_involvement():
    temp = verb_ing()
    return f'''{capitalize_first_letter(temp)} each other
    involves
    {temp} ourselves.'''

# Forms
def template_form():
    return f'''{capitalize_first_letter(concept())} can be
    a form of {concept()}.'''
    
# Recipe
def template_recipe():
	food = food_singular()
	return f'''Mix {food_plural()}, {food_singular()} slices,
    and {food_concept()} with {a_or_an(food)} {food}
    for a delicious {meal()}'''
	
# Contents
def template_contents():
    return f'''{capitalize_first_letter(concept())}?
    That's just {food_concept()},
    a tiny bit of {random.choice([food_singular(), concept()])}
    and some {food_concept()}.'''
	
# Ingredients
def template_ingredients():
	return f'''{capitalize_first_letter(food_concept())} is
    {str(random.randrange(1, 110, 1))}% {food_plural()}
    and {str(random.randrange(1, 110, 1))}% {food_singular()}.''' 
	
# Necessity
def template_necessity():
	temp = noun_singular()
	return f'''{rule()}You need {random.choice([noun_plural(), f"{a_or_an(temp)} {temp}"])}
    to {situation_active()}.'''
	
# Peanuts
def template_peanuts():
	return f'''Any {random.choice([people_singular(), noun_singular()])}
    can {situation_active()}'''

# Ready
def template_ready():
    return f"Get ready for {random.choice([concept(), noun_plural()])}!"

# They do
def template_they_do():
    persons = people_plural()
    return f'''{capitalize_first_letter(adjective())} {persons} {verb()}
    what {adjective()} {persons} {verb()}'''

# Do both
def template_do_both():
    return f"{capitalize_first_letter(random.choice([verb(), verb_intransitive()]))} and {random.choice([verb(), verb_intransitive()])}"

# Irish insult
def template_irish_insult():
    return f"You {amplifier()} {noun_singular()}!"

# Weirdness
def template_weird():
    noun = noun_singular()
    return f'''You are {a_or_an(noun)} {noun}-{verb_ing()}
    {noun_singular()} {people_singular()}!'''

# Ornate
def template_ornate():
    return f'''You are the {royalty()}
    of {concept()}
    and {noun_plural()}'''

# Utter
def template_utter():
    return f'''{capitalize_first_letter(concept())} is
    {amplifier()} {concept()}'''

# What do you get
def template_what():
    return f'''What do you get
    when you combine
    {concept()} and {random.choice([concept(), noun_plural()])}?
    {capitalize_first_letter(concept())}.'''

# The same
def template_same():
    people = people_plural()
    verbplural = verb()

    return f'''The {people} who
    {verbplural} {noun_plural()}
    are the same {people}
    who {verbplural} {noun_plural()}'''

# Meaningless
def template_meaning():
    return f'''{capitalize_first_letter(concept())} without {random.choice([concept(), noun_plural()])}
    is meaningless.'''

# Lingo
def template_lingo():
    return f'''\"{capitalize_first_letter(people_singular())}\" comes from
    business lingo and
    means \"{people_singular()}\".'''

# No I
def template_noi():
    return f'''There's no \"I\"
    in \"{random.choice([concept(), noun_singular()])}\".'''

# Or don't
def template_dont():
    passive = verb()
    active = f"{verb()} {noun_plural()}"

    return f'''{capitalize_first_letter(random.choice([passive, active]))}.
    
    Or don't.'''
    
# They do
def template_theydo():
	they = f"{capitalize_first_letter(adjective())} {people_plural()}"

	return f'''{they} {verb_intransitive()}
    {they} {verb_intransitive()}
    {they} really {verb_intransitive()}'''

# Complicated
def template_complicated():
    return f'''{horoscope()}{situation()}
    complicates things'''

# Of course
def template_of_course():
    return f'''Of course you are {adjective_positive()}
    Of course you are {adjective_positive()}
    Of course you are {adjective_positive()}'''

# Attempt
def template_attempt():
    return f'''{concept()}
    is actually our attempt
    at solving the {concept()}
    of {concept()}'''

# Memes
def template_memes():
    return f'''{rule()}Share memes
    about {concept()}'''

# Spread
def template_spread():
    return f'''{horoscope()}Make
    {concept()}
    spread.'''

# Better
def template_better():
    adj1 = adjective()
    adj2 = adjective()
    return f'''{rule()}It's better to be
    {a_or_an(adj1)} {adj1} {noun_singular()}
    than
    {a_or_an(adj2)} {adj2} {noun_singular()}'''

# A thing
def template_athing():
    return f'''Is "{random.choice([adjective(), noun_singular()])} {noun_singular()}" 
    a thing?'''

# Odd
def template_odd():
    return f'''It's {quantifier()} 
    that my {noun_plural()}
    aren't my {noun_plural()}'''

# Will you?
def template_willyou():
    return f'''Will you {verb()}
    my {noun_singular()}?'''

# That's me
def template_thatsme():
    return f'''{noun_plural()},
    {adjective()},
    that's me.'''
	
# Why is it?
def template_whyisit():
    adj = adjective()
    return f'''It's {adj}!
    Why is it {adj}!''' 

# Supposed
def template_supposed():
    return f'''It's {concept()}.
    It's not supposed
    to be {adjective()}.'''

# Tick tock
def template_clock():
    return f'''Tick tock
    {random.choice([concept(), noun_singular()])} o'clock'''

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
                 template_what,
                 template_same,
                 template_meaning,
                 template_lingo,
                 template_noi,
                 template_dont,
                 template_theydo,
                 template_complicated,
                 template_of_course,
                 template_attempt,
                 template_memes,
                 template_spread,
                 template_better,
				 template_athing,
				 template_odd, 
				 template_willyou, 
				 template_thatsme, 
				 template_whyisit, 
				 template_supposed, 
				 template_clock, 
                 ]

