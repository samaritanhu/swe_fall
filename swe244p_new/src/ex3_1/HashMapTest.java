package ex3_1;

import java.util.HashMap;
import java.util.Vector;

// Your task: make HashMapTest thread safe, so that those exceptions do not happen.
// For the purposes of this exercises, it's not enough to catch the exceptions;
// you need to prevent them from happening in the first place.

// Exception encountered: ConcurrentModificationException
// Reason: expectedModCount doesn't match modCount
// Solution: synchronized - put a lock on the operation of hashmap
// For one-thread program, it can use Iterator to go through every element in list or set
// However, for multithread program, it will change the value of modcount which may cause the situation that expectedModCount dose not match modCount
// In this case, ConcurrentModificationException appears.


public class HashMapTest {

    private boolean running = true;
    private HashMap<String, Integer> people = new HashMap<String, Integer>();

    private synchronized void addPerson() {
        people.put(RandomUtils.randomString(), RandomUtils.randomInteger());

    }

    private synchronized void deletePeople(String pattern) {
        Vector<String> hasPattern = new Vector<String>();
        for (String key : people.keySet()) {
            if (key.contains(pattern))
                hasPattern.add(key);
        }
        for (String key : hasPattern)
            people.remove(key);

    }

    private synchronized void printPeople() {
        for (HashMap.Entry<String, Integer> entry : people.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
        System.out.println("-----------------------------------------");

    }

    public void run() {
        // Start printer thread
        new Thread(new Runnable() {
            public void run() {
                Thread.currentThread().setName("Printer");
                while (running) {
                    printPeople();
                    try {
                        Thread.sleep(200);
                    } catch (InterruptedException e) {
                    }
                }
            }
        }).start();

        // Start deleter thread
        new Thread(new Runnable() {
            public void run() {
                Thread.currentThread().setName("Deleter");
                while (running) {
                    deletePeople("a");
                    try {
                        Thread.sleep(200);
                    } catch (InterruptedException e) {
                    }
                }
            }
        }).start();

        // This thread adds entries
        for (int i = 0; i < 100; i++) {
            addPerson();
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
            }
        }
        running = false;
    }

    public static void main(String[] args) {
        HashMapTest hm = new HashMapTest();
        hm.run();
    }

}
