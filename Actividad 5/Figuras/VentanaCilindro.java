package Figuras;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class VentanaCilindro extends JFrame implements ActionListener {
    private static final String TITULO = "Cilindro";
    private static final String ERROR_MENSAJE = "Campo nulo o error en formato de número";
    private static final String ERROR_TITULO = "Error";

    private final JTextField campoRadio;
    private final JTextField campoAltura;
    private final JLabel volumenLabel;
    private final JLabel superficieLabel;

    public VentanaCilindro() {
        setTitle(TITULO);
        setSize(280, 210);
        setLocationRelativeTo(null);
        setResizable(false);

        Container contenedor = getContentPane();
        contenedor.setLayout(null);

        campoRadio = crearCampoTexto(100, 20);
        campoAltura = crearCampoTexto(100, 50);
        volumenLabel = crearEtiqueta("Volumen (cm3):", 20, 110);
        superficieLabel = crearEtiqueta("Superficie (cm2):", 20, 140);

        JButton calcularButton = new JButton("Calcular");
        calcularButton.setBounds(100, 80, 135, 23);
        calcularButton.addActionListener(this);

        contenedor.add(crearEtiqueta("Radio (cms):", 20, 20));
        contenedor.add(campoRadio);
        contenedor.add(crearEtiqueta("Altura (cms):", 20, 50));
        contenedor.add(campoAltura);
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
            double radio = Double.parseDouble(campoRadio.getText());
            double altura = Double.parseDouble(campoAltura.getText());
            Cilindro cilindro = new Cilindro(radio, altura);
            actualizarResultados(cilindro);
        } catch (NumberFormatException e) {
            mostrarError();
        }
    }

    private void actualizarResultados(Cilindro cilindro) {
        volumenLabel.setText("Volumen (cm3): " + String.format("%.2f", cilindro.getVolumen()));
        superficieLabel.setText("Superficie (cm2): " + String.format("%.2f", cilindro.getSuperficie()));
    }

    private void mostrarError() {
        JOptionPane.showMessageDialog(null, ERROR_MENSAJE, ERROR_TITULO, JOptionPane.ERROR_MESSAGE);
    }
}
