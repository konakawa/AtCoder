my ($a, $b) = split " ", <>;

my $result;

if ($a == $b) {
    $result = -1;
}
else {
    $result = 6 - ($a + $b);
}

print "$result\n";