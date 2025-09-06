# Notes 



## Data Sources

These come from the ATProto network itself
or others who have aggregated the data from the network.

#### PLC

- https://plc.directory

#### PDS List

- https://bsky-debug.app/
- https://github.com/pirmax/atproto-pds-tracker
- The PLC logs
- https://github.com/mary-ext/atproto-scraping



## Feedgens

#### Links

-  https://tangled.sh/@willdot.net/feed-demo-go



## AI


### General Links


#### Trust & Safety

- https://ai.google.dev/responsible
- https://www.llama.com/llama-protections/
- https://thealliance.ai/blog/the-state-of-open-source-trust


### Fine-tune, LoRA, ect

- https://ai.google.dev/responsible/docs/safeguards/agile-classifiers


### Models of interest

#### Generative

We focus on the most recent version in a family, they are noticably better.
The older models are around because several other models
are LoRA adapters on the prior generation(s).

The generative modles are used for topic/sentiment analysis so far.
Thinking models aren't great for what we are doing (yet) because...
they spend far too much time thinking and don't produce
noticable better results from basic chage models.



- https://huggingface.co/google/gemma-3-270m
- https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/gemma3.md
- ....


#### Content Policy

- https://huggingface.co/google/shieldgemma-27b
- https://huggingface.co/google/shieldgemma-2-4b-it
- https://github.com/huggingface/transformers/blob/main/docs/source/en/model_doc/shieldgemma2.md
- https://huggingface.co/meta-llama/Llama-Guard-4-12B
- https://huggingface.co/zentropi-ai/cope-a-9b

#### Prompt Safety

- https://huggingface.co/meta-llama/Llama-Prompt-Guard-2-86M
- https://huggingface.co/Roblox/Llama-3.1-8B-Instruct-RobloxGuard-1.0


#### Unsorted

- https://docs.mistral.ai/capabilities/guardrailing/
- https://github.com/Roblox/RobloxGuard-1.0


### Datasets of interest

Safety:

- ATProto labeler dumps (tbd)
- https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0