# fix typo in file extension

exec { 'fix .phpp':
  command => '/bin/sed -i s/phpp/php/ /var/www/html/wp-settings.php',
}
