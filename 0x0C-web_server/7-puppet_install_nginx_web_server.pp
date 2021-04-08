# Configures Nweb server
exec { 'Update packages DB':
  command => 'apt-get update -y',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Install Nginx':
  require => Exec['Update packages DB'],
  command => 'apt-get install nginx -y',
  path    => ['/usr/bin', '/bin'],
}

exec { 'Change index.html':
  require => Exec['Install Nginx'],
  command => 'echo "Holberton School" > /var/www/html/index.nginx-debian.html',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'Redirection':
  require     => Exec['Change index.html'],
  environment => ['command="\\\n\t# Redirection\n\trewrite ^/redirect_me/(.*)$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;"'],
  command     => 'sed -i "/server_name _;/ a $command" /etc/nginx/sites-available/default',
  path        => ['/usr/bin', '/bin'],
}

exec { 'Start service':
  require => Exec['Redirection'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
}
