# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 10
# Description:
# This program simulates a user's music library and lets them add new artists and albums

import MusicLibraryHelper
import random


# Displays list of potential actions
def displayMenu():
    print("\nWelcome to Your Music Library")
    print("Options:")
    print("\t1) Display library\n\t2) Display all artists\n\t3) Add an album\n\t4) Delete an album\n\t"
          "5) Delete an artist\n\t6) Search library\n\t7) Generate a random playlist\n\t8) Make your own playlist"
          "\n\t9) Exit")


# Nicely displays the current artists and albums in the music library
def displayLibrary(musicLibDictionary):
    for key in musicLibDictionary:
        print("Artist: " + key + "\nAlbums:")
        for i in range(len(musicLibDictionary[key])):
            print("\t\t-" + musicLibDictionary[key][i])


# Nicely displays the current artists only in the music library
def displayArtists(musicLibDictionary):
    keys = list(musicLibDictionary.keys())
    print("Displaying all artists:")
    for i in range(len(keys)):
        print("- " + str(keys[i]))


# Add an album if it doesn't exist to library
def addAlbum(musicLibDictionary):
    artist = input("Enter artist: ")
    artistCompare = artist.lower().strip()
    keys = list(musicLibDictionary.keys())
    artistFound = False
    # Loop through dictionary and compare entered artist with existing ones
    for i in range(len(keys)):
        if artistCompare == keys[i].lower().strip():
            artistFound = True
            key = keys[i]

    album = input("Enter album: ")
    albumCompare = album.lower().strip()
    # Only search for album if artist was already found
    if artistFound:
        albumFound = False
        albums = musicLibDictionary[key]
        # Loop through each album, comparing it with the entered value
        for i in range(len(albums)):
            if albumCompare == albums[i].lower().strip():
                albumFound = True
        if not albumFound:
            musicLibDictionary[key] = musicLibDictionary.get(key, []) + [album]
    # Create a new artist and album entry if both are new
    else:
        musicLibDictionary[artist] = [album]


# Delete the album of an existing artist
def deleteAlbum(musicLibDictionary):
    artist = input("Enter artist: ")
    artistCompare = artist.lower().strip()
    keys = list(musicLibDictionary.keys())
    artistFound = False
    for i in range(len(keys)):
        if artistCompare == keys[i].lower().strip():
            artistFound = True
            key = keys[i]

    album = input("Enter album: ")
    albumCompare = album.lower().strip()
    # Can only delete an album if the artist exists
    if artistFound:
        albumFound = False
        albums = musicLibDictionary[key]
        for i in range(len(albums)):
            if albumCompare == albums[i].lower().strip():
                albumFound = True
                del musicLibDictionary[key][i]
                # If this is the final album, delete the artist as well
                if not musicLibDictionary[key]:
                    del musicLibDictionary[key]
                break
    return albumFound


# Completely delete an artist from library
def deleteArtist(musicLibDictionary):
    artist = input("Enter artist to delete: ")
    artistCompare = artist.lower().strip()
    keys = list(musicLibDictionary.keys())
    artistFound = False
    for i in range(len(keys)):
        if artistCompare == keys[i].lower().strip():
            artistFound = True
            del musicLibDictionary[keys[i]]
    return artistFound


# Loop through all artists and albums keeping track of which contain the search term
def searchLibrary(musicLibDictionary):
    term = input("Please enter a search term: ")
    artists = []
    albumsList = []
    termCompare = term.lower().strip()
    keys = list(musicLibDictionary.keys())
    for i in range(len(keys)):
        # If an artist contains the term add it to the list
        if termCompare in keys[i].lower().strip():
            artists.append(keys[i])
        albums = musicLibDictionary[keys[i]]
        # Loop through albums looking for search term
        for j in range(len(albums)):
            if termCompare in albums[j].lower().strip():
                albumsList.append(albums[j])

    # If any artists or albums contained the term, print them out
    print("Artists containing '" + term + "'")
    if not artists:
        print("\t\tNo results")
    else:
        for i in range(len(artists)):
            print("- " + artists[i])

    print("Albums containing '" + term + "'")
    if not albumsList:
        print("\t\tNo results")
    else:
        for i in range(len(albumsList)):
            print("- " + albumsList[i])


# Randomly select one album from each existing artist and add it to list
def generateRandomPlaylist(musicLibDictionary):
    playlist = []
    keys = list(musicLibDictionary.keys())
    for key in musicLibDictionary:
        rand = random.randrange(len(musicLibDictionary[key]))
        playlist.append(musicLibDictionary[key][rand])
    print("Here is your random playlist:")
    for i in range(len(playlist)):
        print("- " + playlist[i] + " by " + keys[i])


def main():
    music = MusicLibraryHelper.loadLibrary("musicLibrary.dat")
    choice = ""
    while choice != "9":
        displayMenu()
        choice = input("> ")
        # Error checking to ensure only values from 1-9 are entered
        while not choice.isdigit() or int(choice) < 1 or int(choice) > 9:
            choice = input("> ")
            if choice.isdigit():
                choice = int(choice)
                if choice < 1 or choice > 9:
                    choice = input("> ")
                else:
                    break;
        if isinstance(choice, str):
            choice = int(choice)
        # Call appropriate function based on user input
        if choice == 1:
            displayLibrary(music)
        elif choice == 2:
            displayArtists(music)
        elif choice == 3:
            addAlbum(music)
        elif choice == 4:
            status = deleteAlbum(music)
            if status:
                print("Delete album success!")
            else:
                print("Delete album failed.")
        elif choice == 5:
            status = deleteArtist(music)
            if status:
                print("Delete artist success!")
            else:
                print("Delete artist failed.")
        elif choice == 6:
            searchLibrary(music)
        elif choice == 7:
            generateRandomPlaylist(music)
        elif choice == 9:
            break

    print("Saving music library...\nGoodbye!")
    MusicLibraryHelper.saveLibrary("musicLibrary1.dat", music)


main()
