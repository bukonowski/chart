from matplotlib import font_manager

installed_fonts = font_manager.findSystemFonts()

def get_font(font_name):
    installed_fonts = font_manager.findSystemFonts()
    font = "default"
    for font_dir in installed_fonts:
        if font_name.lower() in font_dir.lower():
            font = font_dir
    return font


#fuente = get_font("arialbd")
#print(fuente)

for x in installed_fonts:
    print(x)

#C:\Windows\Fonts\verdanai.ttf
#arialbd
#calibri