import bentoml, pydantic
from PIL import Image
import requests
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = ""



# Check if CUDA is available and set the device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")



MODEL_ID = "Qwen/Qwen3-Next-80B-A3B-Instruct"
IMAGE = bentoml.images.PythonImage(python_version='3.13')
  # .requirements_file('requirements.txt')

class Qwen3NextResponse(pydantic.BaseModel):
  message: str

@bentoml.service(
  resources={
    # "cpu": 1,
    # "memory": "4Gi",
    "gpu": 2,
  },
  traffic={"concurrency": 5, "timeout": 300},
  # envs=[{'name': 'HF_TOKEN'}],
  image=IMAGE
)
class Qwen3Next:
  model = bentoml.models.HuggingFaceModel(MODEL_ID)

  def __init__(self):

    self.tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    self.model = AutoModelForCausalLM.from_pretrained(self.model, device_map="auto", dtype="auto")


  @bentoml.api
  async def qwen3next(self,
    # messages
  ) -> Qwen3NextResponse:

    # messages = [
    #   {
    #     "role": "system",
    #     "content": [{"type": "text", "text": "You are a helpful assistant."}]
    #   },
    #   {
    #     "content": [
    #       {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
    #       {"type": "text", "text": "What animal is on the candy?"}
    #     ]
    #   }
    # ]

    # messages = [
    #   {
    #     "role": "user",
    #     "content": [
    #       {
    #         "type": "video",
    #         "video": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2-VL/space_woaudio.mp4",
    #       },
    #       {"type": "text", "text": "Describe this video."},
    #     ],
    #   }
    # ]
    # prepare the model input
    prompt = "Give me a short introduction to large language model."
    messages = [
      {"role": "user", "content": prompt},
    ]


    print("inputs:", messages)

    # Preparation for inference
    text = self.tokenizer.apply_chat_template(
      messages,
      tokenize=False,
      add_generation_prompt=True,
    )
    model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)

    # conduct text completion
    generated_ids = self.model.generate(
      **model_inputs,
      max_new_tokens=16384,
    )
    output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

    content = self.tokenizer.decode(output_ids, skip_special_tokens=True)

    print("content:", content)

    # print("outputs:", outputs)
    # msg = self.processor.decode(outputs[0][inputs["input_ids"].shape[-1]:])
    # print(msg)

    return Qwen3NextResponse(message=content)