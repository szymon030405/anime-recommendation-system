from AnilistPython import Anilist

aniList = Anilist()

blueLock = aniList.get_anime("Blue Lock")

print(blueLock["average_score"])