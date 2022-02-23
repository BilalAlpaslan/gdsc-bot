import random
from pydantic import BaseModel


class Gif(BaseModel):
    url: str
    category: str


gifs = [
    Gif(url="https://tenor.com/view/hello-there-private-from-penguins-of-madagascar-hi-wave-hey-there-gif-16043627", category="hello"),
    Gif(url="https://tenor.com/view/hello-there-baby-yoda-mandolorian-hello-gif-20136589", category="hello"),
    Gif(url="https://tenor.com/view/hello-gif-20758171", category="hello"),
    Gif(url="https://tenor.com/view/cat-cute-animals-hello-there-gif-11875188", category="hello"),
    Gif(url="https://tenor.com/view/quby-chan-hi-wave-hello-hi-there-gif-17010845", category="hello"),
    Gif(url="https://tenor.com/view/hello-cute-cat-hi-greetings-gif-16242995", category="hello"),
    Gif(url="https://tenor.com/view/sup-hi-hey-bear-animal-gif-23962860", category="hello"),
    Gif(url="https://tenor.com/view/puppy-love-hi-dont-leave-cute-adorable-gif-17101332", category="hello"),
    Gif(url="https://tenor.com/view/hello-dog-hi-cute-cute-dog-gif-14091311", category="hello"),
]


async def get_random_gif(category: str = None) -> Gif:
    if category:
        return random.choice([gif for gif in gifs if gif.category == category])
    return random.choice(gifs)
