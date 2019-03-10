import argparse
import sc2reader


'''

--source SOURCE
    Source folder where the replays reside

--dest DEST
    


filename-attributes
    {game-type} : ladder, vsAI, custom, etc.
    {matchup}   : PvP, PvT, PvZ, TvT, TvZ, ZvZ, PPvPP, PTvPP, etc.
    {format}    : 1v1, 2v2, 3v3, 4v4
    {date}      : 2012-8-4
        ex.
            {date:"%Y_%M"}   : 2012_8
            
    {teams}   : NULL vs IIIIllIIl
        {name}   : NULL
        {race}   : P, Z, T
        {result} : W, L
        ex.
            {teams:"{name}({race})"}   : NULL(P) vs IIIIllIIl(Z)
            
    {map}       : Year Zero LE
    {length}    : 20:01
        ex.
            {length:"%M:%S"}   : 20:01

example
    --dest root
    --rename "{date:"%M"}/{game-type}/{format}/{matchup} on {map}: {teams:"{name}({race})"}"

    output:
        root/Aug/ladder/1v1/PvZ on Year Zero LE: NULL(P) vs IIIIllIIl(Z).SC2Replay

'''



