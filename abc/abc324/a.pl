my $n = int <>;
my @as = split ' ', <>;

my $a = $as[0];

for my $i (1..$#as) {
    unless ($a == $as[$i]) {
        print "No\n";
        exit;
    }
}

print "Yes\n";
