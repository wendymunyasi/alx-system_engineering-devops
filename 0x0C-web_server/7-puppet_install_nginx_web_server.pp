# Installs and configure an Nginx server using Puppet instead of Bash
# Nginx should be listening on port 80
# When querying Nginx at its root / with a GET request (requesting a page)
# using curl, it must return a page that contains the string Hello World!
# The redirection must be a “301 Moved Permanently”
# Your answer file should be a Puppet manifest containing commands to
# automatically configure an Ubuntu machine to respect above requirements

exec {'install':
  provider => shell,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/github.com\/luischaparroc permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
