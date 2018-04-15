The HQ Trivia bot can answer questions correctly with accuracy of around 83%. That's usually 10/12 questions

How it works:
- I mirror my phone's screen on the computer
- as a question is presented I take a screenshot and scan it for text using Google’s Vision API
- Than I search the question on Google using the Google Custom Search Engine API 
- I scan the 9 results the API returns and give each answer a score based on how many times it occurs in the snippet and it's title

I use the nltk library to parse the answers using natural language processing to improve my search results.
To succesfully run it you need to have to have a Google Cloud account with Google’s Vision API and Google Custom Search Engine API anabled. Than you will need to insert the key and custom search engine ID on lines 83 and 84 of the trivia.py file. You can get those from your Google Cloud account -> https://cloud.google.com/video-intelligence/docs/common/auth