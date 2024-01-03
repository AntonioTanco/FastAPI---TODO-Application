#!/usr/bin/env bash

while !</dev/tcp/db/5432; do sleep 1; done;

uvicorn --host 0.0.0.0 --port 8000 app.main:app


