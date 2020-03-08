const express = require('express');
const bodyParser = require('body-parser');
const app = express();

var dir = __dirname + '/sounds';
app.use(express.static(dir));

let testData = [
    {"link": "adrenaline/Track-01.mp3", "mode": "0"},
    {"link": "adrenaline/Track-02.mp3", "mode": "0"}
];

app.get('/sound', (req, res) => {

    var mode = req.query.mode.toString();
    var latitude = req.query.latitude.toString();
    var longitude = req.query.longitude.toString();
    
    var datetime = new Date();

    console.log(datetime)
    console.log("[I] GET request on: /sound");
    console.log("[I] running python module\n");
    console.log("[I] Input: " + mode + ", " + latitude + ", " + longitude + "\n")

    // test
    //console.log('##### Sending data: #####')
    //console.log(testData);
    //console.log('#########################\n')
    //return res.json(testData);

    const { spawn } = require('child_process')
    const pyProg = spawn('python', ['-u', './../python_module/main.py', mode, latitude, longitude]);

    pyProg.stdout.on('data', function(data) {

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

        return res.json(links);
    });

    pyProg.stderr.on('data', (data) => {
        console.log(`error:${data}`);
    });

    pyProg.stderr.on('close', () => {
        console.log("[I] Closed");
    });
});

const { spawn } = require('child_process')
const pyOnCreate = spawn('python', ['./../python_module/onCreate.py']);
pyOnCreate.stdout.on('data', function(data) {
    console.log('\n[onCreate] Running onCreate.py before app starts...');
    console.log(data.toString());
    console.log('[onCreate] Done.\n');
});

app.listen(8080, () => console.log("[App] Application listening on port 8080!\n"));
