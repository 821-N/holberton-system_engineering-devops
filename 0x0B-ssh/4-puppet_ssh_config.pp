# Edit ssh config file
file_line { 'Use private key holberton':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'Disable password authentication':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
