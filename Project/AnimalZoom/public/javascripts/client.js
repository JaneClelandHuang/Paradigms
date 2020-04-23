console.log('Client-side code running');
// LOCAL USE:
const myURL = "http://localhost:3000";

// STUDENT 04 use:
//const myURL = "http://student04.cse.nd.edu:51000";

const zoomButton = document.getElementById('zoomButton');
zoomButton.addEventListener('click', function(e) {
  console.log('Zoom button was clicked');
  location.href = myURL.concat("/zoom")
});

const zooButton = document.getElementById('zooButton');
zooButton.addEventListener('click', function(e) {
  console.log('Zoo button was clicked');
  location.href = myURL.concat("/zoo");
  console.log("Pushing " + href);
  //document.getElementById("AnimalImage").src ="images/zoo.jpg"
  //document.getElementById("p2").innerHTML = "Welcome to the zoo.";
  //document.getElementById("p1").innerHTML = "Zoo Animals"; 
});

const camelButton = document.getElementById('camelButton');
camelButton.addEventListener('click', function(e) {
  console.log('Camel button was clicked');
  location.href = myURL.concat("/camel")
  //document.getElementById("AnimalImage").src ="images/camel.jpg"
  //document.getElementById("p2").innerHTML = "Camels are mammals with long legs, a big-lipped snout and a humped back.!";
  //document.getElementById("p1").innerHTML = "Cherry Camel"; 
});

const monkeyButton = document.getElementById('monkeyButton');
monkeyButton.addEventListener('click', function(e) {
  console.log('Monkey button was clicked');
  location.href = myURL.concat("/monkey")
  //document.getElementById("AnimalImage").src ="images/monkey.jpg";
  //document.getElementById("p2").innerHTML = "Monkeys live in trees, grasslands, mountains, forests, and on high plains. Each monkey has its own unique fingerprints.";
  //document.getElementById("p1").innerHTML = "Mindy Monkey"; 
});

const crocButton = document.getElementById('crocButton');
crocButton.addEventListener('click', function(e) {
  console.log('Crocodile button was clicked');
  location.href = myURL.concat("/crocodile") ;
  //document.getElementById("AnimalImage").src ="images/crocodile.jpg";
  //document.getElementById("p2").innerHTML = "Crocodiles are repitles with sharp teeth.  They can run very fast over short distances.";
  //document.getElementById("p1").innerHTML = "Craig Crocodile"; 
});

const cowButton = document.getElementById('cowButton');
cowButton.addEventListener('click', function(e) {
  console.log('Cow button was clicked');
  location.href = myURL.concat("/cow");
  //document.getElementById("AnimalImage").src ="images/cow.jpg"
  //document.getElementById("p2").innerHTML = "Cows are ruminants, which are cud chewing mammals. Sheep and camels also are ruminants. A cow chews her cud (regurgitated, partially digested food) for up to 8 hours each day.";
  //document.getElementById("p1").innerHTML = "Chloe Cow";  
});

