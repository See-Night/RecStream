import "reflect-metadata";
import { Listener } from "../../src/entity/Listener";

import express = require('express');
import bodyParser = require('body-parser');

const axios = require('axios');
const qs = require('qs');

const listener = express.Router();

listener.get('/get', (req, res, next) => {
    try{
        axios.get('http://localhost:8000/Listener/get').then(r => {
            res.send(r.data);
        });
    }
    catch(err) {
        res.send({
            status: false,
            msg: err
        });
    }
});

listener.post('/add', (req, res, next) => {
    try {
        axios.post(
            'http://localhost:8000/Listener/add', 
            qs.stringify({
                LiveURL: req.body.LiveURL,
                Name: req.body.Name,
                Platform: req.body.Platform,
                Status: req.body.Status ? 1 : 0
            })
        ).then(r => {
            res.send(r.data);
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
        let url = req.body.Status ? 'http://localhost:8000/Listener/start': 'http://localhost:8000/Listener/stop';
        axios.post(url, qs.stringify({
            LiveURL: req.body.LiveURL
        })).then(r => {
            res.send(r.data);
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
        /*connect.then(async connection => {
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
        });*/
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
        axios.post(
            'http://localhost:8000/Listener/delete',
            qs.stringify({
                LiveURL: req.body.LiveURL
            })
        ).then(r => {
            res.send(r.data);
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