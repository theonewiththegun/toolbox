# Toolbox
### A set of convenience tools for data science.
This package as of now consists of the following submodules:

## Projects
    
This submodule contains function to make starting, managing and sharing data-projects easier. The goal is to give the user an opportunity to use any tools they like and automate as many routine steps of managing the project as possible.

The basic project consists of your code, your `data` folder and your `output` folder. 

The `data` folder should be used to store everything you have at the start of the project and anything else that needs processing or helps you to solve your tasks.

The `output` folder should contain any preliminary of final results of your work.

You may also put and arbitrary number of any file type to the `templates` folder within the module to copy those file to a just initiated project. E.g. you may put a sample `ipynb` file with your regular imports and snippets there and it will be copied to your project the moment you initiate it.
## Settings

This is a set of conveniece functions for handling diffirent variables on disk, like persistent constants or important env variables. This module uses `json` as the main storage format so it can hold deep nested structure.


## Utils

This is a set of functions that helps other submodules or helps you with misc stuff.