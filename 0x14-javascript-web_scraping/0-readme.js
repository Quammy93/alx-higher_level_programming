#!/usr/bin/node
const fs = require('fs');

//const filePath = process.argv[2];

fs.readFile(process.argv[2], 'utf-8', function(error, content) {
    console.error(`An error occurred while reading the file: ${error}`);
    console.log(content);
  }
);

