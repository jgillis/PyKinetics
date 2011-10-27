#/bin/bash

pushd ..
DIR=`pwd`
popd
echo "export PYTHONPATH=\$PYTHONPATH:$DIR" > bashrc
registerbashrc bashrc

