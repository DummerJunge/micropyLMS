# micropyLMS

A dependency lite and micropython friendly library for interacting with Lyrion Music Server (LMS) systems

# Overview

This library is intended to help build micropython based LMS controller projects. LMS allows for multiple players to simultaneously play separate streams, most commands and queries have to be represented as coming from one of the players connected to the server. Because of this, the bulk of the library is the player class that allows the creation of an object to hold information about and interaction methods for an LMS player. 

A player object only needs to be created once at startup. Any commands can be issued via the class methods. The various class attributes store some useful information on the last updated status of the player. Other information can be retrieved with the generic ``player_query()`` method. To insure that the information is current the ``status_update()`` method should be called. So for example, if the song playing has moved on since the last ``status_update()`` call the ``player.title``, ``player.artist``, and ``player.album`` information will all refer to that other song.

# Installation

`` pip install micropyLMS

# Example Setup

The following code snippet shows how to initialize and use a simple setup
```
import micropyLMS

host = "192.168.1.5" # Change this to the specific local URL for your LMS server.
player_name = "Lounge" # Change to the name of the specific player. 

server_url = micropyLMS.build_url(host)

player = micropyLMS.get_player(server_url,player_name)
    if player:
        player.status_update()
    else:
        print(f'Error setting up player named {player_name} connected to host at {server_url}')
        # Other code to handle retrying or whatever.

player.set_volume(50) # Sets the volume to half the maximum.
player.play() # Starts the playback. Enjoy your music.
...
```

# Advanced Usage

There are a wide varied of commands and queries that could be issued that are less commonly used than the ones implemented in this library. For that reason, the ``Player`` class has a generic ``player_query()`` method and the library has a generic query function ``core_query()`` for non-player queries. Constructing valid arguments for these function is a little more complicated. For full information how to structure the argument or arguments that go in the place of ``*command`` for these functions see https://lyrion.org/reference/cli/using-the-cli/ under the jsonrpc.js section and the command part of the body of the request.
