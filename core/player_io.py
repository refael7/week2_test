def ask_player_action() -> str:
    word = input("please enter or H or S:")
    if word != 'H' and word != 'S':
        ask_player_action()
    else:
        return word




