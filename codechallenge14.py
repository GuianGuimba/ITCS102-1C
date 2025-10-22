Loop = True
Anime_list = []

print("Welcome to the \"My Anime List\"\n(Type \"exit\" if you're finnished!)\nPlease input your anime you watched below!")
while Loop == True:
    anime = input("==> ").lower()
    if anime == 'exit':
        break
    else:
        Anime_list.append(anime)
        continue
print("\nYou have exited the anime entry program!\nYour anime list inlcudes:")
Anime_list.sort()
for list in Anime_list:
    print("-",list)
