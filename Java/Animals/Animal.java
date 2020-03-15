abstract class Animal {
	private String name;
	public Animal(String name) {
		this.name = name;
	}
	abstrat String sound();
	public String speak() {
		return name + " says " + sound();
	}
}