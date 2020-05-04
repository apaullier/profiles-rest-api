# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
 # The most common configuration options are documented and commented below.
 # For a complete reference, please see the online documentation at
 # https://docs.vagrantup.com.

 # Every Vagrant development environment requires a box. You can search for
 # boxes at https://vagrantcloud.com/search.
 config.vm.box = "ubuntu/bionic64"
 config.vm.box_version = "~> 20200304.0.0"

 config.vm.network "forwarded_port", guest: 8000, host: 8000 # host machine is our laptop
# guest machine is the development server, by default ports are not automatically accesible on any guest machine
 config.vm.provision "shell", inline: <<-SHELL # to run scripts
   systemctl disable apt-daily.service # disable autoupdate which conflicts with sudp apt-get update
   systemctl disable apt-daily.timer

   sudo apt-get update # update local repo with all available packages
   sudo apt-get install -y python3-venv zip
   touch /home/vagrant/.bash_aliases # python 3 is set as default instead of python 2.7
   if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
     echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
     echo "alias python='python3'" >> /home/vagrant/.bash_aliases
   fi
 SHELL
end
