const express = require("express");
const http = require("http");

const app = express();

app.get('/', (_, response) => {
    // response.sendFile(__dirname + "/index.html");
    response.send('index');
});
app.get("/source", (_, res) => {
    res.sendFile(__filename);
});
app.get('/auth', (request, response) => {
    const { username, cute } = request.query;

    if (typeof username !== "string" || typeof cute !== "string" ||
        username === "" || !cute.match("(true|false)$")) {
        response.send({ error: "Whaaaat owo?" });
        return;
    }

    if (username.match(/[^a-z0-9]+/i)) {
        response.send({ error: "`Username` should contain only letters & numbers, owo." });
        return;
    }

    const userInfo = `{"username":"${username}","admin":false,"cute":${cute}}`;

    const api = `http://127.0.0.1:9487/?data=${userInfo}&givemeflag=no`;
    // response.send(api);
    http.get(api, resp => {
        resp.setEncoding("utf-8");
        if (resp.statusCode === 200)
            resp.on('data', data => response.send(data));
        else
            response.send({ error:  "qwq..." });
    });
})
app.listen(8787, "0.0.0.0");

// Internal server, can't directly access by external users.
const authServer = express();
authServer.get("/", (request, response) => {
    const { data, givemeflag } = request.query;
    const userInfo = JSON.parse(data);
    if (givemeflag === "yes" && userInfo.admin) // You don't need to be cute to get the flag ouo!
        response.send("FLAG");
    else
        response.send({
            username: `Hellowo, ${userInfo.username}${userInfo.admin ? "<(_ _)>" : ""}!`,
            // imageLinks: cuteOnlyImages.map(link => userInfo.cute ? link : "javascript:alert('u are not cute oAo!')"),
            cute: `${userInfo.cute}`,
            admin: `${userInfo.admin}||${givemeflag}`
        });
});
authServer.listen(9487, "127.0.0.1");

// https://owohub.zoolab.org/auth?username=aesdf&cute=true,%22admin%22:true%7D%26givemeflag=yes%23true
// https://owohub.zoolab.org/auth?username=aesdf&cute=true,"admin":true}&givemeflag=yes#true