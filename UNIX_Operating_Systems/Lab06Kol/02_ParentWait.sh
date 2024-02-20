#!/bin/bash
dzisiaj=$(date +%Y-%m-%d)

if [ $# -eq 0 ]; then
  echo "Wywolujac program napisz: $0 <arg, arg, arg...>"
  exit 1
fi

even=()
odd=()
for (( i=$#; i>0; i-- )); do
  if [[ $((${!i}%2)) -eq 0 ]]; then
    even+=(${!i})
  else
    odd+=(${!i})
  fi
done

echo "${even[*]}"
echo "${odd[*]}"

bash scnd.sh ${even[*]} &
PIDS=$!
wait
resEven=$?
echo " $resEven"

bash scnd.sh ${odd[*]} &
PIDS=$!
wait
resOdd=$?

touch $dzisiaj
echo $* > $dzisiaj
echo $(($resEven+$resOdd)) >> $dzisiaj
exit 0