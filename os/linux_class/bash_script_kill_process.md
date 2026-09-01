If you still have the problem, we came up with an alternative solution:
– prepare a bash script that will kill the process every 20 seconds
– run the bash script in the background
Bash script

# /root/scripts/ctKillProc.sh
#!/bin/sh
# do what you need to here
while true; do
processId=$(ps -ef | grep ‘kdevtmpfsi’ | grep -v ‘grep’ | awk ‘{ printf $2 }’)
echo $processId
kill -9 $processId
echo “[“`date +%Y%m%d%H%M`”] kdevtmpfsi killed.”
sleep 20
done
exit 1
Run the script in the background

nohup sh /root/scripts/ctKillProc.sh &

Now, the script will be executing in the background solving your Kinsing malware problem even if you close shell connection,.
Script logs can be found in the nohup.out file.