# Configures Nginx web server
exec { 'Update_packages_DB':
  command  => 'sudo apt-get update',
  provider => 'shell',
  user     => 'root',
}

package { 'nginx':
  ensure   => installed,
}

file_line { 'add_header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;',
  line   => 'add_header X-Served-By $hostname;'
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx']
}
