import random
from urllib import request


def downloadImage(url):
    name = "pic" + str(random.randrange(0, 100)) + url[-4:]
    request.urlretrieve(url, name)


# downloadImage("https://i.pinimg.com/originals/1f/5b/18/1f5b18c9a6abeff04875bec765010c08.jpg")

def downloadCSV(url):
    response = request.urlopen(url)
    lines = str(response.read()).split("\\n")
    fx = open(r'LotsOfData.csv', "w")
    for line in lines:
        fx.write(line + "\n")
    fx.close();


downloadCSV(
    "http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv")
