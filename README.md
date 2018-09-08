# RankSystem
Ranking system exercise based on DMC Discord group.

This design exercise is intended to break apart the way a "style" system would work in games similar to Devil May Cry. These systems rank a player for activities performed within a certain time frame. As a user continues to perform well in a limited amount of time, the rank they carry and the bonuses granted change to reflect said actions.

Technical notes:  

- StyleRank uses the Pyglet library for sound and image display : https://bitbucket.org/pyglet/pyglet/wiki/Home
- implements common modules os, time and threading
- StyleRank is intended to be used with Python3. This is due to decisions made around threading which are noticeably better supported in Python 3
