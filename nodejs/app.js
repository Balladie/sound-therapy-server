const express = require('express');
const bodyParser = require('body-parser');
const app = express();

var dir = __dirname + '/sounds';
app.use(express.static(dir));

app.get('/sound', (req, res) => {

    var mode = req.query.mode.toString();
    var latitude = req.query.latitude.toString();
    var longitude = req.query.longitude.toString();

    console.log("## GET request on: /sound");
    console.log("## running python module\n");

    const { spawn } = require('child_process')
    const pyProg = spawn('python', ['./../python_module/main.py', mode, latitude, longitude]);

    pyProg.stdout.on('data', function(data) {

        //console.log(data.toString() + '\n');
        var musicDatas = data.toString().split(",");
        let links = [];

        var i;
        for (i = 0; i < musicDatas.length; ++i) {
            const newLink = {
                link: musicDatas[i],
                mode: mode
            };
            links.push(newLink);
        }

        console.log('##### Sending data: #####')
        console.log(links);
        console.log('#########################\n')

        return res.status(201).json(links);
    });
});

app.listen(8080, () => console.log("Application listening on port 8080!\n"));
