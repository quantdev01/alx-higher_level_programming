#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
	constructor(width, height, size)
	{
		this.size = size;
		super(width, height); 
		this.width = this.size;
		this.height = this.size;
	}
}

module.exports = Square;
