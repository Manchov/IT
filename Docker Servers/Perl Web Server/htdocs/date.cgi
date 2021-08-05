#!/usr/bin/perl
use strict;
use warnings;

print "Content-type: text/html\n\n";
print "<title>Current Date</title>\n";

my $buffer;
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime;
$year += 1900;
$mon++;

$mon = "0$mon" if $mon < 10;
$mday = "0$mday" if $mday < 10;
$sec = "0$sec" if $sec < 10;
$min = "0$min" if $min < 10;
$hour = "0$hour" if $hour < 10;

if ($ENV{'REQUEST_METHOD'} eq "GET") {
   $buffer = $ENV{'QUERY_STRING'};
}

if (substr($buffer, 0, 4) eq "time"){
	print "$mday.$mon.$year \n";
	print "$hour:$min:$sec";
}elsif (not $buffer){	
	print "$mday.$mon.$year";
}else{
	print "INVALID OPERАTION - the service only functions either without any parameters or with the parameter \"time\", used with or without a value"
}

exit;