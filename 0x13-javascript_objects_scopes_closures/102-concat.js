#!/usr/bin/node

const args = process.argv;

const fs = require('fs');

// Reading file content

function readFile (filePath) {
  try {
    const data = fs.readFileSync(filePath, 'utf8');
    return data;
  } catch (err) {
    console.error(`Error occured while reading the file \n ${err}`);
  }
}

const file1Content = readFile(args[2]);
const file2Content = readFile(args[3]);

// function to write in a given file

function writeFile (filePath, content) {
  fs.appendFile(filePath, content, 'utf8', (err) => {
    if (err) {
      console.error(`Error occured writing: ${err}`);
    }
  });
}

const contentFile1 = file1Content;
const contentFile2 = file2Content;

writeFile(args[4], contentFile1);
writeFile(args[4], contentFile2);
