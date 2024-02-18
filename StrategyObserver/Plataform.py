
class Strategy:
    def __init__(self,name, amount, month_change):
        self.name = name
        self.amount = amount
        self.month_change = month_change
  
    #Este metodo devuelve un booleano, verifica y realiza el pago del servicio 
    def execute(self,cuenta):

        #Checo si el cliente tiene dinero suficiente
        money_cuenta = cuenta.observer.get_money()
        if(money_cuenta >= self.amount):
            money_cuenta -= self.amount
            #Actualizo el dinero del cliente
            cuenta.observer.set_money(money_cuenta)

            print(f"{cuenta.observer.name}, se realizo con éxito el pago en {self.name}")
            cuenta.increase_month()
            return True
        else:
            print(f"{cuenta.observer.name},no se pudo realizar el pago en {self.name} ")
            return False
    
    def change_plan(self, cuenta):
        if(self.month_change == cuenta.get_month()):
            print(f"{cuenta.observer.name},ya pasaste {self.month_change} meses en {self.name}, te vamos a cambiar de plan ")




class StrategySpotifyPremium(Strategy):
    def __init__(self):
        super().__init__("Spotify Premium", 80, .5)
    

class StrategySpotifyFree(Strategy):
    def __init__(self):
        super().__init__("Spotify Free",0, .5)


class StrategyDisneyFree(Strategy):
    def __init__(self, name, amount, month_change ):
        super().__init__("Disney Start",130, 3)

class StrategyDisney(Strategy):
    def __init__(self, name, amount, month_change ):
        super().__init__("Disney", 160 ,.5)
 
"""
class StrategyNetflix_uno(Strategy):
    def __init__(self, name, amount, month_change ):
        super().__init__("Spotify Free", 4)

class StrategyHBO(Strategy):
    def execute(self, num):
        if num == "trial":
            return 0
        elif num == "base":
            return 140

class StrategyAmazon(Strategy):
    def execute(self, num):
        if num == "base":
            return 110
        elif num == "premium":
            return 150
"""

###############
###############
###############
        
class cuentaObserver:
    def __init__(self, observer, tipo_plan):
        self.observer = observer
        self.month = -1
        self.tipo_plan = tipo_plan

    def get_user(self):
        return self.observer
    
    def get_month(self):
        return self.month
    
    def set_month(self, number):
        self.month = number

    def get_tipo_plan(self):
        return self.tipo_plan

    def increase_month(self):
        self.month += 1
    
    
    def imprimir_cuenta(self):
        print(f"Observer: {self.observer}")
        print(f"Month: {self.month}")
        print(f"Tipo Plan: {self.tipo_plan}")
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
    def attach(self, observer, plan):
        cuenta = cuentaObserver(observer,plan)
        self.observers.append(cuenta)

        if cuenta in self.exObserver:
            print(f"Bienvenido de vuelta {cuenta.observer.name}")
        else:
            print(f"Hello {self.observers[-1].observer.name}")        
        

    def detach(self, cuenta_observer):
        self.observers.remove(cuenta_observer)
        self.exObserver.append(cuenta_observer)
        print(f"Lamentamos que nos dejes {cuenta_observer.observer.name}")
        # Actualizo los meses de la cuenta a cero
        cuenta_observer.set_month(0)

    def notify(self):
        for observer in self.observers:
            observer.update(self)




class Platform(Subject):
    def __init__(self,strategyy):
        super().__init__()
        self.name = ""
        self.recomendaciones = []
        self.metodos_de_pago = []
        self.strategy = strategyy
        self.metodos_de_pago.append(strategyy) 

    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def attachStrategy_metodos(self, strategy):
        self.metodos_de_pago.append(strategy)


    def execute(self):
        # Aquí llamamos al método execute de la estrategia
        listaclientes = self.observers  
        for cliente in listaclientes:
            plan_cliente = cliente.get_tipo_plan()
            self.set_strategy( self.metodos_de_pago[plan_cliente] )

            # Bandera guarda un booleano, me dice si se pudo realizar el pago o no
            bandera = self.strategy.execute(cliente)

            #Si NO se realizo el pago, quito la suscripcion de mi cliente 
            if( bandera== False):
                self.detach(cliente)



    #def level(self, num):
        #return self.strategy.execute(num)

