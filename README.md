# Some examples on how to use the OVHcloud APIsto control AI-Training


## Regional API

This is the API dedicated to AI-Training. It is distinct from the main OVHcloud API.

The examples are all using the file config.json, so you have to create your own.
Just copy the provided config-example.json with the name config.json, and add the following information :

- client_id and client_secret : your app id and secret. At the time of writing, you cannot create your own,
  but you can use those of the ovhai CLI. Install the CLI (you may already have it), and find them in the config file.json
  (~/.ovhai/config.json)
- OpenStack user and password
- 
