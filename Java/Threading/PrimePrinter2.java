public class PrimePrinter2 {
	public static void main(String[] args) {
		for (int j = 1; j < 10; j++) {
			new Thread(("Thread-" + ((Integer)i).toString()) -> {
				int primeSum = 0;
				synchronized (System.out) {
					System.out.println("Starting " + Thread.currentThread().getName());
				}
				for (int i = 1; i <= 100000; i++) {
					final int candidate = i;
					for (int divisor = 2; divisor <= candidate; divisor++){
						if (divisor == candidate) {
							primeSum += candidate;
						} else if (candidate % divisor == 0) {
							break;
						}
					}
				}
				synchronized (System.out) {
					System.out.println("Ending " + Thread.currentThread().getName() + " " + primeSum);
				}
			}).start();
		}
	}
}