my $n = int <>;
my @hs = split ' ', <>;

my $h1 = $hs[0];

for my $i (1..$n-1) {
    if ($hs[$i] > $h1) {
        print $i + 1 . "\n";
        exit;
    }
}

print -1 . "\n";