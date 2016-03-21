AnDoKaElk
================================================================================
##### (Ansible Orchestrated Dockerized Kafka and Elasticsearch Clusters)

###### Creation: Lingxiao Xia
###### Creation Date: 2016-03-17

This is an `ansible` playbook for creating a secured and dockerized private `kafka` and `elasticsearch` cluster with `logstash` as connectors. It uses `kibana` and `elasticsearch-kopf` as UI and [`oauth2_proxy`](https://github.com/bitly/oauth2_proxy) as security frontend.

A few steps to take before running the playbook:

1. Make sure that `docker 1.10.3` is installed locally.
2. Install `docker-machine v0.6.0` locally and use `docker-machine` to create a `swarm` cluster with an `overlay` network `{{ default_network }}`("andofaelk_default")  with at least two instances. One of them will act as the `gateway` and the others as `nodes`. They are treated as the destination hosts. `gateway` requirements at least 1GB ram. `nodes` require a lot more because `elasticsearch` requires a lot more RAM for good performance. Normally 16GB is the minimum. 
3. Create your own private/public key pair and add the public key to all destination hosts' `~/.ssh/authorized_keys`. Use your private key for accessing the destination hosts.
4. If you are testing the package locally, there is no need for installing `docker-machine` and creating the `overlay` network. Create a docker group and add your user(`sudo usermod -aG docker $(whoami)`) so that you could run `docker` without `sudo`. Next, create a private `bridge` network with `docker network create {{ default_network }}`. 
5. Make sure all distination hosts have `python2.7` installed. 
6. If you would like to create a private docker registry and use it for all your images, you could do so with [dockreg](http://xialingxiao.github.io/dockreg). In which case, make sure `pip` and python package `pexpect` are installed at registry host. 
7. Install `ansible 2.0.0.2` and its dependencies locally.
8. Open the inventory file [staging](https://github.com/xialingxiao/andokaelk/blob/master/staging) and modify the destinations accordingly and update the variables stored in the files in the [vars/](https://github.com/xialingxiao/andokaelk/tree/master/vars) directory. 
9. Choose a vault passphrase and use the same passphrase for the following two steps.
10. Run `ansible-vault create vars/common_vault` and add the following variables for passwords:
    * `vault_ca_pass`
    * `vault_registry_pass`
11. Run `ansible-vault create vars/vault` and add your google app client info, for more information on google app client, please visit [google developer console](https://console.developers.google.com/):
    * `vault_google_app_client_id`
    * `vault_google_app_client_secret`
12. Add a valid redirect uri for `elasticsearch` to your google app client via google developer console. This should be the same as `https://{{ elasticsearch_domain }}/oauth2/callback` from your `gateway` host variables. Or if it does not have a public domain, it should be `https://{{ expose_elasticsearch_as }}:{{ expose_elasticsearch }}/oauth2/callback`. Note that google app redirect uri is required to be either a public top-level domain or localhost, meaning `{{expose_elasticsearch_as}}` is required to be `127.0.0.1` unless google changes its policies in the future. You could use the `-L` option of `ssh` to create a ssh tunnel for accessing remote host's port locally, or `autossh` if you want persistant connection. For example, suppose you have set-up the cluster already, use `autossh -f -L {{ expose_elasticsearch }}:127.0.0.1:{{ expose_elasticsearch }} -i {{ hostvars['gateway']['ansible_ssh_private_key_file'] }} {{ hostvars['gateway']['ansible_user'] }}@{{ hostvars['gateway']['ansible_default_ipv4']['address']}} -N` to create the tunnel and point your browser at `127.0.0.1:{{ expose_elasticsearch }}/_plugin/kopf` to interact with your elasticsearch cluster.
13. Add a valid redirect uri for `kibana` to your google app client via google developer console. This should be the same as `https://{{ kibana_domain }}/oauth2/callback` from your `gateway` host variables. Or if it does not have a public domain, it should be`https://{{ expose_kibana_as }}:{{ expose_kibana }}/oauth2/callback`. Refer to previous step.
14. Please make sure that `docker 1.10.0` and its dependencies are installed and running as a service on all destination hosts and that `{{ ansible_user }}` has access to it without `sudo`.
15. Create all images. Run the following command at project folder:
    ```
    ansible-playbook -i staging --ask-vault-pass images.yaml
    ```

To start all containers:
```
ansible-playbook -i staging --ask-vault-pass -K run.yaml
```

[Andokaelk_Container_Structure_Diagram.pdf](https://github.com/xialingxiao/andokaelk/blob/master/Andokaelk_Container_Structure_Diagram.pdf) illustrates the complete container structure when you have one gateway and three nodes. Gateway also hosts a private docker registry in this case. The registry does not reside in the `overlay` network but has port 5000 open.

To stop and remove all containers:
```
ansible-playbook -i staging --ask-vault-pass stop.yaml
```

To clean up all generated contents:
```
ansible-playbook -i staging --ask-vault-pass -K clean.yaml
```

The `-K` option is only necessary if you are not operating as the root user and there is a root password. 
