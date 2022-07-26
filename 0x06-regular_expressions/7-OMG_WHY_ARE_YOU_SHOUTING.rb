#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# This script should output: [SENDER],[RECEIVER],[FLAGS]

puts ARGV[0].scan(/\[from:(\+?(?:\w)+)\]\s\[to:(\+?(?:\w)+)\]\s\[flags:((?:-?\d:?)+)\]/).join(separator=",")"
