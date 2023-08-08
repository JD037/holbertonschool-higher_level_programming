$(document).ready(function() {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data, status) {
        if (status === 'success') {
            const movies = data.results;
            for (let movie of movies) {
                $('#list_movies').append('<li>' + movie.title + '</li>');
            }
        }
    });
});
