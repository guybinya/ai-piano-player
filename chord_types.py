from typing import TypedDict


class Chord(TypedDict):
    chord_name: str
    velocity: int  # 0- 127
    time: int  # in ms
