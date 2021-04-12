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

exec { 'Header':                                                                                                                          
  require     => Exec['Change_index'],                                                                                                                                                                                               
  command     => "sed -i '/rewrite/ a \n\t# Add header directive\n\tadd_header X-Served-By \$hostname;\n' /etc/nginx/sites-available/default",                                                                                                                                    
  path        => ['/usr/bin', '/bin'],                                                                                                         
  returns     => [0,1]                                                                                                                         
}   

exec { 'Start_service':
  require => Exec['Header'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}
