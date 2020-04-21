var express = require('express');
var router = express.Router();

let index = require('../controllers/index')

/* GET home page. */
router.get('/',index.index );
router.get('/zoo',index.index);
router.get('/camel',index.camel);
router.get('/monkey',index.monkey);
router.get('/cow',index.cow);
router.get('/crocodile',index.croc);
router.post('/clicked', index.clicked);

module.exports = router;
