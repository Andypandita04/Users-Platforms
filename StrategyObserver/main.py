from User import User
from Plataform import Platform, write_on_file, Inter_Spotify, Inter_Amazon, Inter_Disney, Inter_HBO, Inter_Netflix
 
 #platforms

spotify = Platform("Spotify", Inter_Spotify())
spotify.add_recommen(['adele', 'peso pluma', 'morat'])


amazon = Platform("Amazon", Inter_Amazon())
amazon.add_recommen(['Cindy la regia', 'Me gusta pero me asusta', 'El infierno'])

netflix = Platform("Netflix", Inter_Netflix())
netflix.add_recommen(['Black mirror', 'One Piece', 'La asesina del romance'])


hbo = Platform("HBO", Inter_HBO())
hbo.add_recommen(['Nosotros los nobles', 'Ghost in a shell', 'In a loop'])

disney = Platform("Disney",  Inter_Disney())
disney.add_recommen(['Moana', 'Soul', 'Inside Out'])

#Users

Alicia = User("Alicia", 15000)
Bob = User("Bob", 2400)
Cesar = User("Cesar", 5000)
Diego = User("Diego", 9000)
Erika = User("Erika", 10000)
Fausto = User("Fausto", 5000)

#Alicia 
spotify.attach(Alicia, 7)
amazon.attach(Alicia, 5)
netflix.attach(Alicia, 3)
hbo.attach(Alicia, 11)
disney.attach(Alicia, 9)
write_on_file("\n", "log.txt")

#Bob
spotify.attach(Bob, 7)
amazon.attach(Bob, 5)
netflix.attach(Bob, 3)
hbo.attach(Bob, 11)
disney.attach(Bob, 9)
write_on_file("\n", "log.txt")

#Cesar
disney.attach(Cesar, 8)
hbo.attach(Cesar, 10)
write_on_file("\n", "log.txt")

#Diego
hbo.attach(Diego, 10)
amazon.attach(Diego, 5)
spotify.attach(Diego, 6)
write_on_file("\n", "log.txt")

#Erika
netflix.attach(Erika, 3)
spotify.attach(Erika, 6)
hbo.attach(Erika, 10)
write_on_file("\n", "log.txt")

#Fausto
disney.attach(Fausto, 8)
hbo.attach(Fausto, 10)

for month in range(1,13):
    write_on_file(f"\nMES {month}", "log.txt")
    
    match month:
        case 3:
            disney.detach(Bob)
            hbo.detach(Bob)
            hbo.detach(Erika)
            disney.attach(Erika,8)

            disney.detach(Fausto)
            hbo.detach(Fausto)
            netflix.attach(Fausto, 1)
        case 4:
            netflix.detach(Bob)
            amazon.detach(Bob)

        case 5:
            disney.attach(Fausto, 9)
            hbo.attach(Fausto, 11)
        case 6:
            disney.attach(Diego, 8)

            netflix.detach(Erika)
            spotify.detach(Erika)
            disney.detach(Erika)

            disney.detach(Fausto)
            hbo.detach(Fausto)
            netflix.detach(Fausto)

        case 7:
            spotify.attach(Cesar, 7)
            netflix.attach(Diego, 1)
            spotify.attach(Diego,7)
            amazon.detach(Diego)

        case 10:
            amazon.attach(Erika, 4)
            hbo.attach(Erika, 10)
            disney.attach(Erika, 9)

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
