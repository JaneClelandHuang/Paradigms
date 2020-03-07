var latlon = "40.7300694,-74.0024224"; // Sample Lat,Long (Manhattan NYC)
var distance_between_people = 40; // Keep 40 pixels between people on map
var max_map_people = 40; // Attempt to put 40 people on map

var $people_layer = $('.people');

// Create an in-memory canvas and store its 2d context
var water_context = document.createElement('canvas');
water_context.setAttribute('width', 1024);
water_context.setAttribute('height', 160);
water_context = water_context.getContext('2d');

// Assumes <canvas> element already in DOM with class "map"
var map_context = $('canvas.map')[0].getContext('2d');

var map = new Image();
map.crossOrigin = 'http://maps.googleapis.com/crossdomain.xml';
map.src = "http://maps.googleapis.com/maps/api/staticmap?scale=2&center=" + latlon + "&zoom=13&size=1024x160&sensor=false&visual_refresh=true";

map.onload = function(){
  // Put the map image inside the canvas once it loads
  map_context.drawImage(map, 0, 0, 1024, 256);

  water = new Image();
  water.crossOrigin = 'http://maps.googleapis.com/crossdomain.xml';
  water.src = "http://maps.googleapis.com/maps/api/staticmap?scale=2&center=" + latlon + "&zoom=13&size=1024x160&sensor=false&visual_refresh=true&style=element:labels|visibility:off&style=feature:water|color:0x00FF00&style=feature:transit|visibility:off&style=feature:poi|visibility:off&style=feature:road|visibility:off&style=feature:administrative|visibility:off";

  water.onload = function(){
    // Put the water image inside the water canvas
    water_context.drawImage(water, 0, 0, 1024, 256);
    render_random_people();
  }
}

function render_random_people(){
  $people_layer.empty();

  var tries = 0,
  drawn = [];

  // Give up after 2 * map_num_people tries in case it's not possible to place map_num_people icons on the map
  while(tries < max_map_people * 2 && drawn.length < max_map_people){
    tries++;

    // 5px padding around edges (1024 x 160 pixel Map)
    x = _.random(5, 1019);
    y = _.random(5, 155);

    // Skip this random (x,y) pair if it's nearby any currently drawn person
    if( any_people_nearby(drawn, x, y) ) continue;

    // Get the RGB colors at the given random pixel
    pixels = water_context.getImageData(x, y, 1, 1).data;

    // Skip if the pixel is water
    if( color_is_water(pixels) ) continue;

    // Append the icon to the layer (not all CSS included here)
    $people_layer.append('<div class="person" style="top:' + y + 'px;left:' + x + 'px"></div>');

    // Store record of where the person was drawn so nothing overlaps later
    drawn.push({x: x, y: y});
  }
}

function any_people_nearby(current_people, x, y){
  // Return true if any current_people have an (x,y) pair closer than distance_between_people
  return _.some(current_people, function(coords){
    var distance = Math.pow( Math.pow(x - coords.x, 2) + Math.pow(y - coords.y, 2), .5);
    return distance <= distance_between_people;
  });
}

function color_is_water(bytes){
  // Return true if the color is #00FF00 (Lime Green passed to Google Maps as water style property)
  var water_color_bytes = [0, 255, 0],
  our_color_bytes = [bytes[0], bytes[1], bytes[2]];
  return _.isEqual(water_color_bytes, our_color_bytes);
}