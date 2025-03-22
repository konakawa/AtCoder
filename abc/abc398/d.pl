my ($n, $r, $c) = split ' ', <>;
my $s = <>;
chomp $s;

my %moves = (
  'N' => [-1, 0],
  'S' => [1, 0],
  'E' => [0, 1],
  'W' => [0, -1],
);

my @results = ();
my %seen_positions;
my $current_r = 0;
my $current_c = 0;

$seen_positions{"0,0"} = !!1;

for my $i (1..$n) {
  my $direction = substr($s, $i-1, 1);
  my $move = $moves{$direction};
  
  $current_r += $move->[0];
  $current_c += $move->[1];
  
  my $target_r = $current_r - $r;
  my $target_c = $current_c - $c;
  my $target_key = "$target_r,$target_c";

  my $result = exists $seen_positions{$target_key} ? 1 : 0;
  push @results, $result;

  $seen_positions{"$current_r,$current_c"} = !!1;
}

print join('', @results) . "\n";
