# Enables the user holberton to login and open files without error.
exec {'increase_hard_file_limit_for_holberton_user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

exec {'increase_soft_file_limit_for_holberton_user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}'
