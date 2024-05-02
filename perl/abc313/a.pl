#!usr/bin/env perl
use strict;

my $N = int <STDIN>;
my $Ps = <STDIN>;
chomp($Ps);
my @P = split(' ', $Ps);

my $p1 = $P[0];
splice(@P, 0, 1);

my $diff = 0;

for my $P (@P) {
    if ($P - $p1 >= $diff) {
        $diff = $P - $p1 + 1;
    }
}

print "$diff\n";
