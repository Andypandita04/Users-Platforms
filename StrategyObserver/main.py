from User import User
#from Plataform import Platform, StrategySpotifyFree, StrategyAmazon, StrategyDisney, StrategyHBO, StrategyNetflix, StrategySpotify
from Plataform import Platform, StrategySpotifyFree,  StrategySpotifyPremium

def write_on_file(texto, nombre_archivo):
    # Asegura que el nombre del archivo tenga la extensión .txt
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"
    
    # Abre el archivo en modo de añadir o crea uno nuevo si no existe, luego escribe el texto en una nueva línea
    with open(nombre_archivo, "a") as archivo:
        archivo.write(texto + "\n")
 
spotify = Platform("Spotify", StrategySpotifyPremium())

spotify.attachStrategy_metodos(StrategySpotifyFree())

## Aqui metodo de pago 0 = spotify normal 
##      metodo de pago 1 = spotidu free

Alicia = User("ALicia", 50)
Leo = User("Leo", 2000)
Chuby = User("Chuby", 300 )

spotify.attach(Alicia,1)
spotify.attach(Leo,1) #spotify free
spotify.attach(Chuby,0)



print("\nMES 1")
spotify.execute()

print("\nMES 2")
spotify.execute()


print("\nMES 3")
spotify.execute()


print("\nMES 4")
spotify.execute()

print("\n\n\n")

spotify.attach(Chuby,0)

print("\nMES 5\n\n")
spotify.execute()


