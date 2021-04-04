# Craete file in tmp -> holberton
file { '/tmp/holberton':
ensure  => 'file',
content => 'I love Puppet',
owner   => 'www-data',
group   => 'www-data',
mode    => '0744',
}
