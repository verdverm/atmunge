# BentoML

We use [BentoML](https://docs.bentoml.com/en/latest/index.html)
to handle model management and serving.

The majority of the services are single-model,
some like `safety-mesh` combine several modals in a single service.
There are lots of interesting ways to compose them and bentoml makes that super easy,
while still giving you low-level access to the models when you need it.


### Running Models

The model capacity and performance are highly dependent on hardware.
We have run on both commodity and datacenter GPUs to make sure
`atmunge` is accessible at both ends of the spectrum.
You can rent H100|200s from [Hyperbolic](./hyperbolic.md) on the cheap, we do this a lot now.
If you are doing bulk processing, it can be just $10s of dollars and much faster.

You may wish to change the model size or requested resources.
They tend to default to settings ideal on Hyperbolic.
Look to the `service.py` in each directory.

```sh
cd ./ai/bento
make <model>/serve
```

#### Safety Models:

| Model | class | inputs | outputs | notes |
|-|-|-|-|-|
| promptguard2 | safety | text  | boolean | prompt safety |
| shieldgemma  | safety | text  | policy score | custom policy |
| shieldgemma2 | safety | image | scores | custom policy |
| llamaguard4  | safety | multi | boolean | custom policy |
| safety-mesh  | safety | multi | mixed | combo of above |

#### General Models:

| Model | class | inputs | outputs | notes |
|-|-|-|-|-|
| gemma3       | chat   | multi | text | instruction |


> [!NOTE]
> note to self, write way more about the models, in a separate page(s)

### Testing Models

The following runs a `test.sh` in the model's directory.
It's essentially a series of curl calls and json files.


```sh
make <model>/test
```

The endpoint to call is the same as the function name.
There is generally an amount of consistency,
but if you have 404s, this is a good place to check.


```py
@bentoml.api
async def check()

# or

@bentoml.api
async def chat()
```
