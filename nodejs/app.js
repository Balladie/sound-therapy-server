const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.get('/sound', (req, res) => {

    var mode = req.query.mode.toString();
    var latitude = req.query.latitude.toString();
    var longitude = req.query.longitude.toString();

    console.log("## GET request");
    console.log("## running python module");

    const { spawn } = require('child_process')
    const pyProg = spawn('python3', ['./../python_module/app.py', mode, latitude, longitude]);

    pyProg.stdout.on('data', function(data) {

        console.log(data.toString());
        var musicDates = data.toString().split(",");
        let titles = [];

        var i;
        for (i = 0; i < musicDates.length; ++i) {
            const newTitles = {
                title: musicDates[i]
            };
            titles.push(newTitles);
        }

        console.log(titles);
        return res.status(201).json(titles);
    });
});

app.listen(8080, () => console.log("Application listening on port 8080!"));
