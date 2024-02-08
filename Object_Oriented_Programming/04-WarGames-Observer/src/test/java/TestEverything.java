import org.junit.*;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;

import static org.junit.Assert.assertEquals;

public class TestEverything {
    General Erick;
    General AntiErick;
    @Before
    public void Setup(){

        // Create soldiers
        Soldier Ryan = new Soldier("Ryan", 1, 10);
        Soldier Brian = new Soldier("Brian", 1, 1);
        Soldier Greg = new Soldier("Greg", 2, 2);
        Soldier Kamil = new Soldier("Kamil", 2, 3);
        Soldier Cris = new Soldier("Cris", 3, 5);
        Soldier Pat = new Soldier("Pat", 3, 6);

        // Create generals
        Erick = new General(200);
        Erick.AddSoldier(Ryan);
        Erick.AddSoldier(Greg);
        Erick.AddSoldier(Cris);

        AntiErick = new General(300);
        AntiErick.AddSoldier(Brian);
        AntiErick.AddSoldier(Kamil);
        AntiErick.AddSoldier(Pat);

        // Create Secretaries
        Secretary secErick = new Secretary();
        Erick.AddObserver(secErick);
        Secretary secAnti = new Secretary();
        AntiErick.AddObserver(secAnti);


    }


    @Test
    public void Example(){
        // Create things
        int expected, result;
        expected = 10;
        result = 2*2*2+2;
        assertEquals("Wiadomosc", expected, result);
    }

    @Test
    public void Atack(){
        //System.out.println(AntiErick);
        int before = AntiErick.getArmy().size();
        AntiErick.Attack(Erick);
        int after = AntiErick.getArmy().size();

        //System.out.println(AntiErick);
        //System.out.println(Erick);
        assertEquals("General atakuje drugiego generala", 1, before - after);
    }

    @Test
    public void Manewry(){
        //int ArmySize = AntiErick.getArmy().size();
        int before = AntiErick.TotalStrenght();
        AntiErick.Manewry();
        int after = AntiErick.TotalStrenght();

        assertEquals("Manewry przez wszystkich zolnierzy armii", 6,(int) after - before);
    }

    @Test
    public void ManewrySpecyfic(){
        int before = AntiErick.TotalStrenght();
        ArrayList<Soldier> army = AntiErick.getArmy();
        ArrayList<Soldier> specific = new ArrayList<>();
        specific.add(army.get(0));
        specific.add(army.get(2));
        AntiErick.Manewry(specific);
        int after = AntiErick.TotalStrenght();

        //System.out.println(AntiErick);
        assertEquals("Manewry przez konkretnych zolnierzy", 4,after - before);
    }

    @Test
    public void BuySoilder(){
        //int ArmySize = AntiErick.getArmy().size();
        int before = AntiErick.TotalStrenght();
        AntiErick.BuySoilder(1);
        int after = AntiErick.TotalStrenght();

        assertEquals("Manewry przez wszystkich zolnierzy armii", 1,(int) after - before);
    }

    @Test
    public void SaveToFile(){
        String filePath = "ErickArmy.txt";
        Erick.SaveArmy(filePath);
        ArrayList<String> result = new ArrayList<>();
        try {
            // Read all lines from the file into a List
            ArrayList<String> linesFile = (ArrayList<String>) Files.readAllLines(Paths.get(filePath));
            result = linesFile;
        } catch (IOException e) {
            // Handle exceptions, such as file not found or permission issues
            e.printStackTrace();
        }

        ArrayList<String> expected = new ArrayList<>();
        for(Soldier soldier : Erick.getArmy()){
            expected.add(String.join(";", soldier.Save()));
        }
        assertEquals("Zapisywanie do pliku armii", expected, result);
    }

    @Test
    public void LoadFromFile(){
        String filePath = "LoadArmy.txt";
        try (PrintWriter writer = new PrintWriter(new FileWriter(filePath))) {
            writer.println("Tomek;1;4;true");
            System.out.println("Army saved to file: " + filePath);
        } catch (IOException e) {
            // Handle exceptions, such as file not found or permission issues
            e.printStackTrace();
        }
        Erick.LoadArmy(filePath);
        assertEquals("Zaladowywanie armii z pliku", "[Soldier Tomek{stopien=1, experience=4, isAlive=true}]", Erick.toString());
    }

}
