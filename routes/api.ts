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

export { api }