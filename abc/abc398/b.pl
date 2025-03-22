my @a = split ' ', <>;

my %occurence_count;

for my $a (@a) {
  $occurence_count{$a}++;
}

my $ok_3 = 0;
my $ok_2 = 0;

for my $a (keys %occurence_count) {
  if ($occurence_count{$a} > 2) {
    $ok_2 = 1 if $ok_3;
    $ok_3 = 1 unless $ok_3;
  }
  elsif ($occurence_count{$a} > 1) {
    $ok_2 = 1;
  }
}

if ($ok_3 && $ok_2) {
  print "Yes\n";
}
else {
  print "No\n";
}
