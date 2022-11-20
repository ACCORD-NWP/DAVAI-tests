#/usr/bin/bash
# BUILD EXECUTABLES

# superseding arguments
arg=""
if [ "$1" == "preexisting_pack=True" ] || [ "$1" == "preexisting_pack=False" ];then
    echo "Conf attribute '$1' superseded by commandline argument."
    arg=$1
elif [ "$1" != "" ];then
    echo "Commandline argument '$1' ignored."
fi

# prepare wait4build manager
python3 vortex/bin/mkjob.py -j profile=rd name=build_init task=build.wait4build_init
# build
export DAVAI_START_BUILD=`python3 -c "import time; print(time.time())"`
python3 vortex/bin/mkjob.py -j name=build task=build.gmkpack.build_from_gitref $arg
# wait & check for build
export MTOOLDIR=/scratch/mtool/$LOGNAME  # needed to find cached expertise output of build
python3 vortex/bin/mkjob.py -j profile=rd name=build task=build.wait4build
ok=$?

# return status of build
if [ "$ok" == "0" ];then
  echo "Build OK: continue"
  exit 0
else
  echo "Build KO ! $ok"
  echo "See log in $MTOOLDIR/<jobid>"
  exit 1
fi
