package Figuras;

public abstract class FiguraGeometrica {
    private double volumen;
    private double superficie;

    public void setVolumen(double volumen) {
        this.volumen = volumen;
    }

    public void setSuperficie(double superficie) {
        this.superficie = superficie;
    }

    public double getVolumen() {
        return this.volumen;
    }

    public double getSuperficie() {
        return this.superficie;
    }

    public abstract double calcularVolumen();
    public abstract double calcularSuperficie();
}
