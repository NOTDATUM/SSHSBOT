import random


def dice():
    print("game.py - dice")
    bot1 = random.randrange(1, 7)
    bot2 = random.randrange(1, 7)
    user1 = random.randrange(1, 7)
    user2 = random.randrange(1, 7)

    a = bot1 + bot2
    b = user1 + user2

    if a > b:
        return "DEFEAT", 0xFF0000, str(bot1), str(bot2), str(user1), str(user2), str(a), str(b)
    elif a == b:
        return "DRAW", 0xFAFA00, str(bot1), str(bot2), str(user1), str(user2), str(a), str(b)
    elif a < b:
        return "VICTORY", 0x00ff56, str(bot1), str(bot2), str(user1), str(user2), str(a), str(b)


#gamble code is private
