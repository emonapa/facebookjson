from typing import Tuple, Any
import json

def load_memes(filename: str) -> dict[str, Any]:
    with open(filename) as file:
        #memes: dict[str, Any] = json.load(file)
        return json.load(file)

def best_average_subreddit(memes: dict[str, Any]) -> str:
    k = []
    for i in memes['memes']:
        k.append(memes['memes']['subreddit'])
    print(k)
    

def best_from_subreddit(subreddit: str, memes: dict[str, Any]) -> str:
    pass


def best_meme(memes: dict[str, Any]) -> str:
    pass


def analyze_memes(fileName: str) -> Tuple[str, str, str]:
    # TODO
    return ("", "", "")

filename = "C:/Users/mvase/Desktop/pygamy/jsonpicoviny/filename.json"

best_from_subreddit(load_memes(filename))

