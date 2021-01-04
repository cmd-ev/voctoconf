#!/bin/sh
set -e

echo "#!/bin/sh" > /tmp/update-room-stats.sh
printenv | sed 's/^\(.*\)$/export \1/g' >> /tmp/update-room-stats.sh
echo "cd /app &&  /usr/local/bin/python manage.py update-room-stats" >> /tmp/update-room-stats.sh
chmod +x /tmp/update-room-stats.sh

echo 'Starting cron'
/usr/sbin/crond -f
