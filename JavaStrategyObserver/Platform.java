import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;


class WriteFunc {
    public static void writeOnFile(String texto, String nombreArchivo) {
        // Asegura que el nombre del archivo tenga la extensión .txt
        if (!nombreArchivo.endsWith(".txt")) {
            nombreArchivo += ".txt";
        }
        
        // Abre el archivo en modo de añadir o crea uno nuevo si no existe, luego escribe el texto en una nueva línea
        try (BufferedWriter archivo = new BufferedWriter(new FileWriter(nombreArchivo, true))) {
            archivo.write(texto + "\n");
        } catch (IOException e) {
            System.out.println("Ocurrió un error al escribir en el archivo: " + e.getMessage());
        }

        
    }   
}


class Cuenta {
    public User observer;
    private int month;
    private int tipoPlan;

    public Cuenta(User observer, int tipoPlan) {
        this.observer = observer;
        this.month = 0;
        this.tipoPlan = tipoPlan;
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int number) {
        this.month = number;
    }

    public int getTipoPlan() {
        return tipoPlan;
    }

    public void setTipoPlan(int tipoPlan) {
        this.tipoPlan = tipoPlan;
    }

    public void increaseMonth() {
        this.month += 1;
    }

    /*
    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        CuentaObserver cuenta2 = (CuentaObserver) obj;
        return Objects.equals(observer, cuenta2.observer);
    }
    */

}

interface Observer {
    
}

class User {
    private String name;
    private double money;

    public User(String name, double money) {
        this.name = name;
        this.money = money;
    }

    public String getName() {
        return name;
    }
    
    public double getMoney() {
        return money;
    }

    public void setMoney(double money) {
        this.money = money;
    }
}

abstract class Subject {
    public List<Cuenta> observers = new ArrayList<>();
    public List<Cuenta> exObservers = new ArrayList<>();

    // Método para obtener la lista de observadores actuales
    public List<Cuenta> getObservers() {
        return observers;   
    }

    public List<Cuenta> getExObservers() {
        return exObservers;   
    }

    // Método para agregar un observador a la lista
    public void attach(User observer, int plan) {

    }

    // Método para remover un observador de la lista
    public void detach(User observer) {

    }
}

public class Platform extends Subject {
    private List<String> recomendaciones;
    private Banco banco; // Asumiendo que existe una clase Banco con un método cobrar

    public Platform(String name, StrategyMetodos strategy) {
        super();
        this.recomendaciones = new ArrayList<>();
        this.banco = new Banco(strategy);
    }

    public void addRecomendacion(String recomendacion) {
        recomendaciones.add(recomendacion);
    }

    public void execute() {

        for (Cuenta cliente : observers) {
            // Aquí la clase Banco cobra
            boolean banderaPago = banco.cobrar(cliente);

            if (!banderaPago) {
                detach(cliente.observer);
            } else {
                // Simula la elección aleatoria de una recomendación
                int numeroAle = (int) (Math.random() * recomendaciones.size()) + 1;
                WriteFunc.writeOnFile("\tHola! " + cliente.observer.getName() + ", Te recomendamos " + recomendaciones.get(numeroAle) + " de nuestra plataforma.", "log.txt");
            }

            // Aquí checamos si es necesario cambiar de plan, si lo es, lo cambiamos
            banco.cambiarPlanDePago(cliente, banderaPago);
        }
    }

    @Override
    public void attach(User observer, int plan) {
         // Assuming nombrePlan is a method that returns the name of the plan as String
         String nombrePlataforma = nombrePlan(plan);

         Cuenta cuenta = new Cuenta(observer, plan);
 
         if (exObservers.contains(cuenta)) {
             exObservers.remove(cuenta);
             observers.add(cuenta);
             WriteFunc.writeOnFile("Bienvenido de vuelta a " + nombrePlataforma + ", " + cuenta.observer.getName(), "log.txt");
         } else {
             observers.add(cuenta);
             WriteFunc.writeOnFile(observers.get(observers.size() - 1).observer.getName() + ", bienvenido a " + nombrePlataforma, "log.txt");
         }
    }

    @Override
    public void detach(User observer) {
        for (Cuenta cliente : observers) {
           if (cliente.observer.equals(observer)) {
            observers.remove(cliente);
            exObservers.add(cliente);

            WriteFunc.writeOnFile("Lamentamos que nos dejes " + cliente.observer.getName(), "log.txt");

            cliente.setMonth(0);
           }
        }
    }

    public String nombrePlan(int plan) {
        // Implementación del switch-case
        switch (plan) {
            case 1: return "Netflix con un dispositivo";
            case 2: return "Netflix con dos dispositivos";
            case 3: return "Netflix con 4 dispositivos";
            case 4: return "Amazon";
            case 5: return "Amazon Premium";
            case 6: return  "Spotify Free";
            case 7: return "Spotify Premium";
            case 8: return "Disney Start";
            case 9: return "Disney";
            case 10: return "HBO free";
            case 11: return"HBO";

            default: System.out.println("Método de plan no encontrado"); return "CANAL 5";
        }
    }
}




class StrategyMetodos {
    private String name;
    private int amount;
    private double monthChange;

    public StrategyMetodos(String name, int amount, double d) {
        this.name = name;
        this.amount = amount;
        this.monthChange = d;
    }

    // Este método devuelve un booleano, verifica y realiza el pago del servicio
    public boolean execute(Cuenta cuenta) {
        cuenta.increaseMonth();
        double moneyCuenta = cuenta.observer.getMoney();
        if (moneyCuenta >= this.amount) {
            moneyCuenta -= this.amount;
            cuenta.observer.setMoney(moneyCuenta);
            WriteFunc.writeOnFile(cuenta.observer.getName() + ", se realizó con éxito el pago de $" + this.amount + " del mes " + cuenta.getMonth() + " en " + this.name, "log.txt");
            return true;
        } else {
            WriteFunc.writeOnFile(cuenta.observer.getName() + ", no se pudo realizar el pago en " + this.name, "log.txt");
            return false;
        }
    }

    // Método para cambiar plan (método de pago). Está pensado para cambiar de free a premium.
    public boolean changePlan(Cuenta cuenta) {
        boolean result = false;
        if (this.monthChange == cuenta.getMonth()) {
            WriteFunc.writeOnFile("------AVISO :" + cuenta.observer.getName() + ", ya pasaste " + this.monthChange + " meses en " + this.name + ", te vamos a cambiar de plan.", "log.txt");
            result = true;
        }
        return result;
    }
    
}


interface InterSpotify {}

class StrategySpotifyPremium extends StrategyMetodos implements InterSpotify {
    public StrategySpotifyPremium() {
        super("Spotify Premium", 80, 0.5);
    }

    @Override
    public boolean execute(Cuenta cuenta) {
        return super.execute(cuenta);
    }

    @Override
    public boolean changePlan(Cuenta cuenta) {
        return super.changePlan(cuenta);
    }
}

class StrategySpotifyFree extends StrategyMetodos implements InterSpotify {
    public StrategySpotifyFree() {
        super("Spotify Free", 0, 3);
    }
}

interface InterDisney {}

class StrategyDisneyStart extends StrategyMetodos implements InterDisney {
    public StrategyDisneyStart() {
        super("Disney Start", 130, 3);
    }
}

class StrategyDisney extends StrategyMetodos implements InterDisney {
    public StrategyDisney() {
        super("Disney", 160, .5);
    }
}

interface InterNetflix {}

class StrategyNetflix_uno extends StrategyMetodos implements InterNetflix {
    public StrategyNetflix_uno() {
        super("Netflix para un dispositivo", 120, .5);
    }
}
class StrategyNetflix_dos extends StrategyMetodos implements InterNetflix {
    public StrategyNetflix_dos() {
        super("Netflix para dos dispositivo", 170, .5);
    }
}
class StrategyNetflix_cuatro extends StrategyMetodos implements InterNetflix {
    public StrategyNetflix_cuatro() {
        super("Netflix para cuatro dispositivo", 200, .5);
    }
}


interface InterHBO {}

class StrategyHBOFree extends StrategyMetodos implements InterHBO {
    public StrategyHBOFree () {
        super("HBO Free", 0, 3);
    }
}

class StrategyHBO extends StrategyMetodos implements InterHBO {
    public StrategyHBO () {
        super("HBO", 140, .5);
    }
}

interface InterAmazon {}

class StrategyAmazon extends StrategyMetodos implements InterAmazon {
    public StrategyAmazon () {
        super("Amazon", 110, 3);
    }
}

class StrategyAmazonPremium extends StrategyMetodos implements InterAmazon {
    public StrategyAmazonPremium () {
        super("Amazon Premium", 150, .5);
    }
}


// #########################################################################################//

class Banco {

    private StrategyMetodos strategy; // Holds an object of type Strategy (e.g., Inter_Spotify or Inter_Amazon)

    public Banco(StrategyMetodos strategyPlataforma) {
        this.strategy = strategyPlataforma;
    }

    // Method that returns TRUE if the payment was successfully made, otherwise FALSE
    public boolean cobrar(Cuenta cuenta) {
        definirMetodoDePago(cuenta);
        boolean bandera = strategy.execute(cuenta);
        return bandera;
    }

    // This function changes the customer's payment plan
    // Returns True if the customer has changed plans
    // Returns False if the customer has not changed plans
    public void cambiarPlanDePago(Cuenta cuenta, boolean banderaPago) {
        boolean banderaCambio = false;

        // If the customer has made the payment and is still subscribed, then check if I should change their plan
        if (banderaPago) {
            banderaCambio = strategy.changePlan(cuenta);
        }

        // If the customer changes plan, modify the tipo_plan in their account
        if (banderaCambio) {
            int planActual = cuenta.getTipoPlan();
            cuenta.setTipoPlan(planActual + 1);
        }
    }

    // This method defines a Strategy object depending on the account's plan
    private void definirMetodoDePago(Cuenta cuenta) {
        int plan = cuenta.getTipoPlan();
        switch (plan) {
            case 1:
                strategy = new StrategyNetflix_uno();
                break;
            case 2:
                strategy = new StrategyNetflix_dos();
                break;
            case 3:
                strategy = new StrategyNetflix_cuatro();
                break;
            case 4:
                strategy = new StrategyAmazon();
                break;
            case 5:
                strategy = new StrategyAmazonPremium();
                break;
            case 6:
                strategy = new StrategySpotifyFree();
                break;
            case 7:
                strategy = new StrategySpotifyPremium();
                break;
            case 8:
                strategy = new StrategyDisneyStart();
                break;
            case 9:
                strategy = new StrategyDisney();
                break;
            case 10:
                strategy = new StrategyHBOFree();
                break;
            case 11:
                strategy = new StrategyHBO();
                break;
            default:
                System.out.println("Error de Banco: Metodo de plan no encontrado <<" + cuenta.getTipoPlan() + ">> de " + cuenta.observer.getName());
                break;
        }
    }
}