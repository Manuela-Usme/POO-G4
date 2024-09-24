import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.lang.NumberFormatException;

class DisplayFriends {

    public static void main(String data[]) {
        try {
            String nameNumberString;
            String name;
            long number;

            // Usar el archivo "friendsContact.txt"
            File file = new File("friendsContact.txt");

            if (!file.exists()) {
                // Crear el archivo si no existe
                file.createNewFile();
            }

            // Abrir el archivo en modo lectura y escritura
            RandomAccessFile raf = new RandomAccessFile(file, "rw");

            // Recorrer el archivo mientras haya contenido
            while (raf.getFilePointer() < raf.length()) {
                // Leer línea del archivo
                nameNumberString = raf.readLine();

                // Separar el nombre y el número de la línea
                String[] lineSplit = nameNumberString.split("!");

                // Verificar si la línea está correctamente formateada
                if (lineSplit.length == 2) {
                    // Separar nombre y número
                    name = lineSplit[0];
                    number = Long.parseLong(lineSplit[1]);

                    // Imprimir los datos del contacto
                    System.out.println(
                        "Friend Name: " + name + "\n"
                        + "Contact Number: " + number + "\n"
                    );
                } else {
                    System.out.println("Formato de línea incorrecto: " + nameNumberString);
                }
            }

            // Cerrar el archivo
            raf.close();

        } catch (IOException ioe) {
            System.out.println("Error de entrada/salida: " + ioe);
        } catch (NumberFormatException nef) {
            System.out.println("Error en el formato del número: " + nef);
        }
    }
}
