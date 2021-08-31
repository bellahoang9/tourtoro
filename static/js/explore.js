
$('#explore-submit').on('click', () => {
  document.location.href = '/users/trips/explore';
    const formData = {
      city: $('#city-given').val(),
      zipcode: $('#zipcode-given').val(),
      term: $('#term-given').val(),
    };
// });
    $.post('/users/trips/explore.json', formData, (res) => {
          explore = []
          const suggest = res.recommends;
          const recommend = ''
          console.log('checking')
          consolelog(suggest)
          suggest.forEach(r => {
            recommend += (`${r.yep_name} ${r.yep_rating} ${r.yep_address}`);
            explore.push(recommend)
        });
          // explore.forEach(rec => {
          // });  
          console.log(explore)
          $('#misc-recommend').append(explore);
        });
    
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



