from matplotlib import font_manager 

def get_font(name):
    font_path = font_manager.findfont(font_manager.FontProperties(family=name))
    font_props = font_manager.FontProperties(fname=font_path)
    font_name = font_props.get_name()
    return font_name

# Obtener una lista de todas las fuentes instaladas en el sistema
fuentes_instaladas = font_manager.findSystemFonts()
fuentes_ordenadas = sorted(fuentes_instaladas, key=lambda x: font_manager.FontProperties(fname=x).get_name())

font_dirs = ["fonts"]  # The path to the custom font file.
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)


lista_fuentes = font_manager.get_font_names()
lista_fuentes_ordenada = sorted(lista_fuentes)
for x in lista_fuentes_ordenada:
    print(x)

