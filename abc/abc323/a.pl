my @s = split //, <>;

for my $i (0..$#s) {
    unless ($i % 2 == 0) {
        unless ($s[$i] eq '0') {
            print "No\n";
            exit;
        }
    }
}

print "Yes\n";