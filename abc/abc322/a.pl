#!usr/bin/env perl
use strict;

my $n = int <>;
my $s = <>;
chomp($s);
my @cs = split //, $s;

for (my $i = 0; $i < @cs; $i++) {
    if ($cs[$i] eq 'A' && $cs[$i + 1] eq 'B' && $cs[$i + 2] eq 'C') {
        print $i + 1 . "\n";
        exit;
    }
}

print "-1\n";
