import java.io.File;
import java.io.IOException;
import java.io.RandomAccessFile;

class DeleteFriend {

    public static void main(String data[]) {

        try {
            // Obtener el nombre del contacto a eliminar desde los argumentos de línea de comando
            String nameToDelete = data[0];

            String nameNumberString;
            String name;
            long number;
            int index;

            // Crear el archivo friendsContact.txt si no existe
            File file = new File("friendsContact.txt");

            if (!file.exists()) {
                file.createNewFile();
            }

            // Abrir el archivo en modo lectura y escritura
            RandomAccessFile raf = new RandomAccessFile(file, "rw");
            boolean found = false;

            // Comprobar si el contacto existe en el archivo
            while (raf.getFilePointer() < raf.length()) {
                // Leer línea del archivo
                nameNumberString = raf.readLine();

                // Dividir la línea para obtener el nombre y el número
                String[] lineSplit = nameNumberString.split("!");

                // Separar el nombre y el número
                name = lineSplit[0];
                number = Long.parseLong(lineSplit[1]);

                // Si el contacto a eliminar es encontrado
                if (name.equals(nameToDelete)) {
                    found = true;
                    break;
                }
            }

            // Eliminar el contacto si se encuentra
            if (found) {
                // Crear un archivo temporal
                File tmpFile = new File("temp.txt");

                // Abrir el archivo temporal en modo lectura y escritura
                RandomAccessFile tmpraf = new RandomAccessFile(tmpFile, "rw");

                // Regresar el puntero del archivo original al inicio
                raf.seek(0);

                // Recorrer el archivo original y copiar todo excepto el contacto a eliminar
                while (raf.getFilePointer() < raf.length()) {
                    // Leer la línea del archivo original
                    nameNumberString = raf.readLine();

                    index = nameNumberString.indexOf('!');
                    name = nameNumberString.substring(0, index);

                    // Si es el contacto que queremos eliminar, lo omitimos
                    if (name.equals(nameToDelete)) {
                        continue;
                    }

                    // Escribir la línea en el archivo temporal
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

                System.out.println("Contacto eliminado.");
            } else {
                // Si no se encontró el contacto, cerrar el archivo
                raf.close();
                System.out.println("El nombre ingresado no existe.");
            }

        } catch (IOException ioe) {
            System.out.println("Error de entrada/salida: " + ioe);
        } catch (NumberFormatException nfe) {
            System.out.println("Error en el formato del número: " + nfe);
        }
    }
}
