import "reflect-metadata";
import { connect } from "../connection";
import { VideoInfo } from "../../src/entity/VideoInfo";

import express = require('express');
import bodyParser = require('body-parser');
const videoFile = express.Router();

const axios = require('axios');
const qs = require('qs');

videoFile.get('/get', (req, res, next) => {
    try{
        axios.get('http://localhost:8000/VideoInfo/get').then(r => {
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

videoFile.post('/delete', (req, res, next) => {
    try {
        axios.post('http://localhost:8000/VideoInfo/delete',
            qs.stringify({
                FileName: req.body.FileName
            })
        ).then(r => {
            res.send(r.data);
        })
    }
    catch(err) {
        res.send({
            status: false,
            msg: err
        })
    }
});

videoFile.post('/recode', (req, res, next) => {
    try {
        axios.post(
            'http://localhost:8000/VideoInfo/recode', 
            qs.stringify({
                FileName: req.body.FileName,
                format: req.body.format,
                title: req.body.title,
                LiveURL: req.body.LiveURL
            })
        ).then(r => {
            res.send(r.data);
        })
    }
    catch(err) {
        res.send({
            status: false,
            msg: err
        })
    }
});

export { videoFile };