from AnilistPython import Anilist

anilist = Anilist()

valid_parameters = {  # DICTIONARY FOR VALID PARAMETERS
    "valid_genres": ['action', 'adventure', 'comedy', 'drama', 'ecchi',
                     'fantasy', 'horror', 'mahou', 'shoujo', 'mecha', 'music',
                     'mystery', 'psychological', 'romance', 'sci-fi',
                     'slice of life', 'sports', 'supernatural', 'thriller'],
    "valid_airing_status": ['releasing', 'finished']
}


class Search:
    def __init__(self):
        self.search_parameters = {  # DICTIONARY FOR SEARCH PARAMETERS
            "genres": [],
            "airing_status": "",
            "min_episodes": 0,
            "max_episodes": 0
        }

        self.anime_list = []

    def get_search_details(self):
        running, flag_g, flag_as, flag_e = True, True, True, True
        while running:
            while flag_g:
                input_genre = input("Enter a genre, or enter 'end' to stop adding genres ")
                if input_genre.lower() == 'end':
                    flag_g = False
                else:
                    if input_genre.lower() in valid_parameters["valid_genres"]:
                        self.search_parameters["genres"].append(input_genre)
                        print("GENRE ADDED TO SEARCH PARAMS DICT")
                    else:
                        print("INVALID GENRE, TRY AGAIN")
            while flag_as:
                input_airing_status = input("Releasing, finished, or any ")
                if input_airing_status.lower() in valid_parameters["valid_airing_status"]:
                    self.search_parameters["airing_status"] = input_airing_status
                    print("AIRING STATUS ADDED TO SEARCH PARAMS DICT")
                    flag_as = False
                else:
                    print("INVALID AIRING STATUS, TRY AGAIN")
            running = False

    def print_search_details(self):
        for key, value in self.search_parameters.items():
            print(f'{key}: {value}')

    def search_animes(self):
        print(f'----------------------- \n'
              f'SEARCHING ANIMES MATCHING: \n'
              f'GENRES: {self.search_parameters["genres"]} \n'
              f'AIRING STATUS: {self.search_parameters["airing_status"]}')

        searched_animes = anilist.search_anime(genre=self.search_parameters["genres"], score=range(69, 100))
        searched_animes = sorted(searched_animes, key=lambda x: x['average_score'], reverse=True)

        for i in range(len(searched_animes) - 1, -1, -1):
            if searched_animes[i]["airing_status"].lower() != self.search_parameters["airing_status"].lower():
                del searched_animes[i]

        self.anime_list = searched_animes

    def show_animes(self):
        running = True

        while running:
            choice = input("Display simple or detailed list? Type ")

            if choice.lower() == 'simple':
                running = False
                print(f'----------------------- \n'
                      f'{len(self.anime_list)} animes found \n'
                      f'Rating | Anime name')
                for i in range(0, len(self.anime_list)):
                    print(f'{self.anime_list[i]["average_score"]} | {self.anime_list[i]["name_romaji"]}')

            elif choice.lower() == 'detailed':
                running = False
                print(f'{len(self.anime_list)} animes found')
                for i in range(0, len(self.anime_list)):
                    print(f'{self.anime_list[i]["name_romaji"]} \n'
                          f'{self.anime_list[i]["name_english"]} \n'
                          f'Rating: {self.anime_list[i]["average_score"]} \n'
                          f'Airing status: {self.anime_list[i]["airing_status"]} \n'
                          f'Genres: {self.anime_list[i]["genres"]} \n'
                          f'-----------------------')

            else:
                print("INVALID LIST CHOICE, TRY AGAIN")


search_1 = Search()
search_1.get_search_details()
search_1.search_animes()
search_1.show_animes()
