The only thing I've really added so far is some code to prompt dolly with context from a context.txt file located in the repo directory, might update this in the future to use a proper json file rather than just appending text to the same text file.  

clone the repo: 

```
git clone https://github.com/shawnschulz/ask-lora.git
```

cd into the cloned repo and run 

```
pip install -r requirements
```

Run
```
python3 ask-lora.py --memory_dir /path/to/ask-lora --model_path /path/to/model --prompt "Hello! How are you?" 
```

I also recommend adding an alias to your .bashrc for convenience:
```
#add this to your .bashrc!
alias ask_lora='python3 /path/to/ask-lora/ask-lora.py --memory_dir /path/to/ask-lora --model_path /path/to/model --prompt '
```
To-do's:

- Make some proper files to save the memory datase to a vector databaset
- Test what works best for prompting it based on memory (enclose the prompt in brackets?)
- Add some kind of interactive mode 
- Experiment with other ways to instruction fine-tune the model

Link to databricks repo:
https://huggingface.co/databricks/dolly-v2-7b
 
