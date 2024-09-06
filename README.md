# Data Center UI
[This project is a part of my intern program at `AiAiVN`]

Resources owers: `AiAiVN`, `SCG groups`

## Overview

### Parent project
We are buiding a customized chatbot for tourism-related services such as: hotel, restaurant, etc. 
The technology we use is based on RAG, OpenAI within the internal data

### We ran into problems
#### *Lack of data*
The raw data from data partner is not enough. For example, the raw data of hotel has only its name, phone number. 

However, high-performance chatbot need more details such as name, phone number, type of room, price, its view, etc.

#### *Many different data structure*
There are many type of data: table of many items, table of many details of one item. It makes us difficult to group and check data

### Solution proposed (this project)
We proposed a platform manage the whole data for chatbot, provide an UI for low-tech / non-tech team to verify data

## Pages in the app
* `Home` : greeting and tutorials (log in required)
* `Login`/`Log out` : login platform using st authenticator
* `Tasks`: the overview of doc need verification and the editor as well
* `Profile`: user's details and something related to UX

## Local deployment
Run the command `streamlit run router.py`

## Secrets and user information
* Config user details at `users.yaml`
* Config your own secrets at `.streamlit/secrets.toml`

## Some notice
In `Login` page, for login submission, please **double click `Login`/press `Enter`**

This may due to the customized tool I used/OS/keyboard, I will try to fix this issue later