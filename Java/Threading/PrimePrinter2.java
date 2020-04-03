public class PrimePrinter2 {
	public static void main(String[] args) {
		for (int j = 1; j < 10; j++) {
			String threadName = "Thread-" + ((Integer)i).toString();
			new Thread(() -> {
				int primeSum = 0;
				synchronized (System.out) {
					System.out.println("Starting " + Thread.currentThread().getName());
				}
	
				synchronized (System.out) {
					System.out.println("Ending " + Thread.currentThread().getName() + " " + primeSum);
				}
			}).start();
		}
	}
}