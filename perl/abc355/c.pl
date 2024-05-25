my ($n, $t) = split " ", <>;
my @as = split " ", <>;

my @verticals = (0) x $n;
my @horizontals = (0) x $n;
my $cross1 = 0;
my $cross2 = 0;

for my $k (0..$t-1) {
    my $a = $as[$k];
    my $i = int ($a / $n) + 1;
    my $j = $a % $n;
    if ($j == 0) {
        $j = $n;
        $i--;
    }

    $verticals[$j-1]++;
    $horizontals[$i-1]++;
    if ($i == $j) {
        $cross1++;
    }
    if ($i + $j == $n + 1) {
        $cross2++;
    }

    if ($verticals[$j-1] == $n || $horizontals[$i-1] == $n || $cross1 == $n || $cross2 == $n) {
        print $k + 1 . "\n";
        exit;
    }
}

print "-1\n";