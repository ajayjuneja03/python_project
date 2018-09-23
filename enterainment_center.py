import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys", "Toy_story.jpg","https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.title + "\n")
print(toy_story.storyline + "\n")


Avatar = media.Movie("Avatar" ,"A marine of an alien planet" , "avatar.jpeg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")




rampage = media.Movie("Rampage" , "a rogue genetic experiment gone awry mutates this gentle ape into a raging creature of enormous size" , "rampage.jpg","https://www.youtube.com/watch?v=coOKvrsmQiI")


safe_house = media.Movie("Safe House","The two men must join forces and try to stay alive long enough to figure out who wants them dead.","safe_house.jpg","https://www.youtube.com/watch?v=1IfQY4fNcnw")



london_has_fallen = media.Movie("London Has Fallen","Mike, a Secret Service agent, must find a way to escape with his team when Barkawi, a terrorist, attacks all the world leaders attending the funeral of the British Prime Minister, James Wilson.","london_has_fallen.jpg","https://www.youtube.com/watch?v=3AsOdX7NcJs")




movies = [toy_story , Avatar , rampage , safe_house , london_has_fallen]
fresh_tomatoes.open_movies_page(movies)








