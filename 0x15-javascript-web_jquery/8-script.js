$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(response, textStatus){
    var films = response.results;
    for (var film of films) {
        var newItem = $('<li>').text(film.title);  
        $('ul#list_movies').append(newItem);
    }
});
