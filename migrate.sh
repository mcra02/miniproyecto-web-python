#!/bin/bash

MYPAHT=$(readlink -f .)
ALEMBIC_PATH="${MYPAHT}/alembic"
export PYTHONPATH=$PYTHONPATH:$MYPAHT:$ALEMBIC_PATH

alembic upgrade head