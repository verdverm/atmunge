# Hyperbolic.ai

- https://hyperbolic.ai/
- https://app.hyperbolic.ai/
- https://docs.hyperbolic.xyz/

A great place to rent H100 VMs



## Setup - from your computer

You should already have a

- huggingface account, you will need a create token during setup
  - some models require you accept terms before being able to download too (i.e. all of the safety ones)
- hyperbolic account, because that's what we're doing after all

### Hyperbolic one-time setup

> [!NOTE]
> Their cli or api seems broken, getting nothing but 404s when running their example commands
> You can skip this step for now, setup an instance in the web UI

https://docs.hyperbolic.xyz/docs/hyperbolic-cli

```sh
# install the cli
brew install HyperbolicLabs/hyperbolic/hyperbolic

hyperbolic auth login
```

### Starting an instance

Their cli or api seems broken, getting nothing but 404s when running their example commands

You can setup an instance in the UI though

Setup `.ssh/config`, adjust IP and Port

```
Host hyperbolic
  HostName 147.185.41.173
  User user
  IdentityFile ~/.ssh/id_ed25519
  Port 20013
```

## Setup - from vm

> [!WARNING]
> All subsequent commands are run from your Hyperbolic VM

`ssh hyperbolic`


### Setting up atmunge


```sh
# get the repo
git clone https://github.com/blebbit/atmunge
cd atmunge

# more vm setup
./ai/devops/hyperbolic/setup.sh

# ...
# there will be several prompts, a reboot, and a relog
# ...

# build the command
make install

# test it works
atmunge firehose

# setup python
uv sync
```


### Running Models

You should now be able to run various models and python code.

Check out the [ATMunge BentoML Guide](./bento.md) to get started.