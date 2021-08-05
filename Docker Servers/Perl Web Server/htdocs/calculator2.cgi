#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(param header);


print "Content-type: text/html\n\n";
my $buffer;
$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;
my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime;
$year += 1900;
$mon++;
$mon = "0$mon" if $mon < 10;
$mday = "0$mday" if $mday < 10;
# print "$mday.$mon.$year";
#$getpassed = $ENV{'QUERY_STRING'};
#my $postdata = do { local $/; <STDIN> };
if ($ENV{'REQUEST_METHOD'} eq "GET") {
   $buffer = $ENV{'QUERY_STRING'};
   my $time = param('time');

}
if ($buffer eq "time" || $time){
	#print "$postdata"
	#print "$time";
	#print CGI::header();
	print "$mday.$mon.$year \n";
	print "$hour:$min:$sec";
}else{	
	print "$mday.$mon.$year";
}
exit;