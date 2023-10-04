$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(character, textStatus){
    $('div#character').text(character.name);
});
