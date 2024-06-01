#!usr/bin/env perl
use strict;

my $S = <STDIN>;
chomp($S);

my @targets = (
    'ACE',
    'BDF',
    'CEG',
    'DFA',
    'EGB',
    'FAC',
    'GBD'
);

for my $target (@targets) {
    if ($S eq $target) {
        print "Yes\n";
        exit;
    }
}

print "No\n";
