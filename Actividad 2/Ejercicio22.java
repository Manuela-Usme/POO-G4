import java.util.Scanner;

class Empleado {

    // Clase que contiene los métodos que realizaran las operaciones requeridas sobre el salario
    private String nombre;
    private double salarioHora;
    private int horasTrabajadas;

    // Constructor
    public Empleado(String nombre, double salarioHora, int horasTrabajadas) {
        this.nombre = nombre;
        this.salarioHora = salarioHora;
        this.horasTrabajadas = horasTrabajadas;
    }

    // Método para calcular el salario mensual
    public double calcularSalarioMensual() {
        return salarioHora * horasTrabajadas;
    }

    // Método para imprimir el nombre y el salario si es mayor a 450000, de lo contrario imprimir solo el nombre
    public void imprimirSalario() {
        double salarioMensual = calcularSalarioMensual();
        if (salarioMensual > 450000) {
            System.out.println("Nombre: " + nombre + ", Salario: " + salarioMensual);
        } else {
            System.out.println("Nombre: " + nombre);
        }
    }
}

public class Ejercicio22 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Solicitar entradas al usuario
        // Nombre en string, Salario por hora en Double y Horas al mes en Integer
        System.out.print("Ingrese el nombre del empleado: ");
        String nombre = scanner.nextLine();

        System.out.print("Ingrese el salario básico por hora: ");
        double salarioHora = scanner.nextDouble();

        System.out.print("Ingrese el número de horas trabajadas al mes: ");
        int horasTrabajadas = scanner.nextInt();

        // Crear objeto empleado
        Empleado empleado = new Empleado(nombre, salarioHora, horasTrabajadas);

        // Imprimir el nombre y salario (si es mayor a 450000)
        empleado.imprimirSalario();

        scanner.close();
    }
}