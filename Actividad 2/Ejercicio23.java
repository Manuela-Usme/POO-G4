import java.util.Scanner;

class EcuacionSegundoGrado {
    private double A, B, C;

    // Constructor
    public EcuacionSegundoGrado(double A, double B, double C) {
        this.A = A;
        this.B = B;
        this.C = C;
    }

    // Método para calcular las soluciones segun el discriminante
    public void calcularSoluciones() {
        double discriminante = (B * B) - (4 * A * C);

        // Tipos de solucion del sistema según el discriminante
        if (discriminante > 0) {
            // Si el discriminante es mayor a cero, el sistema tiene 2 soluciones reales
            double x1 = (-B + Math.sqrt(discriminante)) / (2 * A);
            double x2 = (-B - Math.sqrt(discriminante)) / (2 * A);
            System.out.println("Las soluciones son reales:");
            System.out.println("x1 = " + x1);
            System.out.println("x2 = " + x2);
        } else if (discriminante == 0) {
            // Si el discriminante es igual a cero, el sistema tiene un única solución real
            double x = -B / (2 * A);
            System.out.println("La solución es real única:");
            System.out.println("x = " + x);
        } else {
            // Si el discriminante es menor a cero, el sistema tiene un par de soluciones complejas conjugadas
            double parteReal = -B / (2 * A);
            double parteImaginaria = Math.sqrt(Math.abs(discriminante)) / (2 * A);
            System.out.println("Las soluciones son complejas:");
            System.out.println("x1 = " + parteReal + " + " + parteImaginaria + "i");
            System.out.println("x2 = " + parteReal + " - " + parteImaginaria + "i");
        }
    }
}

public class Ejercicio23 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitar los coeficientes de la ecuación al usuario
        System.out.println("Ingrese los coeficientes de la ecuación de segundo grado (Ax^2 + Bx + C):");
        System.out.print("A: ");
        double A = scanner.nextDouble();
        System.out.print("B: ");
        double B = scanner.nextDouble();
        System.out.print("C: ");
        double C = scanner.nextDouble();

        System.out.println("\nEl problema es resuelto haciendo uso de la ecuación general mediante el uso del discriminante\n");

        // Crear el objeto de la ecuación de segundo grado
        EcuacionSegundoGrado ecuacion = new EcuacionSegundoGrado(A, B, C);

        // Calcular soluciones
        ecuacion.calcularSoluciones();

        scanner.close();
    }
}
