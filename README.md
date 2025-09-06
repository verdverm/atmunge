# Blebbit AT Mirror

A collection of tools and utilities for backfilling, mirroring, and analyzing the ATProtocol network.


## Install & Setup

### The CLI

```sh
# get the repo
git clone https://github.com/blebbit/atmunge
cd atmunge

# install the cli
make install
```

### Network backfilling

```sh
# [ you can make a separate working dir if you like ]

# setup the env
cp env-example .env

# start the db for plc/accounts
docker compose up -d db

# run db migrations
atmunge db migrate
```

### AI, Datasci, and Python

```sh
uv sync
```


### Extra Dependencies

Varaious parts of `atmunge` require some extra tools

- docker
- postgresql tools (psql, pg_dump, pg_restore)

If you are backfilling large parts of the network,
you're going to want a big disk(s)


## Munging ATProto

The guides are in the `./docs` directory

- [Backfilling the Network](./docs/backfilling.md)
- [AI Processing & Analysis](./docs/bento.md)