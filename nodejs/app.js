const express = require('express');
const bodyParser = require('body-parser');
const app = express();

var dir = __dirname + '/sounds';
app.use(express.static(dir));

app.get('/sound', (req, res) => {

    var mode = req.query.mode.toString();
    var latitude = req.query.latitude.toString();
    var longitude = req.query.longitude.toString();

    console.log("[I] GET request on: /sound");
    console.log("[I] running python module\n");

    const { spawn } = require('child_process')
    const pyProg = spawn('python', ['./../python_module/main.py', mode, latitude, longitude]);

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

        return res.status(201).json(links);
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
