#!/usr/bin/env ruby
# Use of non-greedy quantifiers
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")