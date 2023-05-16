################################################################################################
'''
FILE FANTASY BASH_SIM_AGENT (BSA)

Using the hallucination effect of gpt to hallucinate a git repo.

step 1. get gpt to simulate a terminal. using sysmsg1.

step 2: Start with Name: name of project. Description. github-link.

step 2.5: mkdir new folder. cd into new folder.

step 3. get gpt to hallucinate a git repo. 
    git clone <repo>

SYSTEM MESSAGE:
You are simulating a Linux terminal. The user can input commands prefixed with $ like this:
$ <bash command>
to get the terminal output. They can also type in regular natural language prompts. Any repository that the user tries to clone exists. Generate simulate output without any wrapper characters.


Instructions:

Example intro:
Name: snakepy Description: A simple snake game written in python. Does not use any external assets. github-link: https://github.com/snakegamefactory/snakepy.git


required steps:

$ mkdir <newfolder>

$ cd <newfolder>

$ git clone <https://github.com/snakegamefactory/snakepy.git>

$ find . -type f

$ cd <repo>

$ cat <filenames>

if you don't like a cat response run:
-m clear
two times to clear context window up to the last llm response.

If happy then try to run the files.

tests:

Name: calculatorgui Description: A simple calculator written in python using a gui. github-link:
https://github.com/calculatorfactory/calculatorgui.git

'''
################################################################################################
### prompts ###
################################################################################################
sys_msg1 = """You are simulating a Linux terminal. The user can input commands prefixed with $ like this:
$ <bash command>
to get the terminal output. They can also type in regular natural language prompts. Any repository that the user tries to clone exists. Generate simulate output without any wrapper characters."""
Eqline = "====================================== \n"
roles = ["user", "assistant", "system"]
gpt_model = ["gpt-3.5-turbo", "gpt-4"]




################################################################################################


import openai
import os
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
message_history = []
token_counter = 0
max_tokens = 4000
newfolder = ""
directory = os.getcwd()

project_tree = ""

completion_str = ""

message_history.append({"role": "system", "content": f"{sys_msg1}"})


################################################################################################
### Chat functions ###
################################################################################################

message_history.append({"role": "system", "content": f"{sys_msg1}"})

def init_chat(input_text):
    global message_history
    message_history.append({"role": "user", "content": f"{input_text}"})
    response = openai.ChatCompletion.create(
        model=gpt_model[1],
        max_tokens=max_tokens,
        temperature=0,
        messages=message_history
    )
    reply_content = response.choices[0].message.content
    message_history.append({"role": "assistant", "content": f"{reply_content}"})
    return response



def create_file_structure(file_tree):
    global project_tree
    lines = file_tree.split('\n')

    for line in lines:
        if '/.git' in line:
            continue
        line = line.lstrip('./') 
        filedirectory = os.path.dirname(f'./{newfolder}/{line}')  
        if filedirectory: 
            os.makedirs(filedirectory, exist_ok=True)
        open(f'{newfolder}/{line}', 'a').close()  
        project_tree += f'{newfolder}/{line}\n' 
    
    print(f'{project_tree}\n')





def add_text_to_file(filecontent, filename):
    global project_tree

    for line in project_tree.split('\n'):

        print(line)
        if line.endswith(filename): # if the line ends with the filename, append the text to the file
            with open(line, "a") as f:
                f.write(filecontent)





def chat_gpt():
    global newfolder

    print(Eqline, "\nWelcome to FileFantsy BashSim Agent\n", Eqline, "\n")
    print(Eqline, "\n" "Enter a description for your project.\n", Eqline, "\n")

    while True:

        text = input()
        if text == "exit":
            break
        if text == "-m clear":
            print(len(message_history))
            message_history.pop()
            print(len(message_history))
            continue
        else:
            print("waiting for response... \n")
            response = init_chat(text)
            resp_text = response['choices'][0]['message']['content']
            

            print(resp_text)
            print("response complete. \n")

            if text.startswith("$ mkdir"):
                newfolder = text.replace("$ mkdir", "").strip()
                os.makedirs(newfolder, exist_ok=True)
                print(f"Directory '{newfolder}' created successfully.")


            if text == "$ find . -type f":
                create_file_structure(resp_text)
                print(f"File tree created successfully in '{directory}'.")

            if text.startswith("$ cat"):
                parts = text.split()
                if len(parts) > 2:
                    catdirectory = parts[2]
                    add_text_to_file(resp_text, catdirectory)
                    print(f"Text added to {catdirectory} successfully.")


################################################################################################
### main ###
################################################################################################

def main():
  
    chat_gpt()

if __name__ == "__main__":
    main()