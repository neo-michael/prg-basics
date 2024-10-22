import letter_counter

def main():
    text = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that kept a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing."
    letter = 'e'
    print(letter_counter.count_letter(text, letter))

if __name__ == "__main__":
    main()