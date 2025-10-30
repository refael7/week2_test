from deck import build_standard_deck
def calculate_hand_value(hand: list[dict]) -> int:
    sum = 0
    for i in hand:
        if  i["rank"]=="K" or i["rank"]=="Q" or i["rank"]=="J":
             sum+=10
        else:
            sum+= int(i["rank"])
    return sum

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
     player["hand"]=[deck[0],deck[1]]
     dealer["hand"]=[deck[2],deck[3]]
     print("player:",calculate_hand_value(player["hand"]))
     print("dealer:",calculate_hand_value(dealer["hand"]))
     print(player)
     deck=deck[4:]
     # deck.pop()
def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"])<17:
        dealer["hand"].append(deck[0])
        deck=deck[1:]
    if calculate_hand_value(dealer["hand"])>21:
        return  False
    else:
        return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    print()

# print(calculate_hand_value([{'rank': '7', 'suite': 'D'}]))
(deal_two_each(build_standard_deck(),{},{}))
print(dealer_play(build_standard_deck(), {'hand': [{'rank': '21', 'suite': 'H'}, {'rank': '1', 'suite': 'S'}]}))
