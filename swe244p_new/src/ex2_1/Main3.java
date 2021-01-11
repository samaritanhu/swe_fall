// The exercise itself uses Main3.
// Your task is to write a simple multi-threaded program, a skeleton of which is already in Main3.
// Main3.java shows the structure of a simple main program that creates a display d and starts two threads,
// one executing the static procedure addProc(d), the other executing deleteProc(d).
// You must complete the bodies of these two procedures.
// Fill addProc with a sequence of addRow commands, interspersed with suitable naps.
// Similarly, fill deleteProc with calls to deleteRow(0).
// To allow for a not too boring simulation, naps should be in the order of seconds (or fractions of seconds)
// and not minutes as in a real airport.

package ex2_1;

import java.util.concurrent.*;

public class Main3 {

    private static void nap(int millisecs) {
        try {
            Thread.sleep(millisecs);
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    private static void addProc(HighLevelDisplay d) {

        // Add a sequence of addRow operations with short random naps.
        int i = 0;
        while (true) {
            d.addRow("AAAAAAAAAAAA  " + i);
            // d.addRow("BBBBBBBBBBBB " + i);
            i++;
            nap(50);
        }
    }

    private static void deleteProc(HighLevelDisplay d) {

        // Add a sequence of deletions of row 0 with short random naps.
        while (true) {
            d.deleteRow(0);
            nap(250);
        }
    }

    public static void main(String[] args) {
        final HighLevelDisplay d = new JDisplay2();

        new Thread() {
            public void run() {
                addProc(d);
            }
        }.start();


        new Thread() {
            public void run() {
                deleteProc(d);
            }
        }.start();

    }
}