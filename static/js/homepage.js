"use strict"

// submit new user form to the database and return to login page on success
$('#new-user-submit').on('click', () => {

    const formData = {
        email: $('#new-email').val(),
        password: $('#new-password').val(),
        fname: $('#new-fname').val(),
        lname: $('#new-lname').val()
        };

    // else if (formData.password.length === 0){
    //     alert('Invalid password!')
    // }
    // else if (formData.fname.length === 0){
    //     alert('Please enter your first name!')
    // }
    // else if (formData.lname.length === 0){
    //     alert('Please enter your last name!')
    // }

        $.post('/users/create-user.json', formData, (response) => {
        $('#new-user-modal').modal('toggle');
        alert(response)
        });

    
});


