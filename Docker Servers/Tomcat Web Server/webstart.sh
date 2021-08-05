docker run --name zad2 --privileged --mount type=bind,source="$(pwd)"/webapps,target=/usr/local/tomcat/webapps -p 8080:8080 -d tomcat:9.0 
