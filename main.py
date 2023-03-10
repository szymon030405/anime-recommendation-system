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
        self.search_details = {  # DICTIONARY FOR SEARCH PARAMETERS
            "genres": [],
            "airing_year": [2014, 2018],
            "episodes_min": 0,
            "episodes_max": 0,
            "airing_status": ""
        }

        self.anime_list = []

    def get_search_details(self):
        running, flag_g, flag_as, flag_ay = True, True, True, True
        while running:
            while flag_g:
                input_genre = input("Enter a genre, or enter 'end' to stop adding genres ")
                if input_genre.lower() == 'end':
                    flag_g = False
                else:
                    if input_genre.lower() in valid_parameters["valid_genres"]:
                        self.search_details["genres"].append(input_genre)
                        print("GENRE ADDED TO SEARCH PARAMS DICT")
                    else:
                        print("INVALID GENRE, TRY AGAIN")
            while flag_as:
                input_airing_status = input("Releasing, finished, or any ")
                if input_airing_status.lower() in valid_parameters["valid_airing_status"]:
                    self.search_details["airing_status"] = input_airing_status
                    print("AIRING STATUS ADDED TO SEARCH PARAMS DICT")
                    flag_as = False
                else:
                    print("INVALID AIRING STATUS, TRY AGAIN")
            while flag_ay:
                # LET THE USER INPUT START YEAR AND END YEAR OF SEARCH !!!
                pass
                flag_s = False
            running = False

    def print_search_details(self):
        for key, value in self.search_details.items():
            print(f'{key}: {value}')

    def search_animes(self):
        searched_animes = anilist.search_anime(genre=self.search_details["genres"], score=range(69, 100))
        searched_animes = sorted(searched_animes, key=lambda x: x['average_score'], reverse=True)

        # CLEAN UP THIS FOR LOOP BELOW, BY MAKING VARIABLES AND DOING SMTH OTHER THAN NESTED IF STATEMENTS !!!

        for i in range(len(searched_animes)):
            if searched_animes[i]["airing_status"].lower() == self.search_details["airing_status"].lower():
                if int(searched_animes[i]["starting_time"][-4:]) >= self.search_details["airing_year"][0]:
                    if int(searched_animes[i]["ending_time"][-4:]) <= self.search_details["airing_year"][1]:
                        self.anime_list.append(searched_animes[i])

    def show_animes(self):
        running = True

        while running:
            choice = input("Display simple or detailed list? Type ")

            if choice.lower() == 'simple':
                running = False
                print(f'----------------------- \n'
                      f'{len(self.anime_list)} animes found \n'
                      f'Rating | Anime name | Airing years')

                for i in range(0, len(self.anime_list)):
                    name = self.anime_list[i]["name_romaji"]
                    score = self.anime_list[i]["average_score"]
                    start_year = self.anime_list[i]["starting_time"][-4:]
                    end_year = self.anime_list[i]["ending_time"][-4:]

                    print(f'{score} | {name} | ({start_year}-{end_year})')

            elif choice.lower() == 'detailed':
                running = False
                print(f'{len(self.anime_list)} animes found')
                for i in range(0, len(self.anime_list)):
                    print(f'{self.anime_list[i]["name_romaji"]} \n'
                          f'{self.anime_list[i]["name_english"]} \n'
                          f'Rating: {self.anime_list[i]["average_score"]} \n'
                          f'Airing status: {self.anime_list[i]["airing_status"]} \n'
                          f'Genres: {self.anime_list[i]["genres"]} \n'
                          f'Start date: {self.anime_list[i]["starting_time"][-4:]} \n'
                          f'End date: {self.anime_list[i]["ending_time"][-4:]} \n'
                          f'-----------------------')

            else:
                print("INVALID LIST CHOICE, TRY AGAIN")


search_1 = Search()
search_1.get_search_details()
search_1.print_search_details()
search_1.search_animes()
search_1.show_animes()
