#!/usr/bin/node

const myArgs = process.argv;

const ln = myArgs.length;

if (ln <= 3) { console.log(0); } else {
  function getBiggest (myarray) {
    let i = 2;

    while (i <= ln) {
      if (myarray[i] > myarray[i + 1]) {
        const temp = myArgs[i];
        myarray[i] = myarray[i + 1];
        myarray[i + 1] = temp;
      }
      i++;
    }
    return myarray[ln - 1];
  }

  /* getting the first big element */

  getBiggest(myArgs);

  /* deleting the current biggest element */

  myArgs[ln - 1] = 0;

  /* Calling the function to get the second biggest element and print it out */

  console.log(getBiggest(myArgs));
}
