from kerykeion.charts.kerykeion_chart_svg import KerykeionChartSVG
from kerykeion.astrological_subject import AstrologicalSubject

# AstrologicalSubject
name = "Rahim"
year = 1945
month = 10
day = 10
hour = 10
minute = 10
city = "Berlin"
nation = None   # Falta ver como funciona la nación, GB es la default

# KerykeionChartSVG
style = None # pasar a lowercase. Puede ser dark/bright  (DA ERROR SI LE DAMOS UN STRING, CAMBIAR LOGICA)
font = None #String con el nombre de la fuente (debe estar instalada)
bg_image_wheel = None # string con url de imagen
bg_image = None #String con url de imagen
bg_color = None # String con color en cualquier formato admitido por svg

# Variables que no se van a usar pero deben estar presentes
chart_type = "Natal"
SecondSubject = None
output_directory = None 


if __name__ == "__main__":
    from kerykeion.utilities import setup_logging   #solo para debug, se puede borrar
    setup_logging(level="debug")                    #solo para debug, se puede borrar
    
    subject = AstrologicalSubject(name, year, month, day, hour, minute, city)
    Chart = KerykeionChartSVG(subject, chart_type, SecondSubject, output_directory, style, font, bg_color, bg_image, bg_image_wheel)

    # Generate SVG
    Chart.makeSVG()



# TODO: Crear API que reciba las variables de arriba (armar el json) (Flask o FastAPI)
# TODO: Corregir la lógica en la clase kerykeion para que reciba el tema como un string (usar lowercase)
# TODO: Limpiar proyecto¿?
# TODO: Ver funcionamiento de Nation en la clase AstrologicalSubject
# TODO: Cambiar ouput_path para guardar los chart en la carpeta "output"
# TODO: Devolver el chart con la API
# TODO: Subir el proyecto a koyeb.app (Quizá con la cuenta de chambeadevs)
# TODO: Si usamos la cuenta de chambeadevs hay que hacerle un github
# TODO: Testear API con Postman
# TODO: Dejar de ser pobres
# TODO: Si lo de arriba no se puede, subir la colección de postman a rapidapi
