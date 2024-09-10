package Figuras;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class VentanaPiramide extends JFrame implements ActionListener {
    private static final String TITULO = "Pirámide";
    private static final String ERROR_MENSAJE = "Campo nulo o error en formato de número";
    private static final String ERROR_TITULO = "Error";

    private final JTextField campoBase;
    private final JTextField campoAltura;
    private final JTextField campoApotema;
    private final JLabel volumenLabel;
    private final JLabel superficieLabel;

    public VentanaPiramide() {
        setTitle(TITULO);
        setSize(280, 240);
        setLocationRelativeTo(null);
        setResizable(false);

        Container contenedor = getContentPane();
        contenedor.setLayout(null);

        campoBase = crearCampoTexto(120, 20);
        campoAltura = crearCampoTexto(120, 50);
        campoApotema = crearCampoTexto(120, 80);
        volumenLabel = crearEtiqueta("Volumen (cm3):", 20, 140);
        superficieLabel = crearEtiqueta("Superficie (cm2):", 20, 170);

        JButton calcularButton = new JButton("Calcular");
        calcularButton.setBounds(120, 110, 135, 23);
        calcularButton.addActionListener(this);

        contenedor.add(crearEtiqueta("Base (cms):", 20, 20));
        contenedor.add(campoBase);
        contenedor.add(crearEtiqueta("Altura (cms):", 20, 50));
        contenedor.add(campoAltura);
        contenedor.add(crearEtiqueta("Apotema (cms):", 20, 80));
        contenedor.add(campoApotema);
        contenedor.add(calcularButton);
        contenedor.add(volumenLabel);
        contenedor.add(superficieLabel);
    }

    private JLabel crearEtiqueta(String texto, int x, int y) {
        JLabel etiqueta = new JLabel(texto);
        etiqueta.setBounds(x, y, 135, 23);
        return etiqueta;
    }

    private JTextField crearCampoTexto(int x, int y) {
        JTextField campo = new JTextField();
        campo.setBounds(x, y, 135, 23);
        return campo;
    }

    @Override
    public void actionPerformed(ActionEvent event) {
        try {
            double base = Double.parseDouble(campoBase.getText());
            double altura = Double.parseDouble(campoAltura.getText());
            double apotema = Double.parseDouble(campoApotema.getText());
            Piramide piramide = new Piramide(base, altura, apotema);
            actualizarResultados(piramide);
        } catch (NumberFormatException e) {
            mostrarError();
        }
    }

    private void actualizarResultados(Piramide piramide) {
        volumenLabel.setText("Volumen (cm3): " + String.format("%.2f", piramide.getVolumen()));
        superficieLabel.setText("Superficie (cm2): " + String.format("%.2f", piramide.getSuperficie()));
    }

    private void mostrarError() {
        JOptionPane.showMessageDialog(null, ERROR_MENSAJE, ERROR_TITULO, JOptionPane.ERROR_MESSAGE);
    }
}
