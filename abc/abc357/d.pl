my $n = <>;
my $l = (length $n) - 1;
$n = int $n;

my $mod = 998244353;
my $r = 10 ** $l;
my $r_mod = $r % $mod;

my $r_pow_n_mod = mod_pow($r_mod, $n, $mod);

my $sum = (($r_pow_n_mod - 1) * mod_inv($r_mod - 1, $mod)) % $mod;

my $result = ($n * $sum) % $mod;

print $result;
print "\n";

sub mod_pow {
    my ($base, $exp, $mod) = @_;
    my $result = 1;
    while ($exp > 0) {
        if ($exp % 2 == 1) {
            $result = ($result * $base) % $mod;
        }
        $base = ($base * $base) % $mod;
        $exp = int $exp / 2;
    }
    return $result;
}

sub mod_inv {
    my ($a, $m) = @_;
    return mod_pow($a, $m - 2, $m);
}
