def f(player1, player2):
    def sum_cards(cards):
        s = 0
        for card in cards:
            if card.lower() in 'akqjt':
                s += 10
            else:
                s += int(card)
        return s
    
    return sum_cards(player1) >= sum_cards(player2)

print(f("AJ972", "AQT72"))
print(f("9532", "K8"))