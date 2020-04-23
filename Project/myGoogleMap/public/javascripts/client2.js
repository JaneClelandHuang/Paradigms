var map;

function test(myMarker){
	console.log(myMarker);
}

function initMap() {
   // Zoo center point
   var potowatami = {
     lat: 41.670241,
     lng: -86.218401
   };
   
   var map = new google.maps.Map(document.getElementById('map'), {
   center: potowatami,
   zoom: 18,
   mapTypeId: 'satellite'
   });
   
   // Animal locations
   var monkeyCage = {
     lat: 41.670768,
   	 lng: -86.217297
   };
   var camelCage = {
     lat: 41.670088,
   	 lng:  -86.218338
   };   
   var cowCage = {
     lat: 41.670850,
   	 lng: -86.219570
   };   
   var crocCage = {
     lat: 41.669926,
   	 lng: -86.220068
   };
   var marker = new google.maps.Marker({
	 position: monkeyCage,
	 label: { color: '#f7f7f7', fontWeight: 'bold', fontSize: '10px', text: 'Monkeys' },
     map: map
   });
   var marker = new google.maps.Marker({
     position: camelCage,
     label: { color: '#f7f7f7', fontWeight: 'bold', fontSize: '10px', text: 'Camels' },
     map: map
   });
   var marker = new google.maps.Marker({
     position: cowCage,
     label: { color: '#f7f7f7', fontWeight: 'bold', fontSize: '10px', text: 'Cows' },
     map: map
   });
   var marker = new google.maps.Marker({
     position: crocCage,
     label: { color: '#f7f7f7', fontWeight: 'bold', fontSize: '10px', text: 'Crocodiles' },
     map: map
   });

}
