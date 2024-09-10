package Figuras;

public class Cilindro extends FiguraGeometrica {
    private final double radio;
    private final double altura;

    public Cilindro(double radio, double altura) {
        this.radio = radio;
        this.altura = altura;
        this.setVolumen(calcularVolumen());
        this.setSuperficie(calcularSuperficie());
    }

    @Override
    public double calcularVolumen() {
        return Math.PI * altura * Math.pow(radio, 2.0);
    }

    @Override
    public double calcularSuperficie() {
        double areaLateral = 2.0 * Math.PI * radio * altura;
        double areaBase = 2.0 * Math.PI * Math.pow(radio, 2.0);
        return areaLateral + areaBase;
    }
}
