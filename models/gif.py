import random
from pydantic import BaseModel


class Gif(BaseModel):
    url: str
    category: str


gifs = [
    Gif(url="https://tenor.com/view/hello-there-private-from-penguins-of-madagascar-hi-wave-hey-there-gif-16043627", category="hello"),
    Gif(url="https://tenor.com/view/hello-there-baby-yoda-mandolorian-hello-gif-20136589", category="hello"),
]


async def get_random_gif(category: str = None) -> Gif:
    if category:
        return random.choice([gif for gif in gifs if gif.category == category])
    return random.choice(gifs)
