#!usr/bin/env perl
use strict;

my $s = <>;
$s =~ s/[aeiou]//g;
print $s;
