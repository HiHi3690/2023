import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main2 {
    public static void main(String[]args) throws FileNotFoundException{    
        Scanner s = new Scanner(new File("/home/ad/Documents/code/advcalendar/2023/day1/data.txt"));
        ArrayList<String> list = new ArrayList<String>();
        while (s.hasNext()){
            list.add(s.next());
        }
        s.close();

        
    }  
}
