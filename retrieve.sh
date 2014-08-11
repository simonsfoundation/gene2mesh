idfile=$1
out=$2

mkdir -p $out

IFS=$'\n'
for l in `cat $idfile`
do 
    mesh=`echo $l | cut -f1`
    meshid=`echo $l | cut -f2`
    xml=`echo ${meshid}.xml`
    if [ ! -f $out/$xml ]
    then
	    wget -O $out/$xml http://gene2mesh.ncibi.org/fetch?mesh="$mesh"\&taxid=9606
	    sleep 1s
    fi
done
unset IFS
