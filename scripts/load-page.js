"use strict";

var system = require('system'),
    argv = require('minimist')(system.args.slice(1)),
    url = argv._[0],
    filename = argv._[1],
    width = argv.w || argv.width || 600,
    height = argv.h || argv.height || 600;

console.log('url:', url);
console.log('filename:', filename);
console.log('width:', width);
console.log('height:', height);

var page = require('webpage').create();
page.viewportSize = { width: width, height: height };

page.open(url, function(status) {
    if (status !== 'success') {
        console.log("Couldn't load address");
        phantom.exit(1);
    }

    window.setTimeout(function() {
        var height2 = page.evaluate(function() {
            return document.getElementById('app').offsetHeight;
        });

        var width2 = page.evaluate(function() {
            return document.getElementById('app').offsetWidth;
        });

        page.clipRect = { top: 0, left: 0, width: width2, height: height2+50 };

        page.render(filename);
        phantom.exit();
    }, 200);
});
