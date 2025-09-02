"""
Author: Brent Goode

Dependency lite and micropython friendly library for interacting with Lyrion 
Music Server (LMS, nee Squezebox Server) systems
https://lyrion.org/reference/lyrion-music-server/
"""

from .micropyLMS import build_url, core_query, get_players, get_player, Player

__all__ = ['build_url','core_query','get_players','get_player','Player']