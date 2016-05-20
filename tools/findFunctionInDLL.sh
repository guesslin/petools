#!/bin/bash

if [ $# -ne 1 ]
then
	printf "\n\tUsage: $0 functionname\n\n"
	exit
fi

functionname=$1
searchDir="/cygdrive/c/WINDOWS/system32"

arwin_exe="`pwd`/arwin.exe"
cd $searchDir

ls -1d *.dll | grep -v gui | while read dll
do
	printf "\r                                                       ";
	printf "\r$dll";
	count=0
	count=`$arwin_exe $dll $functionname | grep -c  "is located at"`
	if [ $count -ne 0 ]
	then
		printf "\n";
		$arwin_exe $dll $functionname | grep "is located at"
		printf "\n";
	fi
done
printf "\r                                                       ";
