import "reflect-metadata";
import { connect } from "../connection";
import { VideoInfo } from "../../src/entity/VideoInfo";

import express = require('express');
import bodyParser = require('body-parser');
const videoFile = express.Router();

videoFile.get('/get', (req, res, next) => {
    connect.then(async connection => {
        const repository = connection.getRepository(VideoInfo);
        const files = await repository.find();
        res.send(files);
    })
});

export { videoFile };