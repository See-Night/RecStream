import "reflect-metadata";
import { connect } from "../connection";
import { Config } from "../../src/entity/Config";

import express = require('express');

const settings = express.Router();

settings.use(express.urlencoded({ extended: false }));
settings.use(express.json());

settings.get('/get', (req, res, next) => {
    connect.then(async connection => {
        const repository = connection.getRepository(Config);

        const configs = await repository.find();
        res.send(configs);
    });
});

settings.post('/update', (req, res, next) => {
    try {
        connect.then(async connection => {
            const repository = connection.getRepository(Config);
            for (let config in req.body) {
                let newConfig = await repository.findOne({ where: { key: config } });
                newConfig.value = req.body[config] === '' ? null : req.body[config];
                await repository.save(newConfig);
            }
            res.send({
                status: true,
                msg: 'OK'
            })
        });
    }
    catch (err) {
        res.send({
            status: false,
            msg: err
        })
    }
})

export { settings };