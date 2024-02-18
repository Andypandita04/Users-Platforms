from User import User
#from Plataform import Platform, StrategySpotifyFree, StrategyAmazon, StrategyDisney, StrategyHBO, StrategyNetflix, StrategySpotify
from Plataform import Platform, StrategySpotifyFree,  StrategySpotifyPremium
 
spotify = Platform(StrategySpotifyPremium())

spotify.attachStrategy_metodos(StrategySpotifyFree())

## Aqui metodo de pago 0 = spotify normal 
##      metodo de pago 1 = spotidu free

Alicia = User("ALicia", 50)
Leo = User("Leo", 2000)
Chuby = User("Chuby", 300 )

print(f"The account has (Alicia): {Alicia.get_money()}")
print(f"The account has (Chuby): {Chuby.get_money()}")

spotify.attach(Alicia,0)
spotify.attach(Leo,1) #spotify free
spotify.attach(Chuby,0)


spotify.execute()

###Alicia.pay(spotify.level("base"), spotify)

print(f"The account has (Alicia): {Alicia.get_money()}")
print(f"The account has (Chuby): {Chuby.get_money()}")


#print(spotify.observers)

spotify.attach(Alicia,0)

#print(spotify.observers)


#TODO Revisar notify
#TODO Cambiar sistema de pago para tomar en cuenta la cuenta de los meses
#TODO Implementar response en .txt
