
$('#explore-submit').on('click', (evt) => {
    // evt.preventDefault();
    default_display_state();
    const formData = {
      city: $('#city-given').val(),
      zipcode: $('#zipcode-given').val(),
      term: $('#term-given').val(),
    };
  if (formData.city.length === 0){
    alert('Please enter city for the suggestion!')
  }
  else {
  $.post('/users/trips/explore.json', formData, (res) => {
    let explore = [];
    const recommends = res.recommends;

    recommends.forEach(r => 
      explore.push([`Name: ${r.yep_name}, rating: ${r.yep_rating}⭐, address: ${r.yep_address} `, r.yep_img ]));
      
    explore.forEach(rec => {
      $("#misc-recommend").append(`<ul>${rec[0]}</ul> <img src="${rec[1]}">`);
      


      });  
        
          
          
      });
    }
    $('#explore-modal').css("display", "none");
    $('body').removeClass("modal-open");
    $('.modal-backdrop').css("display", "none");

  });
  

function default_display_state() {
  $('#misc-recommend').html('');

};


