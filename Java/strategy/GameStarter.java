package edu.nd.secourse.strategy;
import edu.nd.secourse.strategy.ducks.MallardDuck;
import edu.nd.secourse.strategy.fly.FlyNoWay;
import edu.nd.secourse.strategy.fly.FlyWithWings;
import edu.nd.secourse.strategy.quack.Peep;
import edu.nd.secourse.strategy.quack.QuackLikeADuck;

/**
 * Sets up game
 * @author Jane
 *
 */
public class GameStarter {
	
	public void setup(){
		MallardDuck mallard = new MallardDuck(new FlyWithWings(), new QuackLikeADuck());
		mallard.doYourThing();
		mallard.setFlyStrategy(new FlyNoWay());
		mallard.setQuackStrategy(new Peep());
		mallard.doYourThing();
	}
	
	// Any ways to improve the design?
	public static void main(String[] args) {
		GameStarter gameStarter = new GameStarter();
		gameStarter.setup();
	}

}
