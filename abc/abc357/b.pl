my $str = <>;

my $uppercase_count = 0;
my $lowercase_count = 0;

$uppercase_count = () = $str =~ /[A-Z]/g;
$lowercase_count = () = $str =~ /[a-z]/g;

if ($uppercase_count > $lowercase_count) {
    print uc($str);
}
else {
    print lc($str);
}