from User import User
#from Plataform import Platform, StrategySpotifyFree, StrategyAmazon, StrategyDisney, StrategyHBO, StrategyNetflix, StrategySpotify
from Plataform import Platform, StrategySpotifyFree,  StrategySpotifyPremium
 
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





#TODO Revisar notify
#TODO Cambiar sistema de pago para tomar en cuenta la cuenta de los meses
#TODO Implementar response en .txt
