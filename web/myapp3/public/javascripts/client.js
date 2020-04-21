console.log('Client-side code running');

const camelButton = document.getElementById('camelButton');
camelButton.addEventListener('click', function(e) {
  console.log('Camel button was clicked');
  location.href = "http://localhost:3000/camel"; 
});

const monkeyButton = document.getElementById('monkeyButton');
monkeyButton.addEventListener('click', function(e) {
  console.log('Monkey button was clicked');
  location.href = "http://localhost:3000/monkey"; 
});

const crocButton = document.getElementById('crocButton');
crocButton.addEventListener('click', function(e) {
  console.log('Crocodile button was clicked');
  location.href = "http://localhost:3000/crocodile"; 
});

const cowButton = document.getElementById('cowButton');
cowButton.addEventListener('click', function(e) {
  console.log('Cow button was clicked');
  location.href = "http://localhost:3000/cow"; 
});

function getImage(animal) {
  switch(animal) {
    case "camel":
      myImage = img(src='images/camel.jpg',style='width:500px')
    break;
    default:
      myImage = img(src='images/zoo.jpg',style='width:500px')
    break;
  }
  document.getElementById("animalImage").innerHTML = myImage;
}