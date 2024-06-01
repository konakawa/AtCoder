my ($n, $x) = split / /, <>;
my @s = split / /, <>;

my $sum = 0;

for my $i (0..$n-1) {
    if ($s[$i] <= $x) {
        $sum += $s[$i];
    }
}

print $sum . "\n";