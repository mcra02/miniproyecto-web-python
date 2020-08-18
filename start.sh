#!/bin/bash

export $(xargs < .env)

gunicorn -b 0.0.0.0:$PORT --reload main:app