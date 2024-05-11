my $n = int <>;
my @as = map { int $_ } split ' ', <>;

my @sorted = sort { $a <=> $b } @as;

my $left = 0;
my $right = $n-1;
my $count = 0;
my $mod = 10 ** 8;

# 和がmod以上になる組み合わせの数
while ($left < $right) {
    if ($sorted[$left] + $sorted[$right] >= $mod) {
        $count += $right - $left;
        $right--;
    } else {
        $left++;
    }
}

my $total = 0;
for my $i (0..$n-1) {
    $total += $as[$i] * ($n - 1);
};

my $ans = $total - $count * $mod;
print $ans . "\n"; 
