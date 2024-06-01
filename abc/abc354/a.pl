my $h = int <>;

my $tree = 0;
my $count = 0;

while (1) {
    $tree += 2 ** $count;
    if ($tree > $h) {
        print $count+1 . "\n";
        exit;
    }
    $count++;
}