my ($n, $l, $r) = split / /, <>;

my @result = ();

for my $i (1..$l-1) {
    push @result, $i;
}

for my $i ($l..$r) {
    push @result, ($r + $l) - $i;
}

for my $i ($r+1..$n) {
    push @result, $i;
}

print join ' ', @result;
print "\n";