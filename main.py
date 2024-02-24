import turtle
import pandas
from scoreboard import Header
from county import County
import random

screen = turtle.Screen()
screen.title("Guess the county")
image = "harta.gif"

screen.addshape(image)
screen.screensize(1000,1000)
turtle.shape(image)

screen.tracer(0)
header = Header()

data = pandas.read_csv("counties.csv")
counties = []
guessed = [False] * 42
chosen = 0  # Inițializăm chosen în afara buclei

header.update()
screen.update()
def click_handler(x, y):
    global chosen  # Permite accesul la variabila globala chosen
    print(chosen)
    if abs(x - counties[chosen].x_cor) < 10 and abs(y - counties[chosen].y_cor) < 10 and not guessed[chosen] :
        counties[chosen].color("green")
        guessed[chosen] = True
        # header.update()
        chosen = random.randint(0, 40)  # Actualizează chosen când un județ este ales
        while guessed[chosen]:
            chosen = random.randint(0, 40)
        row = data.iloc[chosen]
        print(row["county"])
        header.current_county = row["county"]
        header.update()
        screen.update()


screen.onclick(click_handler)

for index, row in data.iterrows():
    county = County()
    counties.append(county)
    county.x_cor = row["county_x_cor"]
    county.y_cor = row["county_y_cor"]
    county.goto(county.x_cor, county.y_cor)

header.current_county = data.iloc[chosen]["county"]
header.update()
screen.update()

turtle.mainloop()
