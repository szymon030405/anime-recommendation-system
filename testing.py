from AnilistPython import Anilist

anilist = Anilist()

# TEST CODE FOR SEEING ALL ANIME DETAILS
responses = [anilist.get_anime("Black Clover"), anilist.get_anime("ONE PIECE")]

for i in range(0, len(responses)):
    for key, value in responses[i].items():
        print(f'{key}: {value}')
    print("------------------------------------------------------------------")

for i in range(10,0,-1):
    print(i)

animes = anilist.search_anime(genre="Sports", score=range(70, 100))

for i in range(0,len(animes)):
    print(f'{animes[i]["name_romaji"]} \n'
          f'{animes[i]["airing_status"]}')

print(f'# of animes: {len(animes)}')

