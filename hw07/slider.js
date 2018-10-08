#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('blynk-library');
const b = require('bonescript');
const util = require('util');

const LED1 = 'P9_14';
b.pinMode(LED1, b.OUTPUT);


const AUTH = 'f04dac5bf0cf4df3af0c549ace851718';


var blynk = new Blynk.Blynk(AUTH);


var v10 = new blynk.VirtualPin(10);


v10.on('write', function(param) {

    console.log('V0:', param[0]);

    b.analogWrite(LED1, param[0]/1023);

});
