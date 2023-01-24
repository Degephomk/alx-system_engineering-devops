#nginx using puppet

exec { 'apt-get-update' :
  command => 'sudo apt-get update -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'nginx' :
  require => Exec['apt-get-update'],
  command => 'sudo apt-get install nginx -y',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'htmlcontent' :
  require => Exec['nginx'],
  command => 'sudo echo "Holberton School for the win!" | sudo tee /var/www/html/index.nginx-debian.html',
  path    => ['/usr/bin', '/bin'],
  returns => [0,1]
}

exec { 'redirection' :
  require     => Exec['nginx'],
  environment => ['YY=youtube.com permanent'],
  command     => 'sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me $YY;/" /etc/nginx/sites-enabled/default',
  path        => ['/usr/bin', '/bin'],
  returns     => [0,1]
}


exec { 'nginxstart' :
  require => Exec['htmlcontent'],
  command => 'sudo service nginx start',
  path    => ['/usr/bin', '/bin', '/usr/sbin'],
  returns => [0,1]
}
