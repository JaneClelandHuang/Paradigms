public class PrimePrinter2 {
	public static void main(String[] args) {
		for (int j = 1; j < 10; j++) {
			new Thread(() -> {
				for (int i = 1; i <= 100000; i++) {
					final int candidate = i;
					for (int divisor = 2; divisor <= candidate; divisor++){
						if (divisor == candidate) {
							synchronized (System.out) {
								System.out.print(" " + candidate);
							}
						} else if (candidate % divisor == 0) {
							break;
						}
					}
				}
			}).start();
		}
	}
}