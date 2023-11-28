#!/usr/bin/env ruby
#This ruby script that accepts one argument and pass it to a regular expression matching method.
#The regular expression must match a 10 digit phone number.

puts ARGV[0].scan(/^\d{10,10}$/).join
