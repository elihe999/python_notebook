#!/usr/bin/env zsh
#move it into virtualenv/bin
#NOW change the script for  anaconda3/bin

if [ -z "$CONDA_DEFAULT_ENV" ] ; then
    echo "YOU MUST activate your conda virtural env: source activate xxxx"
    exit 1
fi

ROOT_PYTHON="/usr/bin/python3"
#PYTHON=`python -c "import sys; print(sys.real_prefix)"`/bin/python3
PYTHON="/usr/bin/python"
export PYTHONHOME=$ENV
exec $PYTHON "$@"
