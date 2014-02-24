LEXICON = dict(
    direction = ["north", "south", "east", "west",
                "down", "up", "left", "right", "back"],
    verb = ["go", "stop", "kill", "eat"],
    stop = ["the", "in", "of", "from", "at", "it"],
    noun = ["door", "bear", "princess", "cabinet"],
    number = [i for i in range(10)]
)

def scan(words):
    result = []

    for word in words.split():
        found_category = 'error'
        for category, category_lexicon in LEXICON.items():
            if word in category_lexicon:
                found_category = category
                break

        result.append((found_category, word))

    return result