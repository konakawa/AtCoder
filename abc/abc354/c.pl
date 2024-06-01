my $n = int <>;
my @cards = ();
for (0..$n-1) {
    my ($a, $c) = split / /, <>;
    push @cards, [$a, $c, $_+1];
}

my @sorted_desc_cards = sort { $b->[0] <=> $a->[0] } @cards;

my @remains = ();

my $cheapest_cost = $sorted_desc_cards[0][1];
for my $card (@sorted_desc_cards) {
    my $a = $card->[0];
    my $c = $card->[1];
    if ($c == $cheapest_cost) {
        push @remains, $card;
    }
    if ($c < $cheapest_cost) {
        push @remains, $card;
        $cheapest_cost = $c;
    }
}

my @sorted_remains = sort { $a->[2] <=> $b->[2] } @remains;

print scalar @sorted_remains . "\n";

my $output = "";
for my $card (@sorted_remains) {
    $output .= $card->[2] . " ";
}

chop $output;
print $output . "\n";
