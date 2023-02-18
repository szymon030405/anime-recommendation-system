from AnilistPython import Anilist
import datetime


# similarity / match percentage : 0.35 * (rating ) + 0.2 *(genres in anime / all genres inputted by user) + 0.15(if the anime is in the year range) + 0.3 (abs(preferredEpisodes-actualEpisodes)/preferredEpisodes) + 
aniList = Anilist()
valid_genres = ['action', 'adventure', 'comedy', 'drama', 'ecchi',
                'fantasy', 'horror', 'mahou', 'shoujo', 'mecha', 'music',
                'mystery', 'psychological', 'romance', 'sci-fi',
                'slice of life', 'sports', 'supernatural', 'thriller']

genre = ""

genres = []
while genre.lower() != "end":
    genre = input("Enter a genre, or type 'end' to stop entering genres: ")
    if genre in valid_genres:
        genres.append(genre)

startYear = input("Enter a preferred year range, starting with the earliest year: ")
endYear = input ("Enter the latest year: ")
startYear = int(startYear)
endYear = int(endYear)

yearRange = list(range(startYear, endYear))

isAiring = ""
while isAiring.lower() != "yes" and isAiring.lower() != "no":
    isAiring = input("Should the anime currently be airing?: Only enter yes or no. ")

preferredEpisodes = input("Enter the preferred number of episodes: ")
#customDesc = input("Enter a custom description: ")
preferredEpisodes = int(preferredEpisodes)


animeMatches = aniList.search_anime(genre = genres, year = yearRange, score = range(70,100))
animeMatches = sorted(animeMatches,key = lambda x: x['average_score'], reverse = True)

animeMatchesAiring = aniList.search_anime(genre = genres, year = yearRange,score = range(70,100)) #FIXME
animeMatchesAiring = sorted(animeMatches,key = lambda x: x['average_score'], reverse = True)

highestSimilarityScores = {} # dictionary mapping anime names to similarity scores

if isAiring.lower() == "yes":
    for anime in animeMatchesAiring:
        if anime["airing_status"].lower() == "releasing": #FIXME - anime["next_airing_ep"]["episode"] not working
            similarityScore = (0.45 * (anime["average_score"]/100)) +   (0.3 * ( abs(preferredEpisodes - anime["next_airing_ep"]["episode"])/preferredEpisodes)) + (0.2 * ((len(genres))/len(anime["genres"])))
        else:
            similarityScore = 0
        if similarityScore > 70:
            highestSimilarityScores[anime["name_romaji"]] = similarityScore 


else:
    for anime in animeMatches:
   
        similarityScore = (0.35 * (anime["average_score"]/100)) + 0.15 +  (0.3 * (abs(preferredEpisodes - anime["airing_episodes"])/preferredEpisodes)) +  (0.2 * ((len(genres))/len(anime["genres"])))
        #(0.35 * (rating ) + 0.2 *(all genres inputted by usergenres in anime ) + 0.15(if the anime is in the year range) + 0.3 (abs(preferredEpisodes-actualEpisodes)/preferredEpisodes) + (0.05 * popularity) + (0.05 * custom Desc match )
        #popularity:  
        similarityScore *= 100
        if similarityScore > 70:
            highestSimilarityScores[anime["name_romaji"]] = similarityScore 
        
        
        
print ("Now printing animes with the highest similarity scores: \n")
highestSimilarityScores = {k: v for k, v in sorted(highestSimilarityScores.items(), key=lambda x: x[1], reverse=True)}

for anime, score in highestSimilarityScores.items():
    print (anime, "|| Similarity Score: " , round(score,1) , "% \n")







