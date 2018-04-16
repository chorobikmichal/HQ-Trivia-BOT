## The HQ Trivia bot can answer questions correctly with accuracy of around 83%. That's usually 10/12 questions

## How it works:
- I mirror my phone's screen on the computer
- as a question is presented I take a screenshot and scan it for text using Google’s Vision API
- Than I search the question on Google using the Google Custom Search Engine API 
- I scan the 9 results the API returns and give each answer a score based on how many times it occurs in the snippet and its title

## How to use:
Simply run 'python trivia.py'<br />
Than drag the mouse highlighting the question<br />
The likely answer is the one with the highest score

I use the nltk library to parse the answers using natural language processing to improve my search results so you will need to install nltk. To successfully run the bot you need to also have to have a Google Cloud account with Google’s Vision API and Google Custom Search Engine API enabled. Than you will need to insert the key and custom search engine ID on lines 83 and 84 of the trivia.py file. You can get those from your Google Cloud account. https://cloud.google.com/video-intelligence/docs/common/auth

## Examples:
 <img src="https://user-images.githubusercontent.com/24882037/38785142-146bb92a-40ea-11e8-86fe-1615b8693cba.gif">  <img src="https://user-images.githubusercontent.com/24882037/38785152-23613c02-40ea-11e8-87f7-714810afecd6.jpg" height="55%" width="35%"> 

 <img src="https://user-images.githubusercontent.com/24882037/38785143-1486a03c-40ea-11e8-9332-1a710a6d95b4.gif">  <img src="https://user-images.githubusercontent.com/24882037/38785153-2374fe7c-40ea-11e8-8000-40ca2544a55f.jpg" height="55%" width="35%">
 
 <img src="https://user-images.githubusercontent.com/24882037/38785144-14964b68-40ea-11e8-8c61-d4e3ccfa5cc1.gif">  <img src="https://user-images.githubusercontent.com/24882037/38785157-29bc9e2a-40ea-11e8-9219-493156502810.jpg" height="55%" width="35%">
 
