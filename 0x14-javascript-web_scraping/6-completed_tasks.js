#!/usr/bin/node

const request = require('request');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: ./completedTasksByUser.js <api_url>');
  process.exit(1);
}

const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve tasks information. Status code:', response.statusCode);
  } else {
    const tasks = JSON.parse(body);

    // Filter tasks with completed status
    const completedTasks = tasks.filter(task => task.completed);

    // Compute the number of completed tasks for each user
    const completedTasksByUser = completedTasks.reduce((result, task) => {
      const userId = task.userId.toString();
      result[userId] = (result[userId] || 0) + 1;
      return result;
    }, {});

    console.log(completedTasksByUser);
  }
});
