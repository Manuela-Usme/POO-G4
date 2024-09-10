package Figuras;

public class Piramide extends FiguraGeometrica {
    private final double base;
    private final double altura;
    private final double apotema;

    public Piramide(double base, double altura, double apotema) {
        this.base = base;
        this.altura = altura;
        this.apotema = apotema;
        this.setVolumen(calcularVolumen());
        this.setSuperficie(calcularSuperficie());
    }

    @Override
    public double calcularVolumen() {
        return (Math.pow(base, 2.0) * altura) / 3.0;
    }

    @Override
    public double calcularSuperficie() {
        double areaBase = Math.pow(base, 2.0);
        double areaLateral = 2.0 * base * apotema;
        return areaBase + areaLateral;
    }
}
