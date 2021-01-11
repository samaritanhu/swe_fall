package ex2_2;

public class TrafficController {
    // Using lock with notify and wait method in Object class
    private Object lock = new Object();
    // number of cars in the left
    private int left = 0;
    // number of cars in the right
    private int right = 0;


    public void enterLeft() {
        synchronized (lock) {
            // If there is car in the right
            while (right != 0) {
                try {
                    // wait for notify if there are still cars on the bridge
                    lock.wait();
                    // wait would block this thread
                } catch (InterruptedException e) {
                    // An InterruptedException is thrown when a thread that is sleeping, waiting, or is occupied is interrupted.
                    e.printStackTrace();
                }
            }
            // pass the bridge if there is no car in the right
            left++;
        }

    }

    public void enterRight() {
        synchronized (lock) {
            while (left != 0) {
                try {
                    lock.wait();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            right++;
        }

    }

    public void leaveLeft() {
        // If car have went through the bridge
        // it will notify all the thread blocked by wait method
        // thread will judge whether it's able to get on the bridge. If not, it will block again
        synchronized (lock) {
            try {
                // the number of car on bridge minus 1
                right--;
                // try to notify the waiting car
                lock.notify();
            } catch (Exception e) {
                e.printStackTrace();
            }

        }
    }

    public void leaveRight() {
        synchronized (lock) {
            try {
                left--;
                lock.notify();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

}