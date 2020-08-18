#!/bin/bash
MYPAHT=$(readlink -f .)
ALEMBIC_PATH="${MYPAHT}/alembic"
export PYTHONPATH=$PYTHONPATH:$MYPAHT:$ALEMBIC_PATH


if [ -z $1 ]
then
    echo 'please input name migrations!'
else
    alembic revision --autogenerate -m $1
fi
