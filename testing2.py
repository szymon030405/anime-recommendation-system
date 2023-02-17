from AnilistPython import Anilist


# similarity / match percentage : 0.35 * (rating ) + 0.2 *(genres in anime / all genres inputted by user) + 0.15(if the anime is in the year range) + 0.3 (abs(preferredEpisodes-actualEpisodes)/preferredEpisodes) + 
aniList = Anilist()
valid_genres = ['action', 'adventure', 'comedy', 'drama', 'ecchi',
                'fantasy', 'horror', 'mahou', 'shoujo', 'mecha', 'music',
                'mystery', 'psychological', 'romance', 'sci-fi',
                'slice of life', 'sports', 'supernatural', 'thriller']

choice = ""

genres = []
while choice.lower() is not "end":
    genre = input("Enter a genre, or type 'end' to stop entering genres: ")
    if genre in valid_genres:
        genres.append(genre)

startYear = input("Enter a preferred year range, starting with the earliest year: ")
endYear = input ("Enter the latest year")
yearRange = [startYear, endYear]

preferredEpisodes = input("Enter the preferred number of episodes")
customDesc = input("Enter a custom description: ")

animes = aniList.search_anime()
#note : only append the anime if its similarity score is over 75%
highestSimilarityScores = {} # dictionary mapping anime names to similarity scores
for anime in range (0, len(animes)) # list of animes found using the search_anime function
    similarityScore = #(0.35 * (rating ) + 0.2 *(all genres inputted by usergenres in anime ) + 0.15(if the anime is in the year range) + 0.3 (abs(preferredEpisodes-actualEpisodes)/preferredEpisodes) + (0.05 * popularity) + (0.05 * custom Desc match )
    #popularity:  
    # < 250: x1
    # 250 < x < 500 : 0.9x
    # 500 < x < 1000 : 0.8x
    # 1001 < x < 5000 :0.5x
    #  > 5001 : 0.1x
    if (similarityScore > 75){
        highestSimilarityScores[anime["name_romaji"]] = similarityScore
    }




