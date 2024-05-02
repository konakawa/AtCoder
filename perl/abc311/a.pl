#!usr/bin/env perl
use strict;

my $N = <STDIN>;
chomp($N);
my $S = <STDIN>;
chomp($S);

my $occur_a = 0;
my $occur_b = 0;
my $occur_c = 0;

my $count = 0;

my @chars = split(//, $S);
foreach my $char (@chars) {
    $count++;
    if ($char eq 'A') {
        $occur_a++;
    } elsif ($char eq 'B') {
        $occur_b++;
    } elsif ($char eq 'C') {
        $occur_c++;
    }
    if ($occur_a && $occur_b && $occur_c) {
        last;
    }
}

print $count;
print "\n";
 