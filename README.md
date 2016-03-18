AnDoKaElk
================================================================================
##### (Ansible Orchestrated Dockerized Kafka and Elasticsearch Clusters)

###### Creation: Lingxiao Xia
###### Creation Date: 2016-03-17

This package creates a all components of a log processing pipeline. 

A few steps to take before running the playbook:

1. Please open the inventory file [staging](staging) to modify the destinations and corresponding variables according to your setup.
2. Please install `ansible 2.0.0.2` and its dependencies.
3. Run `ansible-vault create vars/common_vault` and add the following variables for passwords:
    * `vault_ca_pass`
    * `vault_registry_pass`
4. Run `ansible-vault create vars/vault` and add your google app client info, for more information on google app client, please visit [google developer console](https://console.developers.google.com/):
    * `vault_google_app_client_id`
    * `vault_google_app_client_secret`
5. Add a valid redirect uri for `elasticsearch` to your google app client via google developer console. This should be the same as `https://{{ expose_elasticsearch_as }}:{{ expose_elasticsearch }}` from your `gateway` host variables. 
6. Add a valid redirect uri for `kibana` to your google app client via google developer console. This should be the same as `https://{{ expose_kibana_as }}:{{ expose_kibana }}` from your `gateway` host variables. 
7. Please make sure that `docker 1.10.0` and its dependencies are installed and running as a service on all destination hosts.
8. Please create an overlay network `{{ default_network }}` using `docker-machine` on all destination hosts. 
9. Create all images. Run the following command at project folder:
    ```
    ansible-playbook -i staging --ask-vault-pass images.yaml
    ```

To start all containers:
```
ansible-playbook -i staging --ask-vault-pass run.yaml
```

To stop and remove all containers:
```
ansible-playbook -i staging --ask-vault-pass stop.yaml
```

To clean up all generated contents:
```
ansible-playbook -i staging --ask-vault-pass -K clean.yaml
```
