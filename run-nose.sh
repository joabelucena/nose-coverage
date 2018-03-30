#!/usr/bin/bash

export PYTHONPATH=$(pwd)
export DIRECTORY=report

export PROGRAM=$PYTHONPATH/test/TestShape.py

if [  -d "$DIRECTORY" ]; then
   rm -rf "$DIRECTORY" 
fi

mkdir "$DIRECTORY"
cd "$DIRECTORY"

# Run nose

nosetests ../test/ --with-xunit --with-coverage --cover-xml --xunit-testsuite-name=test -q
#nosetests ../test/ --with-xunit --with-coverage --cover-xml --cover-html  --xunit-testsuite-name=test 
# Run Sonnar Qube

