#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./swMovieCharacters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a GET request to the Star Wars API to get movie information
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie information. Status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    const characterUrls = movieData.characters;

    // Fetch all character data
    const characters = [];
    let charactersFetched = 0;

    characterUrls.forEach(characterUrl => {
      request.get(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          characterData.id = characterUrl.split('/')[5];
          characters.push(characterData);

          // Check if all characters have been fetched
          charactersFetched++;
          if (charactersFetched === characterUrls.length) {
            // Sort characters by ID in ascending order
            characters.sort((a, b) => a.id - b.id);

            // Print character names in the sorted order
            characters.forEach(character => {
              console.log(character.name);
            });
          }
        } else {
          console.error('Error retrieving character information. URL:', characterUrl);
        }
      });
    });
  }
});
