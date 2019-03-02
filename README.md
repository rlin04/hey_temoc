## Hey Temoc
Voice Activated UTD FAQ

## Our Team
We are a group of students looking for ways to create a project that has a real impact on the UTD community. Starting from a near blank slate knowledge base regarding Smart Assistant development, we learned about and successfully created our Alexa Skill, Hey Temoc over the course of twenty-four hours.

## The Project
Hey Temoc is an Alexa skill that allows students and visitors to UTD to ask and receive up to date answers about the university through the Alexa app on mobile or an Amazon Echo device. Students lead busy lives, and as the name suggests, have many frequently asked questions. Furthermore, university specific information can't always be found though a quick search. Hey Temoc solves this problem by allowing students to find the solutions to their problems just by asking.

## Implemention
We used the Alexa developer console and JSON to set up the initial Alexa Skill activation and keyword recognition. Our back-end was created using AWS Lambda to call functions. This involved the usage of the Beautiful Soup Python library to scrape question and answer data from the UTD FAQ website into a CSV. This information is scraped and process at the start of the invocation of the Alexa skill to ensure that the information is up to date. We then processed the set of questions and answers and assigned relevant intents and slots to link appropriate pairs. 

## Future Goals
Although we used a Beautiful Soup to get the data we needed for Hey Temoc, we also explored the option of using a web API. Additional uses for Hey Temoc could also include providing directions to specified classrooms through the UTD Room Locator and academic performance/grading policy analysis.

## Thank You
We thoroughly enjoyed our time at HackUTD and look forward to future hackathons to come!
