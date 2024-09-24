import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;
import java.lang.NumberFormatException;

class UpdateFriend {

    public static void main(String data[]) {
        try {
            // Obtener el nombre del contacto a actualizar
            String newName = data[0];

            // Obtener el nuevo número de contacto
            long newNumber = Long.parseLong(data[1]);

            String nameNumberString;
            String name;
            long number;
            int index;

            // Usar el archivo "friendsContact.txt"
            File file = new File("friendsContact.txt");

            if (!file.exists()) {
                // Crear el archivo si no existe
                file.createNewFile();
            }

            // Abrir el archivo en modo lectura y escritura
            RandomAccessFile raf = new RandomAccessFile(file, "rw");
            boolean found = false;

            // Buscar el contacto en el archivo
            while (raf.getFilePointer() < raf.length()) {
                // Leer línea del archivo
                nameNumberString = raf.readLine();

                // Dividir la línea para obtener nombre y número
                String[] lineSplit = nameNumberString.split("!");

                // Separar nombre y número
                name = lineSplit[0];
                number = Long.parseLong(lineSplit[1]);

                // Si se encuentra el contacto, marcar como encontrado
                if (name.equals(newName)) {
                    found = true;
                    break;
                }
            }

            // Si el contacto fue encontrado, actualizarlo
            if (found) {
                // Crear un archivo temporal
                File tmpFile = new File("temp.txt");

                // Abrir el archivo temporal en modo lectura y escritura
                RandomAccessFile tmpraf = new RandomAccessFile(tmpFile, "rw");

                // Colocar el puntero del archivo original al inicio
                raf.seek(0);

                // Recorrer el archivo original
                while (raf.getFilePointer() < raf.length()) {
                    // Leer el contacto del archivo original
                    nameNumberString = raf.readLine();

                    // Obtener el nombre del contacto
                    index = nameNumberString.indexOf('!');
                    name = nameNumberString.substring(0, index);

                    // Si es el contacto que queremos actualizar, cambiar el número
                    if (name.equals(newName)) {
                        nameNumberString = name + "!" + String.valueOf(newNumber);
                    }

                    // Escribir en el archivo temporal
                    tmpraf.writeBytes(nameNumberString);
                    tmpraf.writeBytes(System.lineSeparator());
                }

                // Copiar el contenido del archivo temporal al archivo original
                raf.seek(0);
                tmpraf.seek(0);

                while (tmpraf.getFilePointer() < tmpraf.length()) {
                    raf.writeBytes(tmpraf.readLine());
                    raf.writeBytes(System.lineSeparator());
                }

                // Ajustar el tamaño del archivo original al del archivo temporal
                raf.setLength(tmpraf.length());

                // Cerrar ambos archivos
                tmpraf.close();
                raf.close();

                // Eliminar el archivo temporal
                tmpFile.delete();

                System.out.println("Contacto actualizado.");
            } else {
                // Si no se encontró el contacto, cerrar el archivo
                raf.close();
                System.out.println("El nombre ingresado no existe.");
            }

        } catch (IOException ioe) {
            System.out.println("Error de entrada/salida: " + ioe);
        } catch (NumberFormatException nef) {
            System.out.println("Error en el formato del número: " + nef);
        }
    }
}
