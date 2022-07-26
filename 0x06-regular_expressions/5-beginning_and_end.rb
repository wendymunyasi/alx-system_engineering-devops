#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# The regular expression must be exactly matching a string that starts,
# with h ends with n and can have any single character in between

puts ARGV[0].scan(/^h.n$/).join
