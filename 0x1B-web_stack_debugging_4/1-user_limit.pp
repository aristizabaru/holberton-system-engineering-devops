# Change the OS configuration
exec { 'task-1' :
  provider => 'shell',
  command  => 'sed -i s/holberton.*//g /etc/security/limits.conf',
}
