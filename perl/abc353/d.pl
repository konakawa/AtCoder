# ! Wrong answer
# ModIntを使えばいいのかな？

my $n = int <>;
my @as = map { int $_ } split ' ', <>;

my @digits = map { 0 } 0..10;

for my $i (0..$n-1) {
    $digits[length $as[$i]]++;
}

my $sum = 0;
my $mod = 998244353;

for my $i (0..$n-1) {
    my $digit = length $as[$i];
    $digits[$digit]--;

    for my $j (1..10) {
        $sum += (10 ** $j) * $as[$i] * $digits[$j];
    }

    $sum += $as[$i] * $i;
    $sum %= $mod;
}

print $sum . "\n";