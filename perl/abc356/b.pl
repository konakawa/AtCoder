my ($n, $m) = split / /, <>;
my @as = split / /, <>;

my @gained = (0) x $m;

sub vector_add {
    my ($a, $b) = @_;
    my @result = ();
    for my $i (0..$#{$a}) {
        push @result, $a->[$i] + $b->[$i];
    }
    return \@result;
}

for (1..$n) {
    my @xs = split / /, <>;
    @gained = @{vector_add(\@gained, \@xs)};
}

for (0..$m-1) {
    if ($as[$_] > $gained[$_]) {
        print "No\n";
        exit;
    }
}

print "Yes\n";