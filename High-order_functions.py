# Higher-order functions allow you to define functions that manipulate arrays in SQL
REDUCE(demo_array, 0, ( element , acc ) -> element + acc, acc ->(acc div size(demo_array)))
# acc is the accumulator variable; it holds a running total of the elements as they are summed in the first function of this command
# Rollup generates subtotals and grand totals for a set of columns. Cube generates subtotals and grand totals for all possible combinations of the grouping columns specified
