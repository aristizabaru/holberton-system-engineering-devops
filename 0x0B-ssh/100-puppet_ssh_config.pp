# Configure config global file
include stdlib

file_line { 'Set IdentityFile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
}
file_line { 'Set PasswordAuthentication':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}

