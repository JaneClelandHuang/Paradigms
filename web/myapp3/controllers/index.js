exports.index = function(req, res, next) {
  res.render('index', { title: 'ZOOm for Animals' , animal_name:
 'Zoo Animals', image_name: 'zoo.jpg'});
}

exports.clicked = function(req, res, next) {
  console.log("Clicked on button");
  res.redirect('images/camel');
}

exports.camel = function(req, res, next) {
   res.render('camel', { title: 'Hello Express' , animal_name:'Camel', image_name: "images/camel.jpg"}); 
}

exports.croc = function(req, res, next) {
   res.render('camel', { title: 'Hello Express' , animal_name:'Crocodile'}); 
}

exports.cow = function(req, res, next) {
   res.render('camel', { title: 'Hello Express' , animal_name:'Cow'}); 
}

exports.monkey = function(req, res, next) {
   res.render('camel', { title: 'Hello Express' , animal_name:'Monkey'}); 
}

