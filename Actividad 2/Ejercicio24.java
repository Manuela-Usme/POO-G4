import java.util.Scanner;

class Esfera {
    private String nombre;
    private double peso;

    // Constructor
    public Esfera(String nombre, double peso) {
        this.nombre = nombre;
        this.peso = peso;
    }

    // Método para obtener el peso
    public double getPeso() {
        return peso;
    }

    // Método para obtener el nombre
    public String getNombre() {
        return nombre;
    }
}

public class Ejercicio24 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Crear los objetos esfera
        Esfera esferaA = crearEsfera(scanner, "A");
        Esfera esferaB = crearEsfera(scanner, "B");
        Esfera esferaC = crearEsfera(scanner, "C");

        // Encontrar la esfera de mayor peso
        Esfera mayorPeso = encontrarMayorPeso(esferaA, esferaB, esferaC);

        // Mostrar resultado
        System.out.println("La esfera de mayor peso es: " + mayorPeso.getNombre() + " con un peso de " + mayorPeso.getPeso());

        scanner.close();
    }

    // Método para crear una esfera ingresando el nombre (predefinido como A,B y C) y el peso
    public static Esfera crearEsfera(Scanner scanner, String nombre) {
        System.out.print("Ingrese el peso de la esfera " + nombre + ": ");
        double peso = scanner.nextDouble();
        return new Esfera(nombre, peso);
    }

    // Método para encontrar la esfera de mayor peso, mediante comparación de los pesos 
    public static Esfera encontrarMayorPeso(Esfera esfera1, Esfera esfera2, Esfera esfera3) {
        if (esfera1.getPeso() > esfera2.getPeso() && esfera1.getPeso() > esfera3.getPeso()) {
            return esfera1;
        } else if (esfera2.getPeso() > esfera1.getPeso() && esfera2.getPeso() > esfera3.getPeso()) {
            return esfera2;
        } else {
            return esfera3;
        }
    }
}