import java.util.Scanner;

class TrianguloEquilatero {
    private double lado;

    public TrianguloEquilatero(double lado) {
        this.lado = lado;
    }

    public double calcularPerimetro() {
        return 3 * lado;
    }

    public double calcularAltura() {
        return Math.sqrt(3) / 2 * lado;
    }

    public double calcularArea() {
        return (Math.sqrt(3) / 4) * lado * lado;
    }
}

public class Ejercicio19 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el valor del lado del triángulo equilátero:");
        double lado = scanner.nextDouble();

        TrianguloEquilatero triangulo = new TrianguloEquilatero(lado);

        double perimetro = triangulo.calcularPerimetro();
        double altura = triangulo.calcularAltura();
        double area = triangulo.calcularArea();

        System.out.println("El perímetro del triángulo equilátero es: " + perimetro);
        System.out.println("La altura del triángulo equilátero es: " + altura);
        System.out.println("El área del triángulo equilátero es: " + area);

        scanner.close();
    }
}
