my ($a, $b, $c, $d) = split / /, <>;

my $area = 0;

my @blocks = (
    [2, 1],
    [1, 2],
    [0, 1],
    [1, 0]
);

sub calc {
    my ($b, $d, $a) = @_;
    my $area = 0;
    my $tmp = int (($d - $b) / 2);
    if ($a % 4 == 0 || $a % 4 == 1) {
        $area += $tmp * 3;
    }
    else {
        $area += $tmp * 1;
    }

    if (($d - $b) % 2 == 1) {
        my $block = $blocks[$a % 4][$b % 2];
        $area += $blocks[$a % 4][$b % 2];
    }
    
    return $area;
}

my $area_calc_0 = calc($b, $d, $a);
my $area_calc_1 = calc($b, $d, $a + 1);
my $area_calc_2 = calc($b, $d, $a + 2);
my $area_calc_3 = calc($b, $d, $a + 3);

my $repeat = int (($c - $a) / 4);
$area += $area_calc_0 + $area_calc_1 + $area_calc_2 + $area_calc_3;
$area *= $repeat;

if (($c - $a) % 4 == 1) {
    $area += $area_calc_0;
}
elsif (($c - $a) % 4 == 2) {
    $area += $area_calc_0 + $area_calc_1;
}
elsif (($c - $a) % 4 == 3) {
    $area += $area_calc_0 + $area_calc_1 + $area_calc_2;
}

print $area . "\n";
