#!usr/bin/env perl
use strict;

my ($n, $h, $x) = split(' ', <STDIN>);
my @ps = split(' ', <STDIN>);

my $diff = $x - $h;

for (my $i = 0; $i < @ps; $i++) {
    if ($ps[$i] >= $diff) {
        print $i + 1;
        print "\n";
        exit;
    }
}