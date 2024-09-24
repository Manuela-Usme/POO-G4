import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MainGUI extends JFrame {

    public MainGUI() {
        // Configuración de la ventana principal
        setTitle("Contact Manager");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new GridLayout(5, 1));

        // Crear los botones para cada opción
        JButton createButton = new JButton("Create Contact");
        JButton readButton = new JButton("Read Contacts");
        JButton updateButton = new JButton("Update Contact");
        JButton deleteButton = new JButton("Delete Contact");
        JButton exitButton = new JButton("Exit");

        // Añadir los botones a la ventana
        add(createButton);
        add(readButton);
        add(updateButton);
        add(deleteButton);
        add(exitButton);

        // Acción del botón "Create Contact"
        createButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = JOptionPane.showInputDialog("Enter the name of the new contact:");
                String number = JOptionPane.showInputDialog("Enter the contact number:");

                if (name != null && number != null) {
                    AddFriend.main(new String[]{name, number});
                    JOptionPane.showMessageDialog(null, "Contact created successfully!");
                }
            }
        });

        // Acción del botón "Read Contacts"
        readButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                DisplayFriends.main(new String[]{});
                JOptionPane.showMessageDialog(null, "Contacts displayed in console.");
            }
        });

        // Acción del botón "Update Contact"
        updateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = JOptionPane.showInputDialog("Enter the name of the contact to update:");
                String newNumber = JOptionPane.showInputDialog("Enter the new contact number:");

                if (name != null && newNumber != null) {
                    UpdateFriend.main(new String[]{name, newNumber});
                    JOptionPane.showMessageDialog(null, "Contact updated successfully!");
                }
            }
        });

        // Acción del botón "Delete Contact"
        deleteButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String name = JOptionPane.showInputDialog("Enter the name of the contact to delete:");

                if (name != null) {
                    DeleteFriend.main(new String[]{name});
                    JOptionPane.showMessageDialog(null, "Contact deleted successfully!");
                }
            }
        });

        // Acción del botón "Exit"
        exitButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                System.exit(0);  // Cierra el programa
            }
        });

        setVisible(true); // Mostrar la ventana
    }

    public static void main(String[] args) {
        // Crear y mostrar la interfaz gráfica
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new MainGUI();
            }
        });
    }
}
