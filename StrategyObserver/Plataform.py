class Strategy:
    def execute(self):
        pass



###################
    ##### AQUI CASO DE SPOTY DONDE COBRE 80
    # Recibe como parametro una cuenta de cliente
class StrategySpotify(Strategy):
    def execute(self, cliente):
        money_cliente = cliente.observer.get_money()
        if(money_cliente >= 80):
            money_cliente -= 80
            cliente.observer.set_money(money_cliente)
            print(f"Se realizo el pago en Spotify normal {cliente.observer.name}")
            aumento_Mes = cliente.get_month() +1
            cliente.set_month(aumento_Mes)
        else:
            print(f"No se pudo realizar el pago {cliente.observer.name}")
            


class StrategySpotifyFree(Strategy):
    def execute(self, cliente):
        print(f"Se realizo tu pago de $0 {cliente.observer.name}. Recuerda que auhn tienes Spotify free")
        aumento_Mes = cliente.get_month() +1
        cliente.set_month(aumento_Mes)





class StrategyDisney(Strategy):
    def execute(self, num):
        if num == "trial":
            return 130
        if num == "base":
            return 160

class StrategyNetflix(Strategy):
    def execute(self, num):
        if num == "oneDevice":
            return 120
        elif num == "twoDevice":
            return 170
        elif num == "fourDevice":
            return 200

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
    
    def set_month(self, nuevo):
        self.tipo_plan = nuevo
    
    
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

    """
    def attach(self, observer):
        self.observers.append(observer)

        if observer in self.exObserver:
            print(f"Bienvenido de vuelta {observer.name}")
        else:
            print(f"Hello {self.observers[-1].name}")
    """

    ###Agrego una cuenta a mi lista de clientes
    def attach(self, observer, plan):
        cuenta = cuentaObserver(observer,plan)
        self.observers.append(cuenta)

        if cuenta in self.exObserver:
            print(f"Bienvenido de vuelta {cuenta.observer.name}")
        else:
            print(f"Hello {self.observers[-1].observer.name}")        
        

    def detach(self, observer):
        self.observers.remove(observer)
        self.exObserver.append(observer)
        print(f"Lamentamos que nos dejes {observer.name}")

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
            self.strategy.execute(cliente)


    #def level(self, num):
        #return self.strategy.execute(num)

