const http = require('http');

const app = http.createServer((req, res) => {
    res.setHeader('Content-Type', 'text/plain');
    res.write('Hello Holberton School!');
    res.end();
});

app.listen(1245, () => {
    console.log('Server is running on port 1245');
});

module.exports = app;