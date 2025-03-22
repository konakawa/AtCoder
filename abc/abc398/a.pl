my $n = int <>;

my $is_odd = $n % 2 == 1;

my $result = '';
if ($is_odd) {
  for (1..int($n/2)) {
    $result .= '-';
  }
  $result .= '=';
  for (1..int($n/2)) {
    $result .= '-';
  }
}
else {
  for (1..int($n/2)-1) {
    $result .= '-';
  }
  $result .= '==';
  for (1..int($n/2)-1) {
    $result .= '-';
  }
}

print $result . "\n";
