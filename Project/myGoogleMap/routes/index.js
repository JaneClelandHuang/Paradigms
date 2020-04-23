var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index',{markers:'Zoom Time'});
});

router.post('/',function(req,res,next) {
  res.render('index');
})

module.exports = router;
