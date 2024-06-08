my $n = int <>;

sub concat_grid {
    my ($grid1, $grid2) = @_;

    my @grid1_lines = split "\n", $grid1;
    my @grid2_lines = split "\n", $grid2;

    my @combined_grid;
    for my $i (0..$#grid1_lines) {
        push @combined_grid, $grid1_lines[$i] . $grid2_lines[$i];
    }

    return join "\n", @combined_grid;
}

sub grid {
    my $level = shift;

    return '#' if $level == 0;

    my $size_pred_level = 3 ** ($level - 1);

    my $center_grid = '';
    for (1..$size_pred_level) {
        $center_grid .= '.' x $size_pred_level . "\n";
    }

    my $grid_pred_level = grid($level - 1);

    my $line1and3 = concat_grid $grid_pred_level, concat_grid $grid_pred_level, $grid_pred_level;
    my $line2 = concat_grid $grid_pred_level, concat_grid $center_grid, $grid_pred_level;

    return $line1and3 . "\n" . $line2 . "\n" . $line1and3;
}

print grid $n;
print "\n";