import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

file = openai.File.create(
  file=open("data/09-06_chat.jsonl", "rb"),
  purpose='fine-tune'
)


tune_job = openai.FineTuningJob.create(training_file='file-s85K5b9KeE6uTmfNPt4MfGDY', model="gpt-3.5-turbo")

# List 10 fine-tuning jobs
openai.FineTuningJob.list(limit=10)

# Retrieve the state of a fine-tune
openai.FineTuningJob.retrieve(tune_job['id'])

# Cancel a job
#openai.FineTuningJob.cancel(tune_job['id'])

# List up to 10 events from a fine-tuning job
openai.FineTuningJob.list_events(id=tune_job['id'], limit=10)

# Delete a fine-tuned model (must be an owner of the org the model was created in)
#openai.Model.delete("ft-abc123")

completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo:my-org:custom_suffix:id",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)