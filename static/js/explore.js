
$('#explore-submit').on('click', () => {

    const formData = {
      city: $('#city-given').val(),
      zipcode: $('#zipcode-given').val(),
      term: $('#term-given').val(),
    };

  $.post('/users/trips/explore.json', formData, (res) => {
    let explore = [];
    const suggest = res.recommends;
    suggest.forEach(r => 
      explore.push(`Name: ${r.yep_name}, rating: ${r.yep_rating}, address: ${r.yep_address}`));
    explore.forEach(rec => {
      console.log(rec);

      $("#misc-recommend").append(`<ul>${rec}</ul>`);

      });  
        
          
          
      });
  // document.location.href = '/users/trips/explore';
});
// $.get('/users/trips/exlpore.json', (data) => {
//   const recommends = []
//   const response = JSON.parse(data);
//   console.log(response)
//   response.forEach(r => {
//     recommend = (`${r.yep_name} ${r.yep_rating} ${r.yep_address}`);
//     recommends.push(recommend)
//   });

//   recommends.forEach(rec => {
//     $('#misc-recommend').append(rec);
//   });
// });



