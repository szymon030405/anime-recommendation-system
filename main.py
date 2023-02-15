from AnilistPython import Anilist
anilist = Anilist()

response = anilist.get_anime("One Piece")

'''
for key, value in response.items():
    print(f'{key}: {value}')
'''


while True:
    genre = input("Enter a genre")
    anime = anilist.search_anime(genre=[genre],score=range(70,100))
    anime = sorted(anime, key=lambda x: x['average_score'], reverse=True)

    for i in range(0,len(anime)):
        print(anime[i]["name_romaji"])
        print(anime[i]["average_score"])
        print("-----------------------")

    print(f'# of animes retrieved: {len(anime)}')




