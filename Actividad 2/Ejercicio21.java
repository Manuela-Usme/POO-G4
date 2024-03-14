import java.util.Scanner;

class Triangulo {
    private double lado1;
    private double lado2;
    private double lado3;

    public Triangulo(double lado1, double lado2, double lado3) {
        this.lado1 = lado1;
        this.lado2 = lado2;
        this.lado3 = lado3;
    }

    public double calcularPerimetro() {
        return lado1 + lado2 + lado3;
    }

    public double calcularSemiperimetro() {
        return calcularPerimetro() / 2;
    }

    public double calcularArea() {
        double s = calcularSemiperimetro();
        return Math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3));
    }
}

public class Ejercicio21 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Ingrese el primer lado del triángulo:");
        double lado1 = scanner.nextDouble();
        System.out.println("Ingrese el segundo lado del triángulo:");
        double lado2 = scanner.nextDouble();
        System.out.println("Ingrese el tercer lado del triángulo:");
        double lado3 = scanner.nextDouble();

        Triangulo triangulo = new Triangulo(lado1, lado2, lado3);

        double perimetro = triangulo.calcularPerimetro();
        double semiperimetro = triangulo.calcularSemiperimetro();
        double area = triangulo.calcularArea();

        System.out.println("El perímetro del triángulo es: " + perimetro);
        System.out.println("El semiperímetro del triángulo es: " + semiperimetro);
        System.out.println("El área del triángulo es: " + area);

        scanner.close();
    }
}
