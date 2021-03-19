import "reflect-metadata";
import {createConnection} from "typeorm";
import {User} from "./entity/User";
import {Config} from './entity/Config';

createConnection().then(async connection => {

    console.log("Inserting a new user into the database...");
    const user = new User();
    user.username = 'admin';
    user.password = 'admin';
    const configs = {
        preferences: {
            savePath: '.',
            listenInterval: '2000',
            format: 'MP4'
        },
        proxy: {
            proxyOn: false,
            proxyHttp: 'http://127.0.0.1:10808',
            proxyUser: null,
            proxyPassword: null
        }
    }
    for (let configItem in configs) {
        for (let config in configs[configItem]) {
            let c = new Config();
            c.key = config;
            c.value = configs[configItem][config];
            await connection.manager.save(c);
        }
    }
    await connection.manager.save(user);

    console.log("Loading users from the database...");

}).catch(error => console.log(error));