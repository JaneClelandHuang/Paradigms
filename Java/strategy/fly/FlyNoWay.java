package edu.nd.secourse.strategy.fly;

public class FlyNoWay implements IFlyStrategy{

	@Override
	public void fly() {
		System.out.println("Duck cannot fly");		
	}

}
