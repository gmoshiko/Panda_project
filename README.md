# BigPanda DevOps Exercise
#### INTRO
Deploying Gify-Panda and Counter-Panda to Vagrant container, Ansible playbook can be used for deploy, and see if the services are started.

#### Get your environment ready
You'll need a Linux machine with the ability to run VMS.

1. Make sure you have Python 2.7 installed. (Ubuntu 14.04 is highly recommended).
1. Install Ansible (version 2.1).
1. Install Vagrant.
1. Install VirtualBox.
1. Mirror this git repo using the instructions [here](https://help.github.com/articles/duplicating-a-repository). Then clone it locally.
1. Run `vagrant up base` and make sure you can ssh into the machine using `vagrant ssh base`.
1. Open your browser, go to <http://localhost:8090> (Gify-Panda) or to <http://localhost:9000> (Counter-Panda)

#### How do they working?
Both Service will be deployed to  the vagrant container at: /tmp/
Both Service will have an upstart config file.

###### Gify-Panda
Gify-Panda just serves 3 working/hello/stop pandas. you have a simple menu at <http://localhost:8090> 
You can upload new pandas and run 'ansible-playbook base.yml' and deploy your new PANDAS YEY! <br />
*PORT*: you  can change port listening on " /roles/gify-panda/files/gify-panda/gify-panda.py ". just change PORT_NUMBER variable
After Deploy you can start/stop/restart the service by running: 'sudo gify-panda start/stop/restart'.
For more help: '/tmp/gify-panda/gify-panda.py -h'

###### Counter-Panda
Counter-Panda is a POST countering, it will respond to GET request the amount of POST request he counted. <http://localhost:8100> 
You can update the code and deploy the service by running: 'ansible-playbook base.yml'.
*PORT*: you  can change port listening on " /roles/counter-panda/files/counter-panda.py ". just change PORT_NUMBER variable
After Deploy you can start/stop/restart the service by running: 'sudo counter-panda start/stop/restart'.
For more help: '/tmp/counter-panda/counter-panda.py -h'


#### HOP YOU ENJOYED. 

##### Email: gmoshiko@gmail.com


