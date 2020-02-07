let convert = require('./pilots2.js');
let assert = require('assert');

describe('Pilots Employees',function(){
	describe('human resources',function(){
		it('should find a pilot if they are on the list', function() {
			assert.equal(true, pilots2.hasPilotNamed("Lintra");
		});
		it('should fail to find a pilot if they are not on the list', function() {
			assert.equal(false, pilots2.hasPilotNamed("Paul");
		});
	});
});
