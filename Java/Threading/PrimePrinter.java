public class PrimePrinter {
	public static void main(String[] args) {
		for (int i = 1; i <= 10000; i++) {
			final int candidate = i;
			new Thread(() -> {
				for (int divisor = 2; divisor <= candidate; divisor++){
					if (divisor == candidate) {
						synchronized (System.out) {
							System.out.print(" x" + candidate);
						}
					} else if (candidate % divisor == 0) {
						break;
					}
				}
			}).start();
		}
	}
}