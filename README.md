<center><h1>Using Ansible 2 to automate the creation of a Flask + Gunicorn + NGINX Web Application on Ubuntu Vagrant Machine</h1></center>

**NOTE:** This is a simple template, but it demonstrates how automation saves a ton of time instead of writing a ton of bash scripts to setup a webserver. This was done in a test environment on a vagrant instance of Ubuntu Bionic.

## Pre-requisites

### Install VirtualBox and Vagrant
- CraftedTech Blog Instructions: https://craftedtech.net/post/vagrant-virtualbox-setup/

### Install VirtualBox
- Installation: https://www.virtualbox.org/wiki/Downloads

### Setup Vagrant
- Installation: https://www.vagrantup.com/docs/installation/
- Useful Vagrant Specific Commands: https://www.vagrantup.com/docs/cli/

## Spin up Ubuntu to setup Ansible Server
- `vagrant box list` - Shows your currently installed boxes

**Create a vagrant project folder**

*If using Powershell on Windows, make sure you open it as **administrator***
- `sudo mkdir ansible-server`
- `vagrant box add ubuntu/bionic64` - Installs Ubuntu Bionic 64-bit (Ubuntu 18.04)
   - *This may take a while as it needs to download the instance*
- Open the **Vagrantfile** that's pulled down, if you have issues, just run the following command: `vagrant init ubuntu/bionic64`, it should look like this:
```ruby
Vagrant.configure("2") do |config|
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vm.hostname = "ansible-box"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  config.vm.network "public_network"
end
```
- **NOTE:** The above configuration file is the vagrant config for your machine, you'll notice that the network is set to public network, as it explains, your hosting machine will act as a bridge to bring your machine onto the network. You could set the network to be private if you like, if you do, look at Vagrant's documentation to understand private networks.
- `vagrant up` - Brings up the machine
- `vagrant ssh` - SSH into your machine
- `vagrant halt` - shuts the vagrant machine down, you could use -f argument to force it
- `vagrant destroy` - stops the machine and for all intents and purposes, destroys it, you cannot recover this instance if you run this command

## Setting up Ansible 2

### Get Latest Releases via Apt
- `sudo apt-get update`
- `sudo apt-get install software-properties-common`

#### Install Ansible
- Via Apt
  - `sudo apt-add-repository --yes --update ppa:ansible/ansible` - This can take a while
  - `sudo apt-get install ansible -y`
- Via pip
  - `sudo apt install python3-pip`
  - `sudo pip3 install ansible`

#### Configure Ansible
- `sudo vim /etc/ansible/ansible.cfg` - make sure to uncomment the host_key_checking and set it to False per the following:
```
[defaults]
host_key_checking = False
```

- Configure what hosts Ansible Server will connect to
  - Each one of the *target* machines need to have python and SSH setup
  - `sudo vim /etc/ansible/host` - the following code block is an **example** of a setup
```
[webservers]
192.168.1.10 ansible_ssh_port=22 ansible_ssh_user=vagrant ansible_ssh_private_key_file=/home/vagrant/.ssh/id_rsa
```
- **NOTE:** Verify the SSH port, with Vagrant sometimes this can change, a good command to verify this is to run this command on the machine in question: `sudo netstat -tulpn`, this will show what ports are open and listening

## Setup Ansible Target - Webserver
