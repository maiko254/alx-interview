#!/usr/bin/node
const request = require('request');
const filmID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmID}/`;

function requestPromise (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

async function getCharacters () {
  try {
    const response = await requestPromise(url);
    const film = JSON.parse(response);

    const actorPromises = film.characters.map((characterUrl) => {
      return requestPromise(characterUrl).then((characterResponse) => {
        const character = JSON.parse(characterResponse);
        return character.name;
      });
    });

    const actors = await Promise.all(actorPromises);
    actors.forEach((actor) => console.log(actor));
  } catch (error) {
    console.log(error);
  }
}

getCharacters();
