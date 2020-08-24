"""
*Student name: Shlomo Yakov
*Student ID: 206322588
*Exercise name: ex7
"""
# imports
import sys
import os

def importData():
    """
    the function load the file and then make a dictionary that the it's keys
    is the movies and the values is the actors in the movies
    in addition it make a set of all the actors and set of all the movies
    *keyword arguments - none
    * return: moviesDic - the dictionary that contain each movie and
    the actors that played in it
    actorsList- a set that contains the names of all actors that play in the
    movies.
    moviesList - a set that contain the names of all the movies in the
    dictionary
    """
    print('Processing...')
    # making the Dictionary and the two sets
    moviesDic = {}
    actorsList = set()
    moviesList=set()
    # opening the file by argument
    file = open(sys.argv[1], 'r')
    # reading each line in the file using this loop
    for line in file:
        #remove the '\n'
        if line[-1:] == '\n':
            line=line[:-1]
        # separate the line to several sections
        section = line.split(',')
        length = len(section)
        # remove the spaces from the first section that he is an actor.
        section[0] = section[0].strip(' ')
        # adding him to actorsList
        actorsList.update([section[0]])
        # loop for the other section of the line that contains movies
        for i in range(1, length):
            # for each section the function remove the spaces
            section[i] = section[i].strip(' ')
            # if the movie is already exist in the moviesList its just updating the actor in the dictionary
            if section[i] in moviesList:
                moviesDic[section[i]].add(section[0])
                continue
            # if not its making a new key in the dictionary that his value is the actor
            moviesDic[section[i]] = set()
            moviesDic[section[i]].update([section[0]])
            # then updating the moviesList
            moviesList.update([section[i]])
    # closing the file
    file.close()
    # return the new values
    return (moviesDic,actorsList,moviesList)
# end of the importData function

def byMovies(moviesDic, moviesList):
    """
    the function ask from the user to select two movies and operator.
    according to the operator the function print to the user name of actors
    if the user chose '&' - it prints the actors who played in both movies
    '|' - it prints the actors who played at least at one of the movies
    '^' - it prints the actors who played just in one of the two movies
    * keyword arguments: moviesDic - the dictionary that contain each movie and
    the actors that played in it
    moviesList - a set that contain the names of all the movies in the
    dictionary
    * return: none
    """
    print("Please select two movies and an operator(&,|,^) separated with ',':")
    movie = input()
    movie = movie.split(',')
    length = len(movie)
    # the operator need to be in the third place
    # valid input is in length 3 after the split
    if length != 3:
        print('Error')
        return;
    # remove the spaces
    for i in range(0, length):
        movie[i] = movie[i].strip(' ')
    operator = movie[2]
    # if one of the movies is not in the list
    if movie[0] not in moviesList or movie[1] not in moviesList:
        print('Error')
        return;
    # if the operator is not one of the 3
    if operator != '|' and operator != '&' and operator != '^':
        print('Error')
        return;
    # according to the operator the actors set filled with the right actors
    if operator == '&':
        actors = moviesDic[movie[0]] & moviesDic[movie[1]]
    if operator == '|':
        actors = moviesDic[movie[0]] | moviesDic[movie[1]]
    if operator == '^':
        actors = moviesDic[movie[0]] ^ moviesDic[movie[1]]
    # turn to a list so it can be sorted
    actors = list(actors)
    if len(actors) == 0:
        print('There are no actors in this group')
        return;
    actors.sort()
    # print by by the right order with ',' separate each actor
    for i in range(0, len(actors) - 1):
        print(actors[i], end='')
        print(', ', end='')
    print(actors[len(actors) - 1])
# end of the byMovie function

def byActor(moviesDic,actorsList,moviesList):
    """
    the function asks from the user to insert
    an actor and then print the actors that played with him
    * keyword arguments: moviesDic - the dictionary that contain each movie and
    the actors that played in it
    actorsList- a set that contains the names of all actors that play in the
    movies.
    moviesList - a set that contain the names of all the movies in the
    dictionary
    * return: none
    """
    print('Please select an actor:')
    actor=input()
    if actor not in actorsList:
        print('Error')
        return;
    # making a new set of the co-actors
    coActors=set()
    # convert the ser of the moviesList to a list we can use the index of the list in the dictionary
    moviesList=list(moviesList)
    # using this loop the function add the actors the played with the actor
    for i in range(0,len(moviesList)):
        if actor in moviesDic[moviesList[i]]:
            coActors = moviesDic[moviesList[i]]|coActors
    # making the coActor to a list so it can be easy to print it by index
    coActors=list(coActors)
    # removing the actor that the user insert that get into the coActor after the '|' operator
    coActors.remove(actor)
    # if there is not actor that played with him
    if len(coActors)==0:
        print('There are no actors in this group')
        return;
    # sort by abc order
    coActors.sort()
    # then print the co-actors in the right order and separate by ','
    for i in range(0, len(coActors) - 1):
        print(coActors[i], end='')
        print(', ', end='')
    print(coActors[len(coActors) - 1])
# end of the byActor function

def newMovie(moviesDic,actorsList,moviesList):
    """
    the function updating the information that
    we have after the changes that the user insert
    * keyword arguments: moviesDic - the dictionary that contain each movie and
    the actors that played in it
    actorsList- a set that contains the names of all actors that play in the
    movies.
    moviesList - a set that contain the names of all the movies in the
    dictionary
    *return: moviesDic- the dictionary after the changes off adding
    new movie or updating a available movie
    actorsList-after the changes that user insert
    moviesList-after the changes that can be if the chose to insert a new
    movie
    """
    print('Please insert a new movie:')
    line=input()
    # separates the line by ','
    line = line.split(',')
    length=len(line)
    # if the separate line has less then 2 parts the input is invalid
    if length < 2:
        print('Error')
        # the function ends
        return (moviesDic, actorsList, moviesList)
    # if the input is valid the function remove the spaces
    line[0]=line[0].strip(' ')
    # create a new set of actors that contains the actors that the user insert
    actors = set()
    for i in range(1, length):
        line[i] = line[i].strip(' ')
    # update the actors set
        actors.update([line[i]])
    # if the movies is already in the dictionary its just updating the actors
    if line[0] in moviesList:
        moviesDic[line[0]] = moviesDic[line[0]] | actors
    # if not it crease a new key in the dictionary
    elif line[0] not in moviesList:
        moviesDic[line[0]]=actors
        # then updating the moviesList
        moviesList.update([line[0]])
    # in each way the actors List needs an update also
    actorsList = actorsList | actors
    # then it returns the update information
    return (moviesDic, actorsList, moviesList)
# end of the newMovie function

def savingData(moviesDic, actors, moviesList):
    """
    the function save the data that the program
    has in the output file. The function print to the file in abc order,
    in each line it has the name of the actor and then the names of the
     movies that he played, all of that in abc order.
    * keyword arguments: moviesDic - the dictionary that contain each movie and
    the actors that played in it
    actors- a set that contains the names of all actors that play in the
    movies.
    moviesList - a set that contain the names of all the movies in the
    dictionary
    * return: none
    """
    # conversion the set of actors and the set of moviesList to list so it can be sorted
    actors = list(actors)
    actors.sort()
    moviesList=list(moviesList)
    moviesList.sort()
    os.chmod(sys.argv[2],0o777)
    # open the file to write using arguments
    file=open(sys.argv[2],"w")
    # using this loop the play list filled with movies that the actor played
    for i in range(0, len(actors)):
        play = []
        for j in range(0, len(moviesList)):
            if actors[i] in moviesDic[moviesList[j]]:
                play.append(moviesList[j])
        # writing the name of the actor first
        file.write(actors[i])
        file.write(', ')
        # then using this loop the it prints the movies
        for j in range(0, len(play) - 1):
            file.write(play[j])
            file.write(', ')
        # after the last movie we need the '\n' and not ','
        file.write(play[len(play) - 1])
        if i < len(actors)-1:
            file.write('\n')
    file.close()
# end of the savingData function
def mainMenu(moviesDic, actorsList, moviesList):
    """
    the function present to the user the operation
    that we have and then according to his choise the function "calls"
    to the right function. the only way to return from that function is if
    the user choose operation number 4 or 5 that end the program
    *keyword argument: moviesDic - the dictionary that contain each movie and
    the actors that played in it
    actors- a set that contains the names of all actors that play in the
    movies.
    moviesList - a set that contain the names of all the movies in the
    dictionary
    * return: none
    """
    # the endless loop that can only break if the
    while 1:
        print("Please select an option:")
        print("1) Query by movies")
        print("2) Query by actor")
        print("3) Insert a new movie")
        print("4) Save and Exit")
        print("5) Exit")
        choose = input()
        # 1-3 the program continue
        if choose is "1":
            byMovies(moviesDic,moviesList)
        elif choose is "2":
            byActor(moviesDic,actorsList,moviesList)
        elif choose is "3":
            moviesDic ,actorsList, moviesList =newMovie(moviesDic, actorsList, moviesList)
        # the program ends
        elif choose is "4":
            savingData(moviesDic,actorsList,moviesList)
            # break the loop
            break;
        elif choose is "5":
            # break the loop
            break;
    # end of the while loop
# end of the savingData function

def main():
    """
     the function calls to the importData
    function and gets from it the information from the file, and then
    calls to mainMenu function
    * keyword arguments: none
    * return: none
    """
    # the values that return from the importData
    moviesDic, actorsList, moviesList= importData()
    mainMenu(moviesDic, actorsList, moviesList)
# end of the main function

# calling the main
main()