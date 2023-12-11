import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader bf = new BufferedReader(new FileReader("/home/ad/Documents/code/advcalendar/2023/day1/data.txt"));
        String[] lines = bf.lines().toArray(String[]::new);             
        double[] data = new double[lines.length];

        for (int i = 0; i < lines.length; i++){
            data[i] = Double.parseDouble(lines[i]);
        }

        double t = 0;
        for (double d : data){
            t += d;
        }

        System.out.println(t/data.length);
    }
}
