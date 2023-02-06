import os
import numpy as np
import requests as re
import textwrap
import tiktoken
from bs4 import BeautifulSoup as bs


# download data of questions
file_path_train  = os.path.join(os.path.dirname(__file__), 'train_input.txt')
file_path_val = os.path.join(os.path.dirname(__file__), 'val_input.txt')

if not os.path.exists(file_path_train) and not os.path.exists(file_path_val):
    train_data_url = 'https://willsketch.github.io/Data/questions_train'
    val_data_url = 'https://willsketch.github.io/Data/questions_val'
    response_train = re.get(train_data_url).content
    response_val = re.get(val_data_url).content

    soup_train = bs(response_train, features='lxml')
    soup_val = bs(response_val, features='lxml')

    with open(file_path_train, 'w') as f:
        data = textwrap.dedent(soup_train.find('p').text)
        f.write(data)

    with open(file_path_val, 'w') as f:
        data = textwrap.dedent(soup_val.find('p').text)
        f.write(data)

#train_data
with open(file_path_train, 'r') as f:
    train_data = f.read()

with open(file_path_val, 'r') as f:
    val_data = f.read()


# encode with tiktoken gpt2 bpe
enc = tiktoken.get_encoding("gpt2")
train_ids = enc.encode_ordinary(train_data)
val_ids = enc.encode_ordinary(val_data)
print(f"train has {len(train_ids):,} tokens")
print(f"val has {len(val_ids):,} tokens")

# export to bin files
train_ids = np.array(train_ids, dtype=np.uint16)
val_ids = np.array(val_ids, dtype=np.uint16)
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))
val_ids.tofile(os.path.join(os.path.dirname(__file__), 'val.bin'))
