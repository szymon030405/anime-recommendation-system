from AnilistPython import Anilist

anilist = Anilist()

valid_genres = ['action', 'adventure', 'comedy', 'drama', 'ecchi',
                'fantasy', 'horror', 'mahou', 'shoujo', 'mecha', 'music',
                'mystery', 'psychological', 'romance', 'sci-fi',
                'slice of life', 'sports', 'supernatural', 'thriller']

valid_airing_status = ['releasing', 'finished']

search_params = {  # DICTIONARY FOR SEARCH PARAMETERS
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


def search_animes():
    print(f'----------------------- \n'
          f'SEARCHING ANIMES MATCHING: \n'
          f'GENRES: {search_params["genres"]} \n'
          f'AIRING STATUS: {search_params["airing_status"]}')

    retrieved_animes = anilist.search_anime(genre=search_params["genres"], score=range(70, 100))
    retrieved_animes = sorted(retrieved_animes, key=lambda x: x['average_score'], reverse=True)

    for i in range(len(retrieved_animes) - 1, -1,
                   -1):  # DELETE ANIME DICTIONARY IF AIRING_STATUS KEY DOES NOT MATCH THE SEARCH AIRING_STATUS
        if retrieved_animes[i]["airing_status"].lower() != search_params["airing_status"].lower():
            del retrieved_animes[i]

    print(f'----------------------- \n'
          f'# OF ANIMES RETRIEVED: {len(retrieved_animes)}')

    return retrieved_animes


def show_animes(animes):
    for i in range(0, len(animes)):
        print(f'----------------------- \n'
              f'{animes[i]["name_romaji"]} \n'
              f'{animes[i]["name_english"]} \n'
              f'Rating: {animes[i]["average_score"]} \n'
              f'Airing status: {animes[i]["airing_status"]} \n'
              f'Genres: {animes[i]["genres"]}')


get_search_details()
searched_animes = search_animes()
show_animes(searched_animes)
