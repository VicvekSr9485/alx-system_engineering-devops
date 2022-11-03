# Using strace, find out why Apache is returning a 500 error and fix
exec { 'fixes http error 500':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin','/bin']
}
