# Automate the task of creating a custom HTTP header response with Puppet.
# The name of the custom HTTP header must be X-Served-By.
# The value of the custom HTTP header must be the hostname of the server Nginx is running on.

exec {'update':
  command => '/usr/bin/apt-get update',
}
-> package {'nginx':
  ensure => 'present',
}
-> file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  match => 'http {',
}
-> exec {'start':
  command => '/usr/sbin/service nginx start',
}
