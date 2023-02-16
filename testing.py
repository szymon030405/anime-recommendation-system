from AnilistPython import Anilist

anilist = Anilist()

# TEST CODE FOR SEEING ALL ANIME DETAILS
responses = [anilist.get_anime("Black Clover"), anilist.get_anime("ONE PIECE")]

for i in range(0, len(responses)):
    for key, value in responses[i].items():
        print(f'{key}: {value}')
    print("------------------------------------------------------------------")


