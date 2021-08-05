FROM docker.io/library/perl:latest as perlstage
FROM httpd:2.4
run apt-get update
run apt-get install -y build-essential

COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf

COPY --from=perlstage /usr/local/bin/ /usr/local/bin/
COPY --from=perlstage /usr/local/lib/ /usr/local/lib/
run cpanm CGI