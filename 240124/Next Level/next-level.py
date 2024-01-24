class Player:
    def __init__(self,ID='codetree',level=10):
        self.ID = ID
        self.level = level

player1 = Player()
player2 = Player()

new_id, new_level = input().split()

player2.ID = new_id
player2.level = int(new_level)

print("user",player1.ID,"lv",player1.level,end=' ')
print()
print("user",player2.ID,"lv",player2.level,end=' ')