###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# display number of characters
print('Number of characters: ', len(movie))

# display title in capital letters
print(f"Title upper cased: {movie.upper()}")

# display title in small letters
print(f"Title lower cased: {movie.lower()}")

# display how many times the vowel "e" appears in the title
print(f"Letter 'e' appears {movie.count('e')} times.")

# display where in the text is the word "Lord"
print(f"The word 'Lord' is at {movie.find("Lord")}")

# display where in the text is the word "dragon"
print(f"The word 'dragon' is at {movie.find("dragon")}")