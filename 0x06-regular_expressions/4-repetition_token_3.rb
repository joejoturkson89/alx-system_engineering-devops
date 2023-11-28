#!/usr/bin/env ruby
#This ruby script accepts one argument and pass it to a regular expression matching method.
#Regex script should not contain square brackets.

puts ARGV[0].scan(/hbt*n/).join
