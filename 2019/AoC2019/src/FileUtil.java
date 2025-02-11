import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Paths;
import java.nio.file.Path;

public class FileUtil {

    /**
     * Reads the content of a file located at the given relative path.
     *
     * @param relativeFilepath The relative path to the file from the project's root
     *                         or current working directory.
     * @return The content of the file as a String, or null if an error occurs
     *         (e.g., file not found).
     * @throws IOException if an I/O error occurs while reading the file.
     */
    public static String Read(String relativeFilepath) throws IOException {
        StringBuilder content = new StringBuilder();
        Path path = Paths.get(relativeFilepath);
        try (BufferedReader reader = new BufferedReader(new FileReader(path.toFile()))) {
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line).append(System.lineSeparator());
            }
        }
        // Remove the last newline character if the file is not empty
        if (content.length() > 0) {
            content.delete(content.length() - System.lineSeparator().length(), content.length());
        }
        return content.toString();
    }


}