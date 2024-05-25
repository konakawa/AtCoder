my $n = int <>;
my @start_events;
my @end_events;

for my $i (0..$n-1) {
    my ($l, $r) = split " ", <>;
    push @start_events, $l;
    push @end_events, $r;
}

my @sorted_start_events = sort { $a <=> $b } @start_events;
my @sorted_end_events = sort { $a <=> $b } @end_events;

my @sorted_start_events_with_type = map { [$_, 1] } @sorted_start_events;
my @sorted_end_events_with_type = map { [$_, -1] } @sorted_end_events;

my $i = 0;
my $j = 0;
my @events;

while ($i < $n || $j < $n) {
    if ($i == $n) {
        push @events, $sorted_end_events_with_type[$j];
        $j++;
    } elsif ($j == $n) {
        push @events, $sorted_start_events_with_type[$i];
        $i++;
    } elsif ($sorted_start_events[$i] <= $sorted_end_events[$j]) {
        push @events, $sorted_start_events_with_type[$i];
        $i++;
    } else {
        push @events, $sorted_end_events_with_type[$j];
        $j++;
    }
}

my $active = 0;
my $sum = 0;

for my $event (@events) {
    if ($event->[1] == 1) {
        $sum += $active;
    }
    $active += $event->[1];
}

print "$sum\n";