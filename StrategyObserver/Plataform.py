import random as rd

def write_on_file(texto, nombre_archivo):
    # Asegura que el nombre del archivo tenga la extensión .txt
    if not nombre_archivo.endswith(".txt"):
        nombre_archivo += ".txt"
    
    # Abre el archivo en modo de añadir o crea uno nuevo si no existe, luego escribe el texto en una nueva línea
    with open(nombre_archivo, "a") as archivo:
        archivo.write(texto + "\n")



# Interfaz strategy
class Strategy:
    #def __init__(self,name, amount, month_change):
    #    pass

    def execute(self,cuenta):
        pass

    def change_plan(self, cuenta):
        pass

# Clase con todos los metodos strategy implementados
class Strategy_Metodos:
    def __init__(self,name, amount, month_change):
        self.name = name
        self.amount = amount
        self.month_change = month_change
  
    #Este metodo devuelve un booleano, verifica y realiza el pago del servicio 
    def execute(self,cuenta):
        cuenta.increase_month()

        #Checo si el cliente tiene dinero suficiente
        money_cuenta = cuenta.observer.get_money()
        if(money_cuenta >= self.amount):
            money_cuenta -= self.amount
            #Actualizo el dinero del cliente
            cuenta.observer.set_money(money_cuenta)

            write_on_file(f"{cuenta.observer.name}, se realizo con éxito el pago del mes {cuenta.get_month()} en {self.name}", "log.txt")
            return True
        else:
            write_on_file(f"{cuenta.observer.name},no se pudo realizar el pago en {self.name}", "log.txt")
            return False
    
    """
    Método para cambiar plan (metodo de pago). Esta pensado para cambiar de free a premium.

    """
    def change_plan(self, cuenta):
        result = False

        if(self.month_change == cuenta.get_month()):
            write_on_file(f"------AVISO :{cuenta.observer.name}, ya pasaste {self.month_change} meses en {self.name}, te vamos a cambiar de plan.", "log.txt")
            result = True

        return result




class Inter_Spotify(Strategy):
    pass
   
class StrategySpotifyPremium(Inter_Spotify, Strategy_Metodos):
    def __init__(self):
        super().__init__("Spotify Premium", 80, .5)
    
class StrategySpotifyFree(Inter_Spotify,Strategy_Metodos):
    def __init__(self):
        super().__init__("Spotify Free",0, 3)






class Inter_Disney(Strategy):
    pass

class StrategyDisneyStart(Inter_Disney ,Strategy_Metodos):
    def __init__(self):
        super().__init__("Disney Start",130, 3)

class StrategyDisney(Inter_Disney ,Strategy_Metodos):
    def __init__(self):
        super().__init__("Disney", 160 ,.5)
 




class Inter_Netflix(Strategy):
    pass 

class StrategyNetflix_uno(Inter_Netflix, Strategy_Metodos):
    def __init__(self):
        super().__init__("Netflix para un dispositivo",120, .5)

class StrategyNetflix_dos(Inter_Netflix, Strategy_Metodos):
    def __init__(self):
        super().__init__("Netflix para 2 dispositivos",170, .5)

class StrategyNetflix_cuatro(Inter_Netflix, Strategy_Metodos):
    def __init__(self):
        super().__init__("Netflix para 4 dispositivos", 200, .5)




class Inter_HBO(Strategy):
    pass 

class StrategyHBOFree(Inter_HBO ,Strategy_Metodos):
    def __init__(self):
        super().__init__("HBO Free",0, 3)

class StrategyHBO(Inter_HBO ,Strategy_Metodos):
    def __init__(self):
        super().__init__("HBO Free", 140, .5)




class Inter_Amazon(Strategy):
    pass 

class StrategyAmazon(Inter_Amazon ,Strategy_Metodos):
    def __init__(self):
        super().__init__("Amazon", 110, .5)

class StrategyAmazonPremium(Inter_Amazon ,Strategy_Metodos):
    def __init__(self):
        super().__init__("Amazon Premium", 150, .5)


###############
###############
###############
        
class cuentaObserver:
    def __init__(self, observer, tipo_plan):
        self.observer = observer
        self.month = 0
        self.tipo_plan = tipo_plan

    def get_user(self):
        return self.observer
    
    def get_month(self):
        return self.month
    
    def set_month(self, number):
        self.month = number

    def get_tipo_plan(self):
        return self.tipo_plan
    
    def set_tipo_plan(self, num):
        self.tipo_plan = num

    def increase_month(self):
        self.month += 1

    def __eq__(self, cuenta2):
        if(self.observer == cuenta2.observer):
            return True
        else:
            return False 


    
    
    def imprimir_cuenta(self):
        write_on_file(f"Observer: {self.observer}", "log.txt")
        write_on_file(f"Month: {self.month}", "log.txt")
        write_on_file(f"Tipo Plan: {self.tipo_plan}", "log.txt")
###############
###############
###############


class Subject:
    def __init__(self):
        self.observers = []
        self.exObserver = []

    def get_observers(self):
        return self.observers


    ###Agrego una cuenta a mi lista de clientes
    def attach(self, observer):
        pass
 
    def detach(self, cuenta_observer):
        pass

    def notify(self):
        for observer in self.observers:
            observer.update(self)




class Platform(Subject):
    def __init__(self,name,strategyy):
        super().__init__()
        self.name = name
        self.recomendaciones = []
        #self.metodos_de_pago = []
        self.strategy = strategyy #Aqui lo de la interzas de cada plataforma
        self.banco = Banco(strategyy)
        #self.metodos_de_pago.append(strategyy) 

    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def attachStrategy_metodos(self, strategy):
        self.metodos_de_pago.append(strategy)
    
    def add_recommen(self, cadena):
        self.recomendaciones.append(cadena)


    def execute(self):
        # Aquí llamamos al método execute de la estrategia
        listaclientes = self.observers  
        for cliente in listaclientes:


            #Aqui banco
            banderaPago = self.banco.cobrar(cliente)
            


          


            # Bandera guarda un booleano, me dice si se pudo realizar el pago o no
            banderaPago = self.strategy.execute(cliente)


            #Si NO se realizo el pago, quito la suscripcion de mi cliente 
            if( banderaPago == False):
                self.detach(cliente)
            else:

                write_on_file(f"Hola! {cliente.observer.name}, Te recomendamos {rd.choice(self.recomendaciones[0])} de nuestra plataforma.", "log.txt")
           # Bandera que guarda un booleano, me dice si ya cambia el metodo de pago 
            # Solo aplica de la prueba free a premium
            banderaPrueba = self.strategy.change_plan(cliente)
            if(banderaPrueba ==True):

                # Esta linea determina el nuevo plan de pago del cliente 
                # Dado que las plataformas que tienen free (o primeros meses mas barato)
                # y premium solo
                # tienen esos 2 metodos de pago. Entonces si tiene el 
                # tipo de free (n) se le asigna el (n +1). 
                plan_nuevo = ((cliente.get_tipo_plan()) + 1)
                #Aqui ya asigno el nuevo metodo de pago el cliente
                cliente.set_tipo_plan(plan_nuevo)

    ###Agrego una cuenta a mi lista de clientes
    def attach(self, observer, plan):
        
        #Ceo una instancia de cuenta con un objeto observer y el tipo de plan
        cuenta = cuentaObserver(observer,plan)
        

        if cuenta in self.exObserver:
            self.exObserver.remove(cuenta)
            #Lo agrego a observer (la lista de clientes)
            self.observers.append(cuenta)
            write_on_file(f"Bienvenido de vuelta a {self.name}, {cuenta.observer.name}", "log.txt")
        else:
            #Los agrego a observer (la lista de clientes)
            self.observers.append(cuenta)
            write_on_file(f"{self.observers[-1].observer.name}, bienvenido a {self.name}", "log.txt")        
    
    
    def detach(self, cuenta_observer):
        for account in self.observers:
            if account.observer == cuenta_observer:
                self.observers.remove(account)
                self.exObserver.append(account)
                write_on_file(f"{self.name} mensaje : Lamentamos que nos dejes {cuenta_observer.name}", 'log.txt')
                # Actualizo los meses de la cuenta a cero
                account.set_month(0)  



class Banco():

    def __init__(self, strategyPlataforma):
        self.strategy = strategyPlataforma #Tiene un objeto tipo Inter_Spotify o Inter_Amazon

    def cobrar(self, cuenta):
        plan = cuenta.get_tipo_plan()
        def case1():
            self.strategy = StrategyNetflix_uno()
        def case2():
            self.strategy = StrategyNetflix_dos()
        def case3():
            self.strategy = StrategyNetflix_cuatro()
        def case4():
            self.strategy = StrategyAmazon()
        def case5():
            self.strategy = StrategyAmazonPremium()
        def case6():
            self.strategy = StrategySpotifyFree()
        def case7():
            self.strategy = StrategySpotifyPremium()
        def case8():
            self.strategy = StrategyDisneyStart()
        def case9():
            self.strategy = StrategyDisney()
        def case10():
            self.strategy = StrategyHBOFree()
        def case11():
            self.strategy = StrategyHBO()
        def default():
            print("Metodo de plan no encontrado")
        def switch_case(plan):
                switch_dict = {
                    1: case1,
                    2: case2,
                    3: case3,
                    4: case4,
                    5: case5,
                    6: case6,
                    7: case7,
                    8: case8,
                    9: case9,
                    10: case10,
                    11: case11,
                }
        bandera = self.strategy.execute(cuenta)
        return bandera

          

