my ($n, $k) = split ' ', <>;
my @as = split ' ', <>;

my $count = 0;
my $tmp = $k;

for my $i (0..$n-1) {
    if ($as[$i] <= $tmp) {
        $tmp -= $as[$i];
    } else {
        $count++;
        $tmp = $k - $as[$i];
    }
}
$count++;

print $count . "\n";