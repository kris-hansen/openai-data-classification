# OpenAI Data Classification

I spun this up quickly as an example to see how well the [openai](https://beta.openai.com) davinci engine could be used to classify and identify different levels of PII data.

The use case here is multi-faceted: if I am scanning a file for PII I'd like more than just a boolean view of whether it contains PII or not, it's more useful to see what type of PII and the level of combined PII risk associated with the contents / payload / response. Different classification levels can have different treatments so being able to sample and detect and then apply a treatment or control becomes useful.

It is interesting to see how AI models think about and consider PII data. It's also interesting to see how well they can classify and identify different types of PII data. I'm sure there are many other use cases for this type of classification.

The original version of this used the classification model but has been updated to use the completion model. The completion model is a bit more flexible and allows for more complex queries and responses. The classification model is more limited in that it only allows for a single classification per query. Part of the analysis is whether the completion model is suited to this type of 'PII detection' task.

It is also interesting to swap out the davinci engine for others such as curie and see how they perform.

* this is for simulated PII use only, not for real world use *

## Instructions

1. Clone or fork the repo
2. Insert your super secret openapi API key in the .env file
3. Source the env file with `source .env`
4. Run with `python classify.py`
5. Check the prediction!

## Results

Overall, it seems like some PII fares better than others when it comes to classification. Davinci seems to err on the side of caution (which is good) but would also result in quite a few false positives. It seems to do a good job of the obvious None scenarios like "hello" and it seems to understand credit card structures and things like names and phone numbers quite well but stumbles on SSN structures and what is a valid area/group coding vs. completely random numbers. Perhaps it could be trained / fine tuned in a more focused way?

## Requirements

Tested with python 3.9.7 and openai Python client library version 0.23.0