if [ "$(docker ps -q --filter name='mysql')" ]; then
    docker kill mysql
fi
docker run --rm -d --name mysql --network my-network -v 'D:\Docker-ScratchPad\Projects\PROJECT_1\my-flask-app\app\storage':/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=mydb -p 4000:3306 mysql:latest
if [ "$(docker ps -q --filter name='flask-app')" ]; then
    docker kill flask-app
fi
docker run --rm -d --name flask-app -v 'D:\Docker-ScratchPad\Projects\PROJECT_1\my-flask-app\app\':/app/ --network my-network --env-file ../.env -p 5000:5000 flask-app:latest
