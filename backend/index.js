import express from "express";

async function startServer() {
    const app = express();
    app.use(express.static('public')); //Serves resources from public folder
    var router = express.Router();
    app.use('/', router);
    router.get('/', (req, res) => {
        console.log('this is root');
        res.send("this is root"); //direct to homepage
    })
    router.get('/api', (req, res) => {
        console.log('this is api-prefix');
        res.send("this is api-prefix"); //direct to homepage
    })

    app.listen(5001, () => {
        console.log(`
            ################################################
            🛡️  HTTP server listening on port: ${5001} 🛡️
            ################################################
        `);
    })
        .on("error", (err) => {
            console.log(err);
            process.exit(1);
        });

}

startServer();