my ($x, $y) = split ' ', <>;

my $diff = $y - $x;

if (-3 <= $diff && $diff <= 2) {
    print "Yes\n";
} else {
    print "No\n";
}