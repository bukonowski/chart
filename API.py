from kerykeion.charts.kerykeion_chart_svg import KerykeionChartSVG
from kerykeion.astrological_subject import AstrologicalSubject
from pathlib import Path
# AstrologicalSubject
name = "Rahim"
year = 1945
month = 10
day = 10
hour = 10
minute = 10
city = "Buenos Aires"
nation = "AR"   #Código de país de dos letras

# KerykeionChartSVG
style = "dark"
font = None #String con el nombre de la fuente (debe estar instalada)
bg_image_wheel = None # string con url de imagen
bg_image = None #String con url de imagen
bg_color = None # String con color en cualquier formato admitido por svg

# Variables que no se van a usar pero deben estar presentes
chart_type = "Natal"
SecondSubject = None
output_directory = "output" #Path(__file__).resolve().parent / 'output'


if __name__ == "__main__":
    from kerykeion.utilities import setup_logging   #solo para debug, se puede borrar
    setup_logging(level="debug")                    #solo para debug, se puede borrar
    
    if style.lower() == "bright":
        style = Path("kerykeion\\charts\\bright.json")
    else:
        style = Path("kerykeion\\charts\\dark.json")

    subject = AstrologicalSubject(name, year, month, day, hour, minute, city)
    Chart = KerykeionChartSVG(subject, chart_type, SecondSubject, output_directory, style, font, bg_color, bg_image, bg_image_wheel)

    # Generate SVG
    Chart.makeSVG()



# TODO: Crear API que reciba las variables de arriba (armar el json) (Flask o FastAPI)
# TODO: Limpiar proyecto¿?
# TODO: Devolver el chart con la API

# TODO: Subir el proyecto a koyeb.app (Quizá con la cuenta de chambeadevs)
# TODO: Si usamos la cuenta de chambeadevs hay que hacerle un github

# TODO: Testear API con Postman
# TODO:subir la colección de postman a rapidapi
