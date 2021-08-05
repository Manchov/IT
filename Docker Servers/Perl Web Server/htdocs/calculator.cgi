#!/usr/bin/perl
use strict;
use warnings;
use Scalar::Util qw(looks_like_number);

#use cgi;

print "Content-type: text/html\n\n";
print "<title>Calculator</title>\n";

$ENV{'REQUEST_METHOD'} =~ tr/a-z/A-Z/;

my $buffer;

if ($ENV{'REQUEST_METHOD'} eq "GET") {
   $buffer = $ENV{'QUERY_STRING'};
}

my @pairs = split(/&/, $buffer);

my %FORM;
foreach my $pair (@pairs) {
   my ($name, $value) = split(/=/, $pair);
   $value =~ tr/+/ /;
   $value =~ s/%(..)/pack("C", hex($1))/eg;
   $FORM{$name} = $value;
}

my $operand1  = $FORM{operand1};
my $operand2  = $FORM{operand2};
my $operation  = $FORM{operation};

if (looks_like_number($operand1) && looks_like_number($operand2)) {
	my $result;
	if ($operation eq "plus") { $result = $operand1 + $operand2; }
	elsif ($operation eq "minus") { $result = $operand1 - $operand2; }
	elsif ($operation eq "multiply-by") { $result = $operand1 * $operand2; }
	elsif ($operation eq "divide-by") {
		if ($operand2 == 0) {
			print "INVALID OPERАTION - parameters \"operand1\" and \"operand2\" are required and should be integer values, \"operation\" is required and the value should be one of: \"plus\", \"minus\", \"multiply-by\", \"divide-by\".";
			$result = "ERROR";
		} else {
			$result = $operand1 / $operand2;
		}
	}else{
		print "INVALID OPERАTION - parameters \"operand1\" and \"operand2\" are required and should be integer values, \"operation\" is required and the value should be one of: \"plus\", \"minus\", \"multiply-by\", \"divide-by\".";
		exit;
	}
	
print "$operand1 $operation $operand2 -> $result";

}else {
	print "INVALID OPERАTION - parameters \"operand1\" and \"operand2\" are required and should be integer values, \"operation\" is required and the value should be one of: \"plus\", \"minus\", \"multiply-by\", \"divide-by\".";
        }
exit;
