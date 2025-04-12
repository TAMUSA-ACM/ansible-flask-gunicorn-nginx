# ansible-flask-gunicorn-nginx

## Project Overview
This repository provides an Ansible-based automation template for setting up a Flask web application with Gunicorn and NGINX on an Ubuntu Vagrant machine. The aim of this project is to showcase the potential of automation in DevOps by simplifying the deployment process and eliminating the need for extensive bash scripting. It covers a range of topics including automation, flask, vagrant, webapp, ansible, backend, bash, microservice, script, scripting, and task.

## Setup / Installation Instructions

### Dependencies
Before you can use this repository, make sure you have the following software installed on your system:

- Vagrant
- VirtualBox
- Ansible

### Steps
1. Clone this repository to your local machine: 
```bash
git clone https://github.com/yourusername/ansible-flask-gunicorn-nginx.git
```
2. Navigate to the cloned repository:
```bash
cd ansible-flask-gunicorn-nginx
```
3. Run the Vagrant machine:
```bash
vagrant up
```
4. SSH into the Vagrant machine:
```bash
vagrant ssh
```
5. Run the Ansible Playbook:
```bash
ansible-playbook playbook.yml
```

## Usage Examples
Once you have the Vagrant machine up and running with the Flask application, you can access it by navigating to `http://localhost:8080` on your web browser. 

## Contribution Guidelines
We welcome contributions from the community. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes in your branch.
4. Submit a pull request with a detailed explanation of your changes.

Before submitting your pull request, make sure your changes do not break the existing functionality of the application. 

## License
This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.