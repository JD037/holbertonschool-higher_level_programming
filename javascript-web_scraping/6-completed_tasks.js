#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    for (const task of todos) {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId] += 1;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    }
    console.log(completedTasks);
  }
});
