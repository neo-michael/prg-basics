translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}

word = input("Enter a word in English").lower().strip()

print(f"The word in polish is: {translations[word]}")
