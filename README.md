# Building Chatbot using NLTK
First a terminal chatbot then integrate this to messaging app to do trading.

### Installation of NLTK
```
pip3 install nltk
```
### Installing required packages
After NLTK has been downloaded, install required packages
```
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading popular packages
nltk.download('punkt') 
nltk.download('wordnet') 
```

## How to run
```
python3 chatbot.py
```
