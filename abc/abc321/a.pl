#!usr/bin/env perl
use strict;

my $n = int <>;

my $tmp = -1;

while ($n) {
    if ($n % 10 > $tmp) {
        $tmp = $n % 10;
        $n = int($n / 10);
    } else {
        print "No\n";
        exit;
    }
}

print "Yes\n";