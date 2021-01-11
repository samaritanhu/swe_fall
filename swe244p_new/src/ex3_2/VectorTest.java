package ex3_2;

import java.util.Vector;

// Error: ArrayIndexOutOfBoundsException
// Reason: Array index out of range: 0
// Solution: synchronized - put a lock on the operation of vector
// If one thread uses getLast function which does not finish,
// another thread uses the deleteLast function - which makes vector size 0
// the first thread using getLast would get nothing at index 0 because vector size is 0.

public class VectorTest {

    private boolean running = true;
    private Vector<String> people = new Vector<String>();

    private synchronized void addPerson() {
	people.add(RandomUtils.randomString());
    }

    private synchronized String getLast() {
	int lastIndex = people.size() - 1;
	if (lastIndex >= 0)
	    return people.get(lastIndex);
	else return "";
    }

    private synchronized void deleteLast() {
	int lastIndex = people.size() - 1;
	if (lastIndex >= 0)
	    people.remove(lastIndex);
    }

    public void run() {
	// Start getter thread
	new Thread(new Runnable () {
		public void run() {
		    Thread.currentThread().setName("Getter");
		    while (running) {
			String person = getLast();
			System.out.println("Last: " + person);
			try {
			    Thread.sleep(200);
			} catch (InterruptedException e) {}
		    }
		}
	    }).start();

	// Start deleter thread
	new Thread(new Runnable () {
		public void run() {
		    Thread.currentThread().setName("Deleter");
		    while (running) {
			deleteLast();
			try {
			    Thread.sleep(200);
			} catch (InterruptedException e) {}
		    }
		}
	    }).start();

	// This thread adds entries
	for (int i = 0; i < 100; i++) {
	    addPerson();
	    try {
		Thread.sleep(200);
	    } catch (InterruptedException e) {}
	}
	running = false;
    }

    public static void main(String[] args) {
	VectorTest hm = new VectorTest();
	hm.run();
    }

}
