from AnilistPython import Anilist

import lists

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

startYear = 0
endYear = 0

isAiring = ""
while isAiring.lower() != "yes" and isAiring.lower() != "no":
    isAiring = input("Should the anime currently be airing?: Only enter yes or no. ")


if isAiring.lower() == "no":
    while startYear < 1980 or endYear > 2023:
        startYear = input("Enter a preferred year range, starting with the earliest year: ")
        endYear = input ("Enter the latest year: ")
        startYear = int(startYear)
        endYear = int(endYear)

yearRange = list(range(startYear, endYear))

preferredEpisodes = input("Enter the preferred number of episodes: ")
#customDesc = input("Enter a custom description: ")
preferredEpisodes = int(preferredEpisodes)

#mainstreamCheck = ""
#while mainstreamCheck.lower() != "mainstream only" and mainstreamCheck.lower() != "mix" and mainstreamCheck.lower() != "no mainstream":
    #mainstreamCheck = input("Should the results only be mainstream, exclude all mainstream anime, or be a mix of both? Valid options - 'mix','mainstream only', 'no mainstream' :")

#if mainstreamCheck.lower() == "mainstream only":
   # mainstreamCheck = True
#elif mainstreamCheck.lower() == "no mainstream":
   # mainstreamCheck = False

animeMatches = aniList.search_anime(genre = genres, year = yearRange, score = range(70,100))
animeMatches = sorted(animeMatches,key = lambda x: x['average_score'])

animeMatchesAiring = aniList.search_anime(genre = genres, year = ["None", "None"],score = range(70,100)) #FIXME
animeMatchesAiring = sorted(animeMatches,key = lambda x: x['average_score'])

highestSimilarityScores = {} # dictionary mapping anime names to similarity scores

if isAiring.lower() == "yes":
    for anime in animeMatchesAiring:
        if anime["airing_status"].lower() == "releasing": #FIXME - anime["next_airing_ep"]["episode"] not working
                similarityScore = (0.45 * (anime["average_score"]/100)) +   (0.3 * ( abs(preferredEpisodes - anime["next_airing_ep"]["episode"])/preferredEpisodes)) + (0.2 * ((len(genres))/len(anime["genres"])))
        else:
             similarityScore = 0
        if similarityScore > 75:
            highestSimilarityScores[anime["name_romaji"]] = similarityScore 


else:
    for anime in animeMatches:
        if anime["airing_episodes"] != None:
            if anime["airing_episodes"] > preferredEpisodes:
                similarityScore = (0.4 * (anime["average_score"]/100)) + 0.15 +  (0.3 * (abs(preferredEpisodes - anime["airing_episodes"])/preferredEpisodes)) +  (0.15 * ((len(genres))/len(anime["genres"])))
            else:
                similarityScore = (0.4 * (anime["average_score"]/100)) + 0.15 +  (0.3 * (abs(anime["airing_episodes"]-preferredEpisodes)/(preferredEpisodes))) +  (0.15 * ((len(genres))/len(anime["genres"])))
            similarityScore *= 100
        if similarityScore > 100:
            similarityScore = 100;
        if similarityScore > 75:
            highestSimilarityScores[anime["name_romaji"]] = similarityScore 
        
        
        
print ("Now printing animes with the highest similarity scores: \n")
highestSimilarityScores = {k: v for k, v in sorted(highestSimilarityScores.items(), key=lambda x: x[1], reverse=True)}

count = 0
for anime, score in highestSimilarityScores.items():
    if count <= 10:
        print (anime, "|| Similarity Score: " , round(score,1) , "% \n")
    count += 1
    






