class demoClass { 
	int a = 1; 
	void func()	{ 
		demo obj = new demo(); 
		obj.display(); 
	} 

	class demo 	{ 
		int b = 2; 
		void display() { 
			System.out.println("\na = " + a); 
		} 
	} 

	void get() { 
		System.out.println("\nb = " + b); 
	} 
} 

class TypeDemo4 { 
	public static void main(String[] args) { 
		demoClass obj = new demoClass(); 
		obj.func(); 
		obj.get(); 
	} 
} 
