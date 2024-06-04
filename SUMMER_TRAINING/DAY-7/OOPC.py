game=int(input())
player1=input("enter player1:")
player2=input("enter player2:")
while True:
    players=input("Enter the players' results (A or D): ")
    if len(players)==game and all(char in [player1, player2] for char in players):
        break
    else:
        print(f"please enter exact {game} players")
b=[]
c=[]
for i in range(game):
    if players[i]==player1:
        b.append(players[i])
    else:
        c.append(players[i])
if len(b)>len(c):
    print("Anton")
elif len(b)==len(c):
    print("Friendship")
else:
    print("Dhanic")

