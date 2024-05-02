#!usr/bin/env perl
use strict;

my ($a, $b) = split(' ', <STDIN>);
print $a ** $b + $b ** $a;
print "\n";