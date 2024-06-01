my ($n, $m) = split " ", <>;
my @as = split " ", <>;
my @bs = split " ", <>;

my @c = sort { $a <=> $b } (@as, @bs);

my %is_in_a = map { $_ => 1 } @as;
my $previous_was_in_a = 0;
my $found_consecutive = 0;

foreach my $element (@c) {
    if ($is_in_a{$element}) {
        if ($previous_was_in_a) {
            $found_consecutive = 1;
            last;
        }
        $previous_was_in_a = 1;
    } else {
        $previous_was_in_a = 0;
    }
}

if ($found_consecutive) {
    print "Yes\n";
} else {
    print "No\n";
}
