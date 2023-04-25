#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) console.error(error);
  if (response && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const output = {};

    for (const todo of todos) {
      if (todo.completed === true) {
        if (output[todo.userId] === undefined) {
          output[todo.userId] = 1;
        } else {
          output[todo.userId]++;
        }
      }
    }
    console.log(output);
  }
});
