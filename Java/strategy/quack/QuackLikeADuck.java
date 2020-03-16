package edu.nd.secourse.strategy.quack;

public class QuackLikeADuck implements IQuackStrategy{

	@Override
	public void quack() {
		System.out.println("Duck says Quack, Quack, Quack");		
	}

}
