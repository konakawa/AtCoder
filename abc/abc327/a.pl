my $n = int <>;
my @s = split //, <>;

for my $i (0..$n-2) {
    if ($s[$i] eq 'a' && $s[$i+1] eq 'b') {
        print "Yes\n";
        exit;
    } elsif ($s[$i] eq 'b' && $s[$i+1] eq 'a') {
        print "Yes\n";
        exit;
    }
}

print "No\n";