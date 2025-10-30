import random
def build_standard_deck() -> list[dict]:
    cards=[]
    arr1=['1','2','3','4','5','6','7','8','9','10','J','K','Q']
    arr2=['H','S','D','C']
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            cards.append({"rank":arr1[i],"suite":arr2[j]})
    return cards

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:

    for i in range(swaps):
        index1=random.randrange(0,51)
        flag = True
        while flag==True:
             index2=random.randrange(0,51)
             temp=deck[index2]
             if temp['suite']=='H':
                if index2 %5!=0:
                 flag=True
             elif temp['suite']=='C':
                if index2 % 3 != 0:
                 flag=True
             elif temp['suite']=='D':
                if index2 %2==0:
                  flag = True
             elif temp['suite']=='s':
                if index2 %7!=0:
                  flag = True
             elif index1 == index2:
                 flag=True
             else:
                deck[index1],deck[index2]=deck[index2], deck[index1]
                flag=False

    return deck


print(build_standard_deck())
print(shuffle_by_suit(build_standard_deck()))