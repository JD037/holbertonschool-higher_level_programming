$(document).ready(function() {
    $('#toggle_header').click(function() {
        if ($('header').hasClass('red')) {
            $('header').removeClass('red').addClass('green');
        } else if ($('header').hasClass('green')) {
            $('header').removeClass('green').addClass('red');
        } else {
            // This block ensures that <header> has a class when the page first loads
            // and neither 'red' nor 'green' class is set yet.
            $('header').addClass('red');
        }
    });
});
