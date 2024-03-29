# Increases amount of traffic an Nginx server can handle.
exec {'set file limit for nginx':
  command => 'sed -i "s/15/2000/g" /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/',
  onlyif  => 'test -f /etc/default/nginx'
}
