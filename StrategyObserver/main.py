from User import User
from Plataform import Platform, StrategySpotifyFree,  StrategySpotifyPremium, write_on_file, StrategyAmazon, StrategyAmazonPremium, StrategyDisney, StrategyDisneyStart, StrategyHBO, StrategyHBOFree, StrategyNetflix_uno, StrategyNetflix_dos, StrategyNetflix_cuatro
 
 #platforms

spotify = Platform("Spotify", StrategySpotifyPremium())
spotify.attachStrategy_metodos(StrategySpotifyFree())
##  metodo de pago 0 = spotify normal 
##  metodo de pago 1 = spotify free

amazon = Platform("Amazon", StrategyAmazonPremium())
amazon.attachStrategy_metodos(StrategyAmazon())
##  metodo de pago 0 = amazon premium
##  metodo de pago 1 = amazon normal

netflix = Platform("Netflix", StrategyNetflix_uno())
netflix.attachStrategy_metodos(StrategyNetflix_dos())
netflix.attachStrategy_metodos(StrategyNetflix_cuatro())
##  metodo de pago 0 = netflix 1
##  metodo de pago 1 = netflix 2
##  metodo de pago 2 = netflix 4

hbo = Platform("HBO", StrategyHBO())
hbo.attachStrategy_metodos(StrategyHBOFree())
##  metodo de pago 0 = hbo normal 
##  metodo de pago 1 = hbo free

disney = Platform("Disney", StrategyDisney())
disney.attachStrategy_metodos(StrategyDisneyStart())

#Users

Alicia = User("Alicia", 15000)
Bob = User("Bob", 2400)
Cesar = User("Cesar", 5000)
Diego = User("Diego", 9000)
Erika = User("Erika", 10000)
Fausto = User("Fausto", 5000)

#Alicia 
spotify.attach(Alicia, 0)
amazon.attach(Alicia, 0)
netflix.attach(Alicia, 2)
hbo.attach(Alicia, 1)
disney.attach(Alicia, 1)

#Bob
spotify.attach(Bob, 0)
amazon.attach(Bob, 0)
netflix.attach(Bob, 0)
hbo.attach(Bob, 1)
disney.attach(Bob, 1)

#Cesar
disney.attach(Cesar, 1)
hbo.attach(Cesar, 1)

#Diego
hbo.attach(Diego, 1)
amazon.attach(Diego, 1)
spotify.attach(Diego, 1)

#Erika
netflix.attach(Erika, 2)
spotify.attach(Erika, 1)
hbo.attach(Erika, 1)

#Fausto
disney.attach(Fausto, 1)
hbo.attach(Fausto, 1)

for month in range(1,13):
    write_on_file(f"\nMES {month}", "log.txt")
    
    match month:
        case 3:
            disney.detach(Bob)
            hbo.detach(Bob)
            hbo.detach(Erika)
            disney.attach(Erika,1)

            disney.detach(Fausto)
            hbo.detach(Fausto)
            netflix.attach(Fausto, 0)
        case 4:
            netflix.detach(Bob)
            amazon.detach(Bob)

        case 5:
            disney.attach(Fausto, 1)
            hbo.attach(Fausto, 1)
        case 6:
            disney.attach(Diego, 1)

            netflix.detach(Erika)
            spotify.detach(Erika)
            disney.detach(Erika)

            disney.detach(Fausto)
            hbo.detach(Fausto)
            netflix.detach(Fausto)

        case 7:
            spotify.attach(Cesar, 0)
            netflix.attach(Diego, 0)
            amazon.detach(Diego)

        case 10:
            amazon.attach(Erika, 0)
            hbo.attach(Erika, 0)
            disney.attach(Erika, 0)

    write_on_file("\n", "log.txt")
    spotify.execute()
    write_on_file("\n", "log.txt")
    amazon.execute()
    write_on_file("\n", "log.txt")
    netflix.execute()
    write_on_file("\n", "log.txt")
    hbo.execute()
    write_on_file("\n", "log.txt")
    disney.execute()
    write_on_file("\n", "log.txt")





# TE CAMBIA DE PLAN EL SPOTIFY