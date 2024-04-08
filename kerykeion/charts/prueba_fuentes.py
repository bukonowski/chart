from matplotlib import font_manager 

def get_font(name):
    font_path = font_manager.findfont(font_manager.FontProperties(family=name))
    font_props = font_manager.FontProperties(fname=font_path)
    font_name = font_props.get_name()
    return font_name

#print(get_font("arialawd"))

# Obtener una lista de todas las fuentes instaladas en el sistema
fuentes_instaladas = font_manager.findSystemFonts()

# Imprimir las fuentes instaladas
for x in fuentes_instaladas:
    font_props = font_manager.FontProperties(fname=x)
    font_name = font_props.get_name()
    print(font_name)
    
print("hola""popó")
