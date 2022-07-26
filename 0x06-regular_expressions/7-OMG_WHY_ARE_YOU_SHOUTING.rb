#!/usr/bin/env ruby
# This script accepts one argument and passes it to a regular expression,
# matching method
# This script should output: [SENDER],[RECEIVER],[FLAGS]

string = ARGV[0]
sender = string.scan(/\[from:(.?\w+)/).join
reciver = string.scan(/\[to:(\+?\d+)/).join
flags = string.scan(/\[flags:(.?\d:.?\d:.?\d:.?\d:.?\d)/).join
puts "#{sender},#{reciver},#{flags}"
