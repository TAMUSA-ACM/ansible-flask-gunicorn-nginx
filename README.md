# ansible-flask-gunicorn-nginx

This repository hosts an Ansible-based automation template designed to streamline the deployment process of a Flask web application using Gunicorn and NGINX on an Ubuntu Vagrant machine. It showcases the effectiveness of automation in DevOps, minimizing the need for complex bash scripting and enhancing the ease of deployment for Flask-based applications.

## Project Overview

The structure of this project is organized to facilitate easy understanding and modification:

```
ansible-flask-gunicorn-nginx/
│
├── ansible/
│   ├── playbooks/
│   │   ├── setup.yml           # Main Ansible playbook to setup the entire stack
│   │   └── ...
│   ├── roles/
│   │   ├── flask/
│   │   ├── gunicorn/
│   │   ├── nginx/
│   │   └── ...
│   └── hosts                   # Inventory file for Ansible
│
├── vagrant/
│   ├── Vagrantfile             # Configuration for Vagrant machine
│   └── ...
│
├── app/
│   ├── main.py                 # Sample Flask application
│   ├── requirements.txt        # Python dependencies for the Flask app
│   └── ...
│
└── README.md
```

### Dependencies

- **Ansible**: For automating the deployment process.
- **Vagrant**: Used for creating and configuring virtual development environments.
- **VirtualBox**: As the provider for Vagrant machines.
- **Python**: Required by Flask and to run Ansible scripts locally.
- **Flask**: Python web framework.
- **Gunicorn**: WSGI HTTP Server for UNIX to serve Python applications.
- **NGINX**: Web server used as a reverse proxy for Gunicorn.

## Setup & Installation

### Prerequisites

Ensure you have the following installed on your local machine:
- Ansible
- Vagrant
- VirtualBox
- Python

### Getting Started

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ansible-flask-gunicorn-nginx.git
   cd ansible-flask-gunicorn-nginx
   ```

2. **Start Vagrant Machine**

   Navigate to the `vagrant` directory and run:

   ```bash
   vagrant up
   ```

   This command will set up an Ubuntu virtual machine with all necessary configurations.

3. **Run Ansible Playbook**

   After the Vagrant machine is up and running, execute the Ansible playbook:

   ```bash
   ansible-playbook -i ansible/hosts ansible/playbooks/setup.yml
   ```

   This will install and configure Flask, Gunicorn, and NGINX on the Vagrant machine.

## Usage

Once the setup is complete, you can access the Flask application via your web browser:

```
http://localhost:8080
```

This URL will route you through NGINX to the Gunicorn served Flask app running inside the Vagrant machine.

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

This README aims to cover all the necessary steps to get this project up and running on your local machine. For more detailed instructions or troubleshooting, consider exploring more specific documentation or the project's issue tracker.