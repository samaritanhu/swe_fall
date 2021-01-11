package ex3_4;
// Author: Xinyi Hu
// Email: xinyih20@uci.edu

// Task Description
//  you should not change JDisplay2, so, leave unsafe.
//  Instead, solve the synchronization problems with a semaphore outside JDisplay2.

import java.util.concurrent.Semaphore;

public class Main3 {
    // When semaphore's size is 1, it will just works like a lock
//    static Semaphore semaphore = new Semaphore(1);

    private static void nap(int millisecs) {
        try {
            Thread.sleep(millisecs);
        } catch (InterruptedException e) {
            System.err.println(e.getMessage());
        }
    }

    private static void addProc(HighLevelDisplay d, Semaphore semaphore) {

        // Add a sequence of addRow operations with short random naps.
        int i = 0;
        while (true) {
            try {
                // acquire method is to get one semaphore
                // if the available semaphore is 0, this thread will be blocked
                semaphore.acquire();
            } catch (InterruptedException e) {
                System.err.println(e.getMessage());
            }
            d.addRow("AAAAAAAAAAAA  " + i);
            d.addRow("BBBBBBBBBBBB  " + i);
            // release the lock
            semaphore.release();
            i++;
            nap(500);
        }
    }

    private static void deleteProc(HighLevelDisplay d, Semaphore semaphore) {

        // Add a sequence of deletions of row 0 with short random naps.
        while (true) {
            try {
                semaphore.acquire();
            } catch (InterruptedException e) {
                System.err.println(e.getMessage());
            }
            d.deleteRow(0);
            semaphore.release();
            nap(5000);
        }
    }

    public static void main(String[] args) {
        final HighLevelDisplay d = new JDisplay2();
        Semaphore s = new Semaphore(1);

        new Thread() {
            public void run() {
                addProc(d, s);
            }
        }.start();


        new Thread() {
            public void run() {
                deleteProc(d, s);
            }
        }.start();

    }
}