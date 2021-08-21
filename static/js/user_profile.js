"use strict"

// Gets user and itinerary data to render profile page
$.get('/users/profile/api', (data) => {
  $('#user-name').text(`${data.fname} ${data.lname}`);
  $('#user-email').text(data.email);
  const trips = data.trips;
  // show "no trips" message
  if (trips.length !== 0) {
    $('#no-itinerary').hide();
  };
  // render list of trips
  trips.forEach(i => {
    $('#user-itineraries').append(`<li><a href="/users/trips/${i.trip_id}">${i.trip_name}</a></li>`);
  });
});

// submits new trip information to be added to DB and adds to html.
$('#new-trip-submit').on('click', () => {
  const formData = {
    trip_name: $('#city-input').val(),
    start_date: $('#depart-date').val(),
    end_date: $('#return-date').val()
  };
  $.post('/users/trips/new-trip.json', formData, (response) => {
    $('#user-itineraries').append(`<li><a href="/users/trips/${response['itinerary_id']}">${response['trip_name']}</a></li>`);
    $('#new-trip-modal').modal('toggle');
    $('#no-itinerary').hide();
  });
});

$('#existing-trip-id').on('keypress', function(e) {
  return e.which !== 13;
});

// Creates a UserItinerary link in DB and adds itinerary to html.
$('#existing-submit').on('click', () => {
  $.post('/users/trips/add-trip.json', {'id': $('#existing-trip-id').val()}, (response) => {
    $('#user-itineraries').append(`<li><a href="/users/trips/${response['itinerary_id']}">${response['trip_name']}</a></li>`);
    document.getElementById("existing-trip-form").reset();
    $('#existing-trip-modal').modal('toggle');
    $('#no-itinerary').hide();
  });
});

