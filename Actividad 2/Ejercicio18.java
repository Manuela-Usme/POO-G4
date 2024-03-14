import java.util.Scanner;

class Empleado {
    private int codigoEmpleado;
    private String nombres;
    private int horasTrabajadas;
    private double valorHora;
    private double retencion;

    public Empleado(int codigoEmpleado, String nombres, int horasTrabajadas, double valorHora, double retencion) {
        this.codigoEmpleado = codigoEmpleado;
        this.nombres = nombres;
        this.horasTrabajadas = horasTrabajadas;
        this.valorHora = valorHora;
        this.retencion = retencion;
    }

    public int getCodigoEmpleado() {
        return codigoEmpleado;
    }

    public String getNombres() {
        return nombres;
    }

    public double calcularSalarioBruto() {
        return horasTrabajadas * valorHora;
    }

    public double calcularSalarioNeto() {
        double salarioBruto = calcularSalarioBruto();
        return salarioBruto - (salarioBruto * retencion / 100);
    }

    public void mostrarInformacion() {
        System.out.println("Código del empleado: " + codigoEmpleado);
        System.out.println("Nombres: " + nombres);
        System.out.println("Salario Bruto: $" + calcularSalarioBruto());
        System.out.println("Salario Neto: $" + calcularSalarioNeto());
    }
}

public class Ejercicio18 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el código del empleado:");
        int codigo = scanner.nextInt();
        scanner.nextLine(); // Consume newline
        System.out.println("Ingrese los nombres del empleado:");
        String nombres = scanner.nextLine();
        System.out.println("Ingrese el número de horas trabajadas al mes:");
        int horas = scanner.nextInt();
        System.out.println("Ingrese el valor por hora trabajada:");
        double valorHora = scanner.nextDouble();
        System.out.println("Ingrese el porcentaje de retención en la fuente:");
        double retencion = scanner.nextDouble();

        Empleado empleado = new Empleado(codigo, nombres, horas, valorHora, retencion);
        empleado.mostrarInformacion();

        scanner.close();
    }
}
