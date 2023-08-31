import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

public class WebDataSearch {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Digite a URL: ");
        String url = reader.readLine();
        System.out.print("Digite o tipo de dado: ");
        String data_type = reader.readLine();
        System.out.print("Digite o tipo de arquivo: ");
        String file_type = reader.readLine();

        String result = searchWebData(url, data_type, file_type);
        System.out.println(result);
    }

    public static String searchWebData(String url, String data_type, String file_type) throws IOException {
        URL urlObj = new URL(url + "?data_type=" + data_type + "&file_type=" + file_type);
        HttpURLConnection connection = (HttpURLConnection) urlObj.openConnection();
        BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));

        StringBuilder response = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            response.append(line);
        }

        reader.close();
        return response.toString();
    }
}
