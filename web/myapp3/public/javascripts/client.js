console.log('Client-side code running');

const zooButton = document.getElementById('zooButton');
zooButton.addEventListener('click', function(e) {
  console.log('Zoo button was clicked');
  //location.href = "http://localhost:3000/"; 
  document.getElementById("AnimalImage").src ="images/zoo.jpg"
});

const camelButton = document.getElementById('camelButton');
camelButton.addEventListener('click', function(e) {
  console.log('Camel button was clicked');
  //location.href = "http://localhost:3000/camel"; 
  document.getElementById("AnimalImage").src ="images/camel.jpg"
});

const monkeyButton = document.getElementById('monkeyButton');
monkeyButton.addEventListener('click', function(e) {
  console.log('Monkey button was clicked');
  //location.href = "http://localhost:3000/monkey"; 
  document.getElementById("AnimalImage").src ="images/monkey.jpg"
});

const crocButton = document.getElementById('crocButton');
crocButton.addEventListener('click', function(e) {
  console.log('Crocodile button was clicked');
  //location.href = "http://localhost:3000/crocodile"; 
  document.getElementById("AnimalImage").src ="images/crocodile.jpg"
});

const cowButton = document.getElementById('cowButton');
cowButton.addEventListener('click', function(e) {
  console.log('Cow button was clicked');
  //location.href = "http://localhost:3000/cow"; 
  document.getElementById("AnimalImage").src ="images/cow.jpg"
});

