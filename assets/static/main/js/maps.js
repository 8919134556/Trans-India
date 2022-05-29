var myLatLng = { lat: 0.0, lng: 0.0 };
var mapOptions = {
    center: myLatLng,
    zoom: 1,
    mapTypeId: google.maps.MapTypeId.ROADMAP
};

// Hide result box
document.getElementById("output1").style.display = "none";

// Create/Init map
var map = new google.maps.Map(document.getElementById('google-map'), mapOptions);

// Create a DirectionsService object to use the route method and get a result for our request
var directionsService = new google.maps.DirectionsService();

// Create a DirectionsRenderer object which we will use to display the route
var directionsDisplay = new google.maps.DirectionsRenderer();

// Bind the DirectionsRenderer to the map
directionsDisplay.setMap(map);


// Define calcRoute function
function calcRoute() {
    //create request
    var request = {
        origin: document.getElementById("location-1").value,
        destination: document.getElementById("location-2").value,
        
        travelMode: google.maps.TravelMode.DRIVING,
        unitSystem: google.maps.UnitSystem.METRIC
    }

    // Routing
    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {

            //Get distance and time            
            
            
            $("#output1").html("<div class='result-table text-dark'><table><tbody><tr><td><img style='width :80px; border-radius: 5px' src = "+ document.getElementById("image").getAttribute('src') + "></td> <td><input name='starting' hidden type='text'  style='width :20%; font-size: 5px;' value ="+ document.getElementById("location-1").value +" readonly></td> <td> <input name='ending' hidden type='text' style='width :50%' value ="+ document.getElementById("location-2").value +" readonly></td> <td> Driving distance: <input name='distance' id='surya' type='text' style='width :25%' value ="+ result.routes[0].legs[0].distance.text +" readonly> </td> <td><input type='text' hidden name='subtotal'  style='width :25%' value ="+ (result.routes[0].legs[0].distance.value*document.getElementById("demo").value)/1000  +" readonly></td> <td><input type='text' hidden name='gst'  style='width :25%' value ="+ ((result.routes[0].legs[0].distance.value*document.getElementById("demo").value)/1000)*0.05 +" readonly></td> <td>Total :<input type='text' name='total' style='width :35%' value ="+ ((result.routes[0].legs[0].distance.value*document.getElementById("demo").value)/1000 + ((result.routes[0].legs[0].distance.value*document.getElementById("demo").value)/1000)*0.05).toFixed(2)  +" readonly></td> <td><button class='btn btn-outline-primary ms-3' style='margin-top: 40px; margin-bottom: 40px;' type='submit'>Book Now</button></td> </tr></tbody></table> </div> " );
            $("#output2").html("<p>"+ result.routes[0].legs[0].distance.text +" <p>")
            document.getElementById("output1").style.display = "block";
           
          

            //display route
            directionsDisplay.setDirections(result);
        } else {
            //delete route from map
            directionsDisplay.setDirections({ routes: [] });
            //center map in London
            map.setCenter(myLatLng);

            //Show error message           
           
            alert("Can't find road! Please try again!");
            clearRoute();
        }
    });

}

// Clear results

function clearRoute(){
    document.getElementById("output1").style.display = "none";
    
    document.getElementById("location-1").value = "";
    document.getElementById("location-2").value = "";
    directionsDisplay.setDirections({ routes: [] });
    
}

// Create autocomplete objects for all inputs

var options = {
    types: ['(cities)']
}


var input1 = document.getElementById("location-1");
var autocomplete1 = new google.maps.places.Autocomplete(input1, options);

var input2 = document.getElementById("location-2");
var autocomplete2 = new google.maps.places.Autocomplete(input2, options);


