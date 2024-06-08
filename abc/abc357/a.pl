my ($n, $m) = split ' ', <>;
my @hs = split ' ', <>;

my $count = 0;

for (0..$n-1) {
    my $h = $hs[$_];
    if ($h <= $m) {
        $count++;
        $m -= $h;
    }
    else {
        last;
    }
}

print $count;
print "\n";