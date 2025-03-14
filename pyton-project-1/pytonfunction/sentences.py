# Author:  Kirubel Mekonen Lemu
# Date:  2021-03-14
# Version: 1.0
# Description: This program generates random sentences using functions. The sentences are composed of a determiner, a noun, a verb, and a prepositional phrase. The determiner and noun are randomly chosen to be singular or plural. The verb is randomly chosen to be past, present, or future tense. The prepositional phrase is composed of a preposition, a determiner, and a noun. The program also includes a function that returns a randomly chosen adverb and adjective. The program includes a main function that calls the make_sentence function six times with different parameters to generate six random sentences. The program uses the random module to randomly choose words from lists of determiners, nouns, verbs, prepositions, adverbs, and adjectives
# The program uses the random module to randomly choose words from lists of determiners, nouns, verbs, prepositions, adverbs, and adjectives.
# The program includes a main function that calls the make_sentence function six times with different parameters to generate six random sentences.
# The program includes a function that returns a randomly chosen adverb and adjective.# The program includes a function that returns a randomly chosen adverb and adjective.
# The program also identifies if the indefinite article preceds an adjective that starts with a vowel.
# The program outputs six random sentences with different parameters having tow proposition phrases.
import random

def get_determiner(quantity):
  """Return a randomly chosen determiner. A determiner is
  a word like "the", "a", "one", "some", "many".
  If quantity is 1, this function will return either "a",
  "one", or "the". Otherwise this function will return
  either "some", "many", or "the".
  Parameter
      quantity: an integer.
          If quantity is 1, this function will return a
          determiner for a single noun. Otherwise this
          function will return a determiner for a plural
          noun.
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word



def get_noun(quantity):
  """Return a randomly chosen noun.
  If quantity is 1, this function will
  return one of these ten single nouns:
      "bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"
  Otherwise, this function will return one of
  these ten plural nouns:
      "birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"
  Parameter
      quantity: an integer that determines if
          the returned noun is single or plural.
  Return: a randomly chosen noun.
    """
  if quantity == 1:
      words = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
  else:
      words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
  # Randomly choose and return a noun.
  word = random.choice(words)
  return word



def get_verb(quantity, tense):
  """Return a randomly chosen verb. If tense is "past",
  this function will return one of these ten verbs:
      "drank", "ate", "grew", "laughed", "thought",
      "ran", "slept", "talked", "walked", "wrote"
  If tense is "present" and quantity is 1, this
  function will return one of these ten verbs:
      "drinks", "eats", "grows", "laughs", "thinks",
      "runs", "sleeps", "talks", "walks", "writes"
  If tense is "present" and quantity is NOT 1,
  this function will return one of these ten verbs:
      "drink", "eat", "grow", "laugh", "think",
      "run", "sleep", "talk", "walk", "write"
  If tense is "future", this function will return one of
  these ten verbs:
      "will drink", "will eat", "will grow", "will laugh",
      "will think", "will run", "will sleep", "will talk",
      "will walk", "will write"
  Parameters
      quantity: an integer that determines if the
          returned verb is single or plural.
      tense: a string that determines the verb conjugation,
          either "past", "present" or "future".
  Return: a randomly chosen verb.
  """
  if tense == "past":
      words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
  elif tense == "present" and quantity == 1:
      words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
  elif tense == "present" and quantity != 1:
      words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
  elif tense == "future":
      words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
  # Randomly choose and return a verb.
  word = random.choice(words)
  return word

def get_adverb():
    """Return a randomly chosen adverb
    from this list of adverbs:
    haphazardly, erratically, haphazard, anyhow, irregularly, aimlessly, anywise, desultorily,
    helter-skelter, willy-nilly, hit or miss, at random, anyway, carelessly, every which way, 
    all over the place, any which way, hit-or-miss, unevenly, 
    eccentrically, inconstantly, capriciously, accidentally, casually, higgledy
    quickly, softly, quietly, loudly, slowly, rapidly, suddenly, unexpectedly,
    gently, carefully, carelessly, cautiously, dangerously, easily, fast, hard,
    hastily, immediately, lazily, noisily, politely, quickly, quietly, rapidly,
    reluctantly, safely, suddenly, suspiciously, unexpectedly, very, well, wisely
    Return: a randomly chosen adverb.
    """
    # randomly choose and return an adverb
    words = ["haphazardly", "erratically", "haphazard", "effortlessly", "anyhow", "gracefully", "brightly", "irregularly", "aimlessly", "anywise", "desultorily", "helter-skelter", "willy-nilly", "hit or miss", "at random", "anyway", "carelessly", "every which way", "all over the place", "any which way", "hit-or-miss", "unevenly", "eccentrically", "inconstantly", "capriciously", "accidentally", "casually", "higgledy", "quickly", "softly", "quietly", "loudly", "slowly", "rapidly", "suddenly", "unexpectedly", "gently", "carefully", "carelessly", "cautiously", "dangerously", "easily", "fast", "hard", "hastily", "immediately", "lazily", "noisily", "politely", "quickly", "quietly", "rapidly", "reluctantly", "safely", "suddenly", "suspiciously", "unexpectedly", "very", "well", "wisely"]
    word = random.choice(words)
    return word
def get_adjective():
    """Return a randomly chosen adjective
    from this list of adjectives:
    aback, abaft, abandoned, abased, abashed, abasic, abatable, abatic, abaxial, abbatial,
    abbreviated, abdicable, abdicant, abdicative, abdominal, abdominous, abducent, abducting,
    abecedarian, aberdeen, aberrant, beautiful, witty, wicked ,confusing ,rich,new ,strange ,rocky, 
    circular ,helpful ,competent ,smelly , stable,
    grumpy ,devoted ,smart ,muscular ,graceful ,scary ,safe ,wooden ,sleepy ,tardy ,hungry , strange,
    hopeful ,proud ,new ,dainty ,royal ,arrogant ,round ,efficient ,youthful ,cumbersome ,fickle , mild,
    expensive ,small ,rude ,generous ,courageous ,zany ,thin ,round ,oval ,dark ,hot ,modern ,petite ,weary, 
    old-fashioned, run-of-the-mill ,middle-of-the-road ,heavy-duty ,happy-go-lucky ,see-through ,easy-going ,big-time ,long-term, 
    better, bigger, older, angrier, prettier, smarter, kinder, more determined, more interesting,
    best ,biggest ,oldest ,prettiest ,happiest ,most striking, burnt ,depressed ,surprised ,misunderstood , annoying,
    shocking ,time-consuming, this ,that ,these ,those ,what ,which ,whose ,your ,our ,its ,his ,a ,an ,some ,few ,dozen ,eight ,thousands
    Return: a randomly chosen adjective.
    """
    # randomly choose and return an adjective
    words = ["aback", "abaft", "abandoned", "abased", "abashed", "abasic", "abatable", "abatic", "abaxial", "abbatial", "abbreviated", "abdicable", "abdicant", "abdicative", "abdominal", "abdominous", "abducent", "abducting", "abecedarian", "aberdeen", "aberrant", "beautiful", "witty", "wicked", "confusing", "rich", "new", "strange", "rocky", "circular", "helpful", "competent", "smelly", "stable", "grumpy", "devoted", "smart", "muscular", "graceful", "scary", "safe", "wooden", "sleepy", "tardy", "hungry", "strange", "hopeful", "proud", "new", "dainty", "royal", "arrogant", "round", "efficient", "youthful", "cumbersome", "fickle", "mild", "expensive", "small", "rude", "generous", "courageous", "zany", "thin", "round", "oval", "dark", "hot", "modern", "petite", "weary", "old-fashioned", "run-of-the-mill", "middle-of-the-road", "heavy-duty", "happy-go-lucky", "see-through", "easy-going", "big-time", "long-term", "better", "bigger", "older", "angrier", "prettier", "smarter", "kinder", "more determined", "more interesting", "best", "biggest", "oldest", "prettiest", "happiest", "most striking", "burnt", "depressed", "surprised", "misunderstood", "annoying", "shocking", "time-consuming", "this", "that", "these", "those", "what", "which", "whose", "your", "our", "its", "his", "a", "an", "some", "few", "dozen", "eight", "thousands"]
    word = random.choice(words)
    return word
   
    
    


def get_preposition():
  """Return a randomly chosen preposition
  from this list of prepositions:
      "about", "above", "across", "after", "along",
      "around", "at", "before", "behind", "below",
      "beyond", "by", "despite", "except", "for",
      "from", "in", "into", "near", "of",
      "off", "on", "onto", "out", "over",
      "past", "to", "under", "with", "without"
  Return: a randomly chosen preposition.
  """
  words = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
  # Randomly choose and return a preposition.
  word = random.choice(words)
  return word

def get_prepositional_phrase(quantity):
  """Build and return a prepositional phrase composed
  of three words: a preposition, a determiner, and a
  noun by calling the get_preposition, get_determiner,
  and get_noun functions.
  Parameter
      quantity: an integer that determines if the
          determiner and noun in the prepositional
          phrase returned from this function should
          be single or pluaral.
  Return: a prepositional phrase.
  """
  # Get a preposition, determiner, and noun.
  preposition = get_preposition()
  determiner = get_determiner(quantity)
  noun = get_noun(quantity)
  # Build and return a prepositional phrase.
  phrase = f"{preposition} {determiner} {noun}"
  return phrase 



def make_sentence(quantity, tense):
  """Build and return a sentence with three words:
  a determiner, a noun, and a verb. The grammatical
  quantity of the determiner and noun will match the
  number in the quantity parameter. The grammatical
  quantity and tense of the verb will match the number
  and tense in the quantity and tense parameters.
  """
  # Get a determiner, noun, and verb. 
  determiner = get_determiner(quantity)
  determiner2 = get_determiner(quantity)
  adjective = get_adjective()
  adjective2 = get_adjective()
  # this condition is to check if the indefinite article preceds an adjective starts with a vowel
  if determiner == "a":
      if adjective[0] in "aeiou":
          determiner = "an"
      else:
          determiner = "a"
      
  if determiner2 == "a":
      if adjective2[0] in "aeiou":
          determiner2 = "an"
      else:
          determiner2 = "a"    
      
  noun = get_noun(quantity)
  noun2 = get_noun(quantity)
  verb = get_verb(quantity, tense)
  adverb = get_adverb()
  
  
  prepositional_phrase = get_prepositional_phrase(quantity)
  prepositional_phrase2 = get_prepositional_phrase(quantity)
  # Build and return a sentence.
  #sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
  sentence = f"{determiner.capitalize()} {adjective} {noun} {prepositional_phrase} {adverb} {verb} {determiner2} {adjective2} {noun2} {prepositional_phrase2}."
  return sentence

def main():
    # Call make_sentence function six times with different parameters
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

main()