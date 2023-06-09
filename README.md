## Shoutout to Kai Greshake
- who came up with this idea.
https://github.com/greshake/unreal-project-extractor/

# File Fantasy Bash Sim Agent (BSA)

File Fantasy Bash Sim Agent (BSA) is an AI-driven tool leveraging the hallucination capabilities of GPT to simulate a git repository. It interacts with a simulated terminal to generate and parse output, mimicking the operation of a real git repository.

## How it Works:

1. GPT simulates a terminal using `sysmsg1`.
2. The simulation starts with a project. Each project has a name, a description, and a GitHub link.
3. A new folder is created and the terminal navigates into this folder.
4. GPT then hallucinates a git repository by simulating the clone command.

## Usage:

Below is an example of how to use BSA:

# Project introduction
Name: snakepy 
Description: A simple snake game written in python. Does not use any external assets.
GitHub-Link: https://github.com/snakegamefactory/snakepy.git

# Required steps to simulate a git repository
$ mkdir <newfolder>
$ cd <newfolder>
$ git clone <https://github.com/snakegamefactory/snakepy.git>
$ find . -type f
$ cd <repo>
$ cat <filenames>
  
If you are unsatisfied with a `cat` response, use the `-m clear` command twice to clear the context window up to the last LLM response.

Afterwards, you can attempt to run the generated files.

## Examples 2 - Calculator:
  
# Project introduction
Name: calculatorgui 
Description: A simple calculator written in python using a GUI.
GitHub-Link: https://github.com/calculatorfactory/calculatorgui.git

Remember to follow the required steps as detailed in the "Usage" section above.
  
Enjoy exploring the world of simulated repositories with BSA!

# SYSTEM MESSAGE
  
You are simulating a Linux terminal. The user can input commands prefixed with $ like this:
$ <bash command>
to get the terminal output. They can also type in regular natural language prompts. Any repository that the user tries to clone exists. Generate simulate output without any wrapper characters.
