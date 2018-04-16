##The HQ Trivia bot can answer questions correctly with accuracy of around 83%. That's usually 10/12 questions

##How it works:
- I mirror my phone's screen on the computer
- as a question is presented I take a screenshot and scan it for text using Google’s Vision API
- Than I search the question on Google using the Google Custom Search Engine API 
- I scan the 9 results the API returns and give each answer a score based on how many times it occurs in the snippet and its title

##How to use:
Simply run ##python trivia.py
Than drag the mouse highlighting the question
The likely answer is the one with the highest score

I use the nltk library to parse the answers using natural language processing to improve my search results.
To successfully run it you need to have to have a Google Cloud account with Google’s Vision API and Google Custom Search Engine API enabled. Than you will need to insert the key and custom search engine ID on lines 83 and 84 of the trivia.py file. You can get those from your Google Cloud account -> https://cloud.google.com/video-intelligence/docs/common/auth

Examples:
![1](https://user-images.githubusercontent.com/24882037/38785142-146bb92a-40ea-11e8-86fe-1615b8693cba.gif) ![img_6613](https://user-images.githubusercontent.com/24882037/38785152-23613c02-40ea-11e8-87f7-714810afecd6.jpg)

![2](https://user-images.githubusercontent.com/24882037/38785143-1486a03c-40ea-11e8-9332-1a710a6d95b4.gif) ![img_6663](https://user-images.githubusercontent.com/24882037/38785153-2374fe7c-40ea-11e8-8000-40ca2544a55f.jpg)

![3](https://user-images.githubusercontent.com/24882037/38785144-14964b68-40ea-11e8-8c61-d4e3ccfa5cc1.gif) ![1518756030870](https://user-images.githubusercontent.com/24882037/38785157-29bc9e2a-40ea-11e8-9219-493156502810.jpg)

