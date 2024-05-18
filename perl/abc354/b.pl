my $n = int <>;
my @users = ();
for (0..$n-1) {
    my ($name, $score) = split / /, <>;
    push @users, [$name, $score];
}

my @sorted_users = sort { $a->[0] cmp $b->[0] } @users;

my $sum = 0;

for my $user (@sorted_users) {
    $sum += $user->[1];
}

my $i = $sum % $n;

print $sorted_users[$i][0] . "\n";