package Figuras;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class VentanaPrincipal extends JFrame implements ActionListener {
    private static final String TITULO = "Figuras Geométricas";
    private static final int ANCHO_VENTANA = 350;
    private static final int ALTO_VENTANA = 160;

    private final JButton cilindroButton;
    private final JButton esferaButton;
    private final JButton piramideButton;

    public VentanaPrincipal() {
        setTitle(TITULO);
        setSize(ANCHO_VENTANA, ALTO_VENTANA);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);

        Container contenedor = getContentPane();
        contenedor.setLayout(null);

        cilindroButton = crearBoton("Cilindro", 20, 50);
        esferaButton = crearBoton("Esfera", 125, 50);
        piramideButton = crearBoton("Pirámide", 225, 50);

        contenedor.add(cilindroButton);
        contenedor.add(esferaButton);
        contenedor.add(piramideButton);
    }

    private JButton crearBoton(String texto, int x, int y) {
        JButton boton = new JButton(texto);
        boton.setBounds(x, y, 100, 23);
        boton.addActionListener(this);
        return boton;
    }

    @Override
    public void actionPerformed(ActionEvent evento) {
        if (evento.getSource() == cilindroButton) {
            abrirVentana(new VentanaCilindro());
        } else if (evento.getSource() == esferaButton) {
            abrirVentana(new VentanaEsfera());
        } else if (evento.getSource() == piramideButton) {
            abrirVentana(new VentanaPiramide());
        }
    }

    private void abrirVentana(JFrame ventana) {
        ventana.setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            VentanaPrincipal ventanaPrincipal = new VentanaPrincipal();
            ventanaPrincipal.setVisible(true);
        });
    }
}
