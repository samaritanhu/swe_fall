// Author: Xinyi Hu
// Email: xinyih20@uci.edu

// Target: Write a program that creates multiple threads (additionally to the main thread).
// Each of the threads should execute a loop that prints "Hello World! I'm thread <thread id>.
// The time is <current time>" on the screen, sleep for 2 seconds, and repeat, until it is stopped.

package ex1;

import java.util.*;


class myThread extends Thread {
    private volatile boolean isShutdown = true;

    public void shutdown() {
        this.isShutdown = false;
        interrupt();
    }

    @Override
    public void run() {
        while (this.isShutdown) {
            // "Hello World! I'm thread <thread id>.
            //// The time is <current time>"
            System.out.println("Hello World! I'm " + this.getName() + ". The time is " + System.currentTimeMillis());
            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                // An InterruptedException is thrown when a thread that is sleeping, waiting, or is occupied is interrupted.
                System.out.println("Stop " + this.getName());
            }
        }
    }
}

public class ex1 {
    public static void main(String[] args) {
        Scanner sc = null;
        boolean flag = true;
        // map <id , thread> by hashmap
        HashMap<String, myThread> threadsGroup = new HashMap<String, myThread>();
        try {
            sc = new Scanner(System.in);
            while (flag) {
                System.out.println("Here are your options:\n" +
                        "a - Create a new thread\n" +
                        "b - Stop a given thread (e.g. \"b 2\" kills thread 2)\n" +
                        "c - Stop all threads and exit this program\n");
                String input = sc.nextLine();
                if (input.equals("a")) {
                    // Create a new thread
                    myThread newThread = new myThread();
                    // newThread.getName() is Thread-1, its number is substring(7)
                    threadsGroup.put(newThread.getName().substring(7), newThread);
                    newThread.start();
                } else if (input.startsWith("b")) {
                    // Stop a given thread
                    // thread number is "b number", so use substring(2) here
                    String index = input.substring(2);
                    if (!threadsGroup.containsKey(index)) {
                        System.out.println("No thread " + index);
                    } else {
                        threadsGroup.get(index).shutdown();
                        threadsGroup.remove(index);
                        System.out.println("Thread " + index + " is killed.");
                    }

                } else if (input.equals("c")) {
                    // Get the keys and shutdown the thread one by one
                    flag = false;
                    for (String index : threadsGroup.keySet()) {
                        threadsGroup.get(index).shutdown();
                    }
                    threadsGroup = null;
                    System.out.println("All of the threads are killed! Exit the program.");

                } else {
                    // If user input is not defined
                    System.out.println("Please check your input!\n");
                }

            }
        } catch (Exception e) {
            // If we encounter an exception, use printStackTrace to trace the bug
            e.printStackTrace();
        } finally {
            // No matter what, "finally" will be executed
            if (sc != null) {
                sc.close();
                sc = null;
            }
        }
    }
}