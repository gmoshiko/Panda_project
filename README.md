# BigPanda DevOps Exercise
#### INTRO
Deploying Gify-Panda and Counter-Panda to Vagrant container, ansible playbook can be used for deploy, and see if the services is started.

#### Get your environment ready
You'll need a linux machine with the ability to run vms.

1. Make sure you have python 2.7 installed. (Ubuntu 14.04 is highly recommended).
1. Install Ansible (version 2.1).
1. Install Vagrant.
1. Install VirtualBox.
1. Mirror this git repo using the instructions [here](https://help.github.com/articles/duplicating-a-repository). Then clone it locally.
1. Run `vagrant up base` and make sure you can ssh into the machine using `vagrant ssh base`.
1. Open your browser, go to <http://localhost:8090> (Gify-Panda) or to <http://localhost:9000> (Counter-Panda)

#### How they work and whats it doing ?
Both Service will be delopyed to  the vagrant container at: /tmp/
Both Service will have upstart config file.

###### Gify-Panda
Gify-Panda just serv 3 working/hello/stop pandas. you have a simple menu at <http://localhost:8090> 
You can upload new pandas and run 'ansible-playbook base.yml' and deploy your new PANDAS YEY!
*PORT*: you  can change port listening on " /roles/gify-panda/file/gify-panda/gify-panda.py ". just change PORT_NUMBER variable
After Deploy you can start/stop/restart the service by running: 'sudo gify-panda start/stop/restart'.
For more help: '/tmp/gify-panda/gify-panda.py -h'

###### Counter-Panda
Counter-Panda is a POST countering, it will respone to GET request the amont of POST request he counted. <http://localhost:8100> 
You can update the code and deploy the service by running: 'ansible-playbook base.yml'.
*PORT*: you  can change port listening on " /roles/counter-panda/counter-panda.py ". just change PORT_NUMBER variable
After Deploy you can start/stop/restart the service by running: 'sudo counter-panda start/stop/restart'.
For more help: '/tmp/counter-panda/counter-panda.py -h'


#### HOP YOU ENJOYED. 

##### Email: gmoshiko@gmail.com



