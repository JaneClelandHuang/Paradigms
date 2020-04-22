var express = require('express');
var router = express.Router();

let index = require('../controllers/index')

/* GET home page. */
router.get('/',index.index );
router.get('/zoo',index.zoo);
router.get('/camel',index.camel);
router.get('/monkey',index.monkey);
router.get('/cow',index.cow);
router.get('/crocodile',index.croc);

module.exports = router;
