#!usr/bin/env perl
use strict;

my ($n, $m, $p) = split(' ', <STDIN>);
my $diff = $n - $m;
print ($diff >= 0 ? int($diff / $p) + 1 : 0);
print "\n";