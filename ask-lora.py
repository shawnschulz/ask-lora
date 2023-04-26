from optparse import OptionParser
import sys
from transformers import LlamaForCausalLM, LlamaTokenizer



#default args
memory_dir = "/home/shawn/datasets/lora_memory/"
from_online = False
save_model = False
path_to_model= "/home/shawn/datasets/LLMs/llama_7b" 

#flags
parser = OptionParser()
#group = parser.add_argument_group('group')
parser.add_option('--prompt', dest="prompt", type=str, help='The Prompt for the LLM')
parser.add_option('--memory_dir', dest="memory_dir", type=str,
                    help='Optional, specify a direcotry containing a context.txt file for the LLM')
parser.add_option('--path_to_model',  dest="path_to_model", type=str,
                    help='Optional, specify a quantized model binary')
(options, args) = parser.parse_args()

#if args.from_online and args.require_online and not args.save_model:
#    parser.error('--arg2 is required if --arg1 is present')


prompt = options.prompt

if options.memory_dir:
    memory_dir = options.memory_dir
if options.path_to_model:
    path_to_model = options.path_to_model



def ask_lora(prompt, memory_path):
    llm = Llama(model_path=path_to_model)
    with open(memory_dir + 'context.txt', 'r+b') as f:
        contents = f.read().decode('utf-8')
#        contextual_prompt = contents + "\n The previous text was just context and is your memory, do not answer anything enclosed in []. Please answer the following question only Q: " + prompt           
        output = llm("Q: " + prompt + " A:", max_tokens=32, stop=["Q:", "\n"], echo=True)
        new_context = output["choices"][0]["text"]
        #save additional context
        f.write(bytes(new_context, 'utf-8'))
        #save the model again (this could either be extremely important or useless idk lol)
    f2 = open(memory_dir + 'dataset.json', 'r+b')
    f2.write(bytes(str(output), 'utf-8'))
    print(output) 
    return(output)

ask_lora(prompt, memory_dir)
