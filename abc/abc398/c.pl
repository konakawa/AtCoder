my $n = int <>;
my @as = split ' ', <>;

my %occurence_count = ();
for my $a (@as) {
  $occurence_count{$a}++;
}

my @desc_sorted_keys = sort { $b <=> $a } keys %occurence_count;

my $result_value = -1;

for my $key (@desc_sorted_keys) {
  my $count = $occurence_count{$key};
  if ($count == 1) {
    $result_value = $key;
    last;
  }
}

my $result_index = -2;
for my $i (0..$n-1) {
  if ($as[$i] == $result_value) {
    $result_index = $i;
    last;
  }
}

print $result_index + 1 . "\n";
