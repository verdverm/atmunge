import bentoml, pydantic
from PIL import Image
import requests
import torch
from transformers import AutoProcessor, Qwen2_5_VLForConditionalGeneration
from qwen_vl_utils import process_vision_info


# Check if CUDA is available and set the device
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")



# MODEL_ID = "Qwen/Qwen2.5-VL-3B-Instruct"
MODEL_ID = "Qwen/Qwen2.5-VL-7B-Instruct"
# MODEL_ID = "Qwen/Qwen2.5-VL-32B-Instruct"
# MODEL_ID = "Qwen/Qwen2.5-VL-72B-Instruct"
IMAGE = bentoml.images.PythonImage(python_version='3.13')
  # .requirements_file('requirements.txt')

class Qwen25VLResponse(pydantic.BaseModel):
  message: str

@bentoml.service(
  resources={
    # "cpu": 1,
    # "memory": "4Gi",
    "gpu": 1,
  },
  traffic={"concurrency": 5, "timeout": 300},
  # envs=[{'name': 'HF_TOKEN'}],
  image=IMAGE
)
class Qwen25VL:
  model = bentoml.models.HuggingFaceModel(MODEL_ID)

  def __init__(self):

    self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(MODEL_ID, torch_dtype="auto", device_map="auto")
    self.processor = AutoProcessor.from_pretrained(MODEL_ID)


  @bentoml.api
  async def qwen25vl(self,
    # messages
  ) -> Qwen25VLResponse:

    messages = [
      {
        "role": "system",
        "content": [{"type": "text", "text": "You are a helpful assistant."}]
      },
      {
        "role": "user",
        "content": [
          {"type": "image", "url": "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/p-blog/candy.JPG"},
          {"type": "text", "text": "What animal is on the candy?"}
        ]
      }
    ]

    messages = [
      {
        "role": "user",
        "content": [
          {
            "type": "video",
            "video": "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen2-VL/space_woaudio.mp4",
          },
          {"type": "text", "text": "Describe this video."},
        ],
      }
    ]

    print("inputs:", messages)

    # Preparation for inference
    text = self.processor.apply_chat_template(
      messages, tokenize=False, add_generation_prompt=True
    )
    image_inputs, video_inputs, video_kwargs = process_vision_info(messages, return_video_kwargs=True)
    inputs = self.processor(
      text=[text],
      images=image_inputs,
      videos=video_inputs,
      # fps=fps,
      padding=True,
      return_tensors="pt",
      **video_kwargs,
    ).to(self.model.device)

    # run the model
    generated_ids = self.model.generate(**inputs, max_new_tokens=128)

    # handle the generated output
    generated_ids_trimmed = [
      out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
    ]
    output_text = self.processor.batch_decode(
      generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
    )
    print(output_text)

    # print("outputs:", outputs)
    # msg = self.processor.decode(outputs[0][inputs["input_ids"].shape[-1]:])
    # print(msg)

    return Qwen25VLResponse(message=output_text[0])