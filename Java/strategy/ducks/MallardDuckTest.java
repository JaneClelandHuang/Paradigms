package edu.nd.secourse.strategy.ducks;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import edu.nd.secourse.strategy.fly.FlyWithWings;
import edu.nd.secourse.strategy.quack.QuackLikeADuck;

public class MallardDuckTest {

	MallardDuck mallard;
	
	@Before
	public void setUp() throws Exception {
		mallard = new MallardDuck(new FlyWithWings(), new QuackLikeADuck());
	}

	@After
	public void tearDown() throws Exception {
	}

	@Test
	public void testFlyingStrategy() {
		assert(mallard.getFlyStrategy() instanceof FlyWithWings);
	}
	
	@Test
	public void testQuackStrategy() {
		assert(mallard.getQuackStrategy() instanceof QuackLikeADuck);
	}

}
