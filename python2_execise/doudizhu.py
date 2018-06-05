# 模拟斗地主发牌，共54张扑克
# 黑桃('\u2660'),梅花('\u2663'),方块('\u2665'),红桃('\u2666')
# A2-10JQK 和大小王
# 三个人，每个人发17张牌，底牌留3张
# 输入回车，打印第1个人的17张牌
# 输入回车，打印第2个人的17张牌
# 输入回车，打印第3个人的17张牌
# 输入回车，打印三张底牌
# print('\u2660')在linux环境下可以打印出黑桃图案
import random
players=[]
#黑桃('\u2660'),梅花('\u2663'),方块('\u2665'),红桃('\u2666')
cardType=["\u2660","\u2663","\u2665","\u2666"]

cards=['king','queen']
import pdb
pdb.set_trace()
def generateCards():
    c = ['J', 'Q', 'K', 'A']
    for num in range(2,11):
        c.append(str(num))
    m = map(combinCardType,c)
    for x in m:
        for j in x:
            cards.append(j)

def combinCardType(num):
    card =[]
    for type in cardType:
        card.append(type+num)
    # print(card)
    return card

def initPlayers():
    #playerNum =  input('checking how many players:')
    playerNum = 3
    p=[]
    for id in range(1,playerNum+1):
        playStr ="player"+str(id)
        p.append(playStr)
    return p

def deliverycard():
    generateCards()
    p = initPlayers()
    random.shuffle(cards)
    playerCard=[]
    print(cards[0:17])
    print(cards[18:18+17])
    print(cards[35:35+17])
    print(cards[-1:-4:-1])

from mypackage import menu as m
m.menu()

deliverycard()
# initPlayers()
# for x in player:
#     print(x)

