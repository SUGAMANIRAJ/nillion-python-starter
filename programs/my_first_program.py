


#Securely computing the average sentiment score of customer reviews across different products. 
#This can help businesses analyze customer feedback while preserving the privacy of individual reviews.


"""
Secure Average Sentiment Score Calculation from Customer Reviews
no.of.products: p = 3
no.of.reviews per product: r = 2

"""

from nada_dsl import *

def nada_main():

    #Parties 
    product0 = Party(name="product0")
    product1 = Party(name="product1")
    product2 = Party(name="product2")
    outparty = Party(name="outparty")

   
    ## Sentiment scores from product 0 reviews
    p0_r0_sentiment = SecretInteger(Input(name="p0_r0_sentiment", party=product0))
    p0_r1_sentiment = SecretInteger(Input(name="p0_r1_sentiment", party=product0))
    
    ## Sentiment scores from product 1 reviews
    p1_r0_sentiment = SecretInteger(Input(name="p1_r0_sentiment", party=product1))
    p1_r1_sentiment = SecretInteger(Input(name="p1_r1_sentiment", party=product1))

    ## Sentiment scores from product 2 reviews
    p2_r0_sentiment = SecretInteger(Input(name="p2_r0_sentiment", party=product2))
    p2_r1_sentiment = SecretInteger(Input(name="p2_r1_sentiment", party=product2))

    ## Calculate total sentiment score and count of reviews for each product
    total_sentiment_p0 = p0_r0_sentiment + p0_r1_sentiment
    total_reviews_p0 = Integer(2)
    
    total_sentiment_p1 = p1_r0_sentiment + p1_r1_sentiment
    total_reviews_p1 = Integer(2)
    
    total_sentiment_p2 = p2_r0_sentiment + p2_r1_sentiment
    total_reviews_p2 = Integer(2)

    ## Calculate average sentiment score for each product
    avg_sentiment_p0 = total_sentiment_p0 / total_reviews_p0
    avg_sentiment_p1 = total_sentiment_p1 / total_reviews_p1
    avg_sentiment_p2 = total_sentiment_p2 / total_reviews_p2

    #Output
    avg_sentiment_p0_output = Output(avg_sentiment_p0, "average_sentiment_product0", outparty)
    avg_sentiment_p1_output = Output(avg_sentiment_p1, "average_sentiment_product1", outparty)
    avg_sentiment_p2_output = Output(avg_sentiment_p2, "average_sentiment_product2", outparty)

    return [avg_sentiment_p0_output, avg_sentiment_p1_output, avg_sentiment_p2_output]


#This program ensures the security and privacy of reviews given by the customers by the using the Secret Datatype inside the network.
#Without Comprimising the security of customers, Companies can calculate the avg sentimets on products

