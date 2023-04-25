#!/usr/bin/node
// Prints the title of Star Wars movie
// where the episoe number matches a given integer

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const filmId = process.argv[2];

request(url + filmId, (error, response, body) => {
  if (error) throw error;
  console.log(response && JSON.parse(body).title);
});
