my ($n, $m) = split / /, <>;

my $num_bits_n = length(sprintf("%b", $n));
my $num_bits_m = length(sprintf("%b", $m));

my $count = 0;

# GPT-4oが吐いたサブルーチン
sub count_bits {
    my ($n) = @_;
    return [] if $n < 0;

    my @bit_counts;
    my $k = 0;
    
    while ((1 << $k) <= $n) {
        my $full_pattern_count = int(($n + 1) / (1 << ($k + 1)));
        my $remainder = ($n + 1) % (1 << ($k + 1));
        my $bit_count = $full_pattern_count * (1 << $k) + (($remainder > (1 << $k)) ? ($remainder - (1 << $k)) : 0);
        push @bit_counts, $bit_count;
        $k++;
    }
    
    return \@bit_counts;
}

my @bit_occurrences_n = @{count_bits($n)};

for my $i (0 .. $num_bits_m - 1) {
    my $bit = ($m >> $i) & 1;
    if ($bit) {
        $count += $bit_occurrences_n[$i];
    }
    $count %= 998244353;
}

print $count;
print "\n";
