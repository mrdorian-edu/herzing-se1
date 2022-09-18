/* 
 * IS341 - SOFTWARE ENGINEERING 1
 * DORIAN BRANDUSA
 * DBRANDUSA@HERZING.EDU
 * UNIT 2 | ASSIGNMENT 1 | FINITE STATE MACHINE TEST
 */

package WeatherSimulation;
import java.util.Random;

public class WeatherSimulation {

  public static void main(String[] args) {

    Random rand = new Random();

    // initialization
    int day = 1;
    String states = "Clear";
    String event = "";

    // 7 day simulation
    while (day <= 7) {

      // event changes
      for (int i = 1; i <= 5; i++) {

        // determination
        int eventNum = rand.nextInt(3);

        // change status
        if (eventNum == 0) {
        	
          if (states.equals("Clear")) {
            states = "Cloudy";
            event = "Getting Warmer";
            
          } else if (states.equals("Cloudy")) {
            states = "Raining";
            event = "Getting Colder";
            
          } else if (states.equals("Raining")) {
            states = "Severe Weather";
            event = "Humidity is Increasing";
            
          } else if (states.equals("Severe Weather")) {
            states = "Clear";
            event = "Wind is Increasing";
          }
          
        } else if (eventNum == 1) {
          event = "No Change";
          
        } else if (eventNum == 2) {
        	
          if (states.equals("Clear")) {
            states = "Cloudy";
            event = "Getting Warmer";
            
          } else if (states.equals("Cloudy")) {
            states = "Raining";
            event = "Getting Colder";
            
          } else if (states.equals("Raining")) {
            states = "Severe Weather";
            event = "Wind is Increasing";
            
          } else if (states.equals("Severe Weather")) {
            states = "Clear";
            event = "Humidity is Increasing";
          }
          
        }

        // display results
        System.out.println("Day " + day + ": " + event);
      }

      // increment
      day++;
    }
  }
}