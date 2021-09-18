//  Get all itinerary, activity and note data from DB to render full itinerary.
$.get('/users/itinerary/api', (data) => {
  
  const response = JSON.parse(data);
  let activities = response.activities
  const trips = response.trips;
  const dates = response.dates;
  const friends = response.friends;

  //Fill in trips and intinerary id in HTML

  $('#trip-name').html(`${trips.trip_name}`);
  $('#trip-id').html(`${trips.trip_id}`);

   //  Sets up itinerary calender based on days of trip.
  let day = 1;
  dates.forEach(d => {
    const date = document.createElement('div');
    date.textContent = `Day ${day}: ${d}`;
    date.setAttribute('id', d);
    date.setAttribute('class','days');
    $('#travel-dates').append(date);
    day = day + 1;
  });
  // Sorts activities by time(if one is included) for ordered 
  // Placement on itinerary
  const untimedActivities = [];
  const timedActivities = [];

  //Separate activities by time and untime and convert to iso format
  activities.forEach(a => {
    if (a.activ_time != null) {
      if (a.activ_date != null) {
        a.iso = new Date(`${a.activ_date}T${a.activ_time}`);
      } else {
        a.iso = new Date(`1970-01-01T${a.activ_time}`)};
        timedActivities.push(a);

    } else {
        untimedActivities.push(a);
    };
  });
  
//Sorted activities from earliest
timedActivities.sort((a, b) => a.iso - b.iso);
// concat time and untime activities to one array
activities = timedActivities.concat(untimedActivities);
//Adds activities to the specific day or to bottom of list
activities.forEach(a => {
  // adds undated activity to misc. section of itinerary
  if (a.activ_date === null) {
    // const day = document.createElement('div');
    // day.setAttribute('class', 'activity-day');
    // day.textContent = a.activ_date;
    // $('#misc-activities').append(day);
    // const time = document.createElement('div');
    // time.setAttribute('class', 'activity-time');
    // time.textContent = a.time;
    // $('#misc-activities').append(time);


    const name = document.createElement('div');
    name.setAttribute('class', 'activity-name');
    name.textContent = a.activ_name;
    $('#misc-activities').append(name);
    const address = document.createElement('div');
    address.setAttribute('class', 'activity-address');
    address.textContent = a.address;
    $('#misc-activities').append(address);
    
  // adds dated activities to the itinerary
  } else {
    // if activity has a time, add time to itinerary
    if (a.activ_time !== null) {
      const time = document.createElement('div');
      time.setAttribute('class', 'activity-time');
      time.textContent = a.activ_time;
      $(`#${a.activ_date}`).append(time);
    };
      const name = document.createElement('div');
      name.setAttribute('class', 'activity-name');
      name.textContent = a.activ_name;
    $(`#${a.activ_date}`).append(name);
      const address = document.createElement('div');
      address.setAttribute('class', 'activity-address');
      address.textContent = a.address;
    $(`#${a.activ_date}`).append(address);
    // if activity has a note, add note to itinerary
    if (a.activ_note !== null) {
      const note = document.createElement('div');
      note.setAttribute('class', 'activity-note');
      note.textContent = a.activ_note;
      $(`#${a.activ_date}`).append(note);
    };
  };
  });
  });
  // Displays list of friends sharing this trip.
  // friends.forEach(f => {
  // const friend = document.createElement('span');
  // friend.textContent = `${f[0]}   `;
  // $('#travel-mates').append(friend);
  // });

  //  redirects to the activity search page.
  $('#add-activity-btn').on('click', () => {
    document.location.href = '/users/trips/activities';
  });

  //  Changes CSS for pretty printing
  window.onbeforeprint = function() {
    $('#trip-name').css('text-align', 'left');
    $('#col-two').hide();
  };
  window.onafterprint = function() {
    $('#trip-name').css('text-align', 'center');
    $('#col-two').show();
  };