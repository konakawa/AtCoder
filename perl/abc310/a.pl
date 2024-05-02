#!/usr/bin/env perl
use strict;

my ($n, $p, $q) = glob <>;
my $line = <>;
chomp $line;
my @ds = split ' ', $line;

my $diff = $p - $q;

for my $d (@ds) {
    if ($diff > $d) {
        $diff = $d;
    }
}

print $q + $diff, "\n";