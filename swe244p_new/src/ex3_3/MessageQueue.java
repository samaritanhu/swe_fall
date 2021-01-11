package ex3_3;

import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;

// Task:
// Complete the missing pieces. The program should behave correctly, in that no messages should be lost. Make sure that the sum of all sent messages equals the sum of all received messages.
// Change the main method so that two consumer threads are created, both of them consuming messages from the single queue. Your program should stop gracefully, as in 1.
// Change the main method so that, additionally to the two consumer threads of the previous point, two producer threads are created, both of them sending messages to the single queue.
// Finally, change the main method so that N consumers and M producers are created. N and M should be given as command line arguments to the program.

public class MessageQueue {
    private static int n_ids;

    public static void main(String[] args) {
    	// Here, we can use arrayBlockingQueue (based on array and have a fix size)
		// or LinkedBlockingQueue (based on linkedlist and size could be change)
        BlockingQueue<Message> queue = new ArrayBlockingQueue<Message>(10);
        Producer p1 = new Producer(queue, n_ids++);
        Consumer c1 = new Consumer(queue, n_ids++);

        new Thread(p1).start();
        new Thread(c1).start();

        try {
            Thread.sleep(10000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        p1.stop();
    }
}
