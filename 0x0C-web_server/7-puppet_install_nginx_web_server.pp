# Configures Nginx web server
exec { 'Update_packages_DB':
  command => 'sudo apt-get update -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'Install_Nginx':
  require => Exec['Update_packages_DB'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'Change_index':
  require => Exec['Install_Nginx'],
  command => 'sudo echo "Holberton School" > /var/www/html/index.nginx-debian.html',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'Redirection':                                                                                                                          
  require     => Exec['Change_index'],                                                                                                         
  environment => ["command='\\\n\t# Redirection\n\trewrite ^/redirect_me/(.*)$ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;"],                                                                                       
  command     => 'sed -i "/server_name _;/ a $command" /etc/nginx/sites-availablle/default',                                                                                                                                    
  path        => ['/usr/bin', '/bin'],                                                                                                         
  returns     => [0,1]                                                                                                                         
}   

exec { 'Start_service':
  require => Exec['Redirection'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}
