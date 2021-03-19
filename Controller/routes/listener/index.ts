import "reflect-metadata";
import { connect } from "../connection";
import { Listener } from "../../src/entity/Listener";

import express = require('express');
import bodyParser = require('body-parser');
const listener = express.Router();

listener.get('/get', (req, res, next) => {
	connect.then(async connection => {
        const repository = connection.getRepository(Listener);
        const listeners = await repository.find();
        res.send(listeners);
    })
});

listener.post('/add', (req, res, next) => {
    try {
        connect.then(async connection => {
            const repository = connection.getRepository(Listener);
            let newListener = new Listener();
            newListener.LiveURL = req.body.LiveURL;
            newListener.Name = req.body.Name;
            newListener.Platform = req.body.Platform;
            newListener.Status = req.body.Status;
            await repository.save(newListener);
            res.send({
                status: true,
                msg: 'OK'
            });
        });
    }
    catch(err) {
        res.send({
            status: false,
            msg: err
        });
    }
});

listener.post('/switch', (req, res, next) => {
    try {
        connect.then(async connection => {
            const repository = connection.getRepository(Listener);
            let listener = await repository.findOne({
                where: {
                    LiveURL: req.body.LiveURL
                }
            });
            listener.Status = req.body.Status;
            repository.save(listener);
            res.send({
                status: true,
                msg: 'OK'
            })
        });
    }
    catch(err) {
        res.send({
            status: false,
            msg: err
        })
    }
});

listener.post('/update', (req, res, next) => {
    try {
        connect.then(async connection => {
            const repository = connection.getRepository(Listener);
            let listener = await repository.findOne({ 
                where: {
                    LiveURL: req.body.LiveURL
                }
            });
            listener.Name = req.body.Name;
            repository.save(listener);
            res.send({
                status: true,
                msg: 'OK'
            });
        });
    }
    catch(err) {
        res.send({
            status: false,
            msg: err
        });
    }
});

listener.post('/delete', (req, res, next) => {
    try{
        connect.then(async connection => {
            const repository = connection.getRepository(Listener);
            let removeListener = await repository.findOne({
                where: {
                    LiveURL: req.body.LiveURL
                }
            });
            await repository.remove(removeListener);
            res.send({
                status: true,
                msg: 'OK'
            });
        });
    }
    catch(err) {
        res.send({
            status: false,
            msg: err
        });
    }
})

export { listener };