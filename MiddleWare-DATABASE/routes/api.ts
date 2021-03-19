import "reflect-metadata";
import { listener } from "./listener";
import { videoFile } from "./file";
import { settings } from "./settings";

import express = require('express');
import bodyParser = require('body-parser');
const api = express.Router();

api.use("/listener", listener);
api.use("/file", videoFile);
api.use("/setting", settings);

/*
import { Guid } from 'guid-typescript';

const connect = createConnection();

router.get('/loginVerification', (req, res, next) => {
    connect.then(async connection => {
        const repository = connection.getRepository(User);
        const user = await repository.findOne({
            username: req.query.username.toString()
        });
        if (req.query.password) {
            if (user.password !== req.query.password) {
                res.send('username/password error');
            }
            else {
                user.UUID = Guid.create().toString();
                repository.save(user);
                res.send(user.UUID);
            }
        }
        else res.send(user.UUID);
        return;
    })
    .catch(error => {
        console.error(error);
    })
})

router.get('/listenerInfo', (req, res, next) => {
    connect.then(async connection => {
        const repository = connection.getRepository(Listener);
        const listeners = await repository.find();
        res.send(listeners);
    })
})

router.get('/listener', (req, res, next) => {
    let control:string = req.query.control.toString();
    console.log(req.query);

    connect.then(async connection => {
        const repository = connection.getRepository(Listener);

        switch (control) {
            case 'add': {
                let newListener = new Listener();
                newListener.LiveURL = req.query.LiveURL.toString();
                newListener.Name = req.query.Name.toString();
                newListener.Platform = req.query.Platform.toString();
                newListener.Status = 0;
                await repository.save(newListener);
            }; break;
        }
        res.json({
            status: true,
            msg: 'OK'
        })
    }).catch(error => {
        res.json({
            status: false,
            msg: error
        })
    })
})
*/

export { api }