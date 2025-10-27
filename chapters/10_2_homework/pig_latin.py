
# Define your global variables and constants here



# word_to_pig_latin: Converts the input string to pig latin and returns the pig latin string
# Input: one string - the word in English
# Return: one string - the word in Pig Latin
def word_to_pig_latin(english):

    # Write your function here


def test_translator():
    pairs = [
        ['boot', 'ootbay'],
        ['image', 'imagehay'],
        ['pig', 'igpay'],
        ['latin', 'atinlay'],
    ]
    for pair in pairs:
        english = pair[0]
        answer = pair[1]
        pl = word_to_pig_latin(english)
        if (pl != answer):
            print(f"Oops!  {english} should translate to {answer}, not {pl} !")