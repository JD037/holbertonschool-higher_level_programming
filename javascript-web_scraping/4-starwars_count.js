#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    let count = 0;
    const films = JSON.parse(body).results;
    for (const film of films) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) {  // Checks if the character's URL ends with "/18/" which would mean it's Wedge Antilles.
          count++;
          break;  // Breaks out of the inner loop once Wedge Antilles is found in the current film.
        }
      }
    }
    console.log(count);
  }
});
