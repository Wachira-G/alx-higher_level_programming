#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2]; // Get the API URL from the cmd line args

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);

    // Create an object to store the count of completed tasks for each user
    const completedTasksByUser = {};

    // Iterate through the tasks and count completed tasks
    tasks.forEach((task) => {
      if (task.completed) {
        const userId = task.userId.toString();
        if (completedTasksByUser[userId]) {
          completedTasksByUser[userId]++;
        } else {
          completedTasksByUser[userId] = 1;
        }
      }
    });

    // Print the completed tasks by user
    console.log(completedTasksByUser);
  }
});
