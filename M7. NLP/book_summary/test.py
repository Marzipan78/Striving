from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
src_text = [
    """ A tropical storm system is threatening to unleash flash flooding and mudslides on the area of Haiti where a 7.2-magnitude earthquake killed almost 1,300 people on Saturday.Tropical Depression Grace was approaching the southern coast of Hispaniola, the island comprising Haiti and the Dominican Republic, early Monday bringing with it sustained winds of 35 mph (56 km/h), and higher gusts, CNN meteorologist Haley Brink said.Tropical storm conditions are possible in the Dominican Republic and Haiti later today, Brink said, adding that several inches of rain are forecast -- with up to 15 inches (38 centimeters) possible in some isolated areas -- through Tuesday."I am worried about the upcoming storm as it can complicate the situation for us," Jerry Chandler, head of Haiti's civil protection agency, said on Sunday."""
]

model_name = 'google/pegasus-xsum'
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)
batch = tokenizer(src_text, truncation=True, padding='longest', return_tensors="pt").to(device)
translated = model.generate(**batch)
tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
#assert tgt_text[0] == "California's largest electricity provider has turned off power to hundreds of thousands of customers."
print(tgt_text[0])