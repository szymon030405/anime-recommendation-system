from AnilistPython import Anilist

anilist = Anilist()

valid_genres = ['action', 'adventure', 'comedy', 'drama', 'ecchi',
                'fantasy', 'horror', 'mahou', 'shoujo', 'mecha', 'music',
                'mystery', 'psychological', 'romance', 'sci-fi',
                'slice of life', 'sports', 'supernatural', 'thriller']

valid_airing_status = ['releasing', 'finished']

search_params = {
    "genres": [],
    "airing_status": "",
    "min_episodes": 0,
    "max_episodes": 0
}


def get_search_details():
    running, flag_g, flag_as, flag_e = True, True, True, True

    while running:
        while flag_g:
            input_genre = input("Enter a genre, or enter 'end' to stop adding genres ")
            if input_genre.lower() == 'end':
                flag_g = False
            else:
                if input_genre.lower() in valid_genres:
                    search_params["genres"].append(input_genre)
                    print("GENRE ADDED TO SEARCH PARAMS DICT")
                else:
                    print("INVALID GENRE, TRY AGAIN")
        while flag_as:
            input_airing_status = input("Releasing, finished, or any ")
            if input_airing_status.lower() in valid_airing_status:
                search_params["airing_status"] = input_airing_status
                print("AIRING STATUS ADDED TO SEARCH PARAMS DICT")
                flag_as = False
            else:
                print("INVALID AIRING STATUS, TRY AGAIN")
        running = False


get_search_details()

print(f'----------------------- \n'
      f'SEARCHING ANIMES MATCHING: \n'
      f'GENRES: {search_params["genres"]}')

anime = anilist.search_anime(genre=search_params["genres"], score=range(70, 100))
anime = sorted(anime, key=lambda x: x['average_score'], reverse=True)

print(f'----------------------- \n'
      f'# of animes retrieved: {len(anime)}')

for i in range(0, len(anime)):
    if anime[i]["airing_status"].lower() == search_params["airing_status"].lower():
        print("-----------------------")
        print(anime[i]["name_romaji"])
        if anime[i]["name_romaji"] != anime[i]["name_english"]:  # PRINT ENGLISH NAME IF DIFFERENT FROM ROMAJI
            print(anime[i]["name_english"])
        print(f'Rating: {anime[i]["average_score"]}')
        print(anime[i]["airing_status"])
        print(anime[i]["genres"])
