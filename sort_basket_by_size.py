
consumer_basket_sample = ["bread-orange-soap",
                          "paper-chocolate",
                          "chocolate",
                          "hot-dog-milk",
                          "hot-dog",
                          "finger-nail-bread",
                          "bread", "orange",
                          "tee-shirt-bread",
                          "soap", "paper",
                          "tee-shirt",
                          "milk",
                          "finger-nail",
                          "orange-bread-hot-dog-milk",
                          "tee-shirt-hot-dog",
                          "bread"]

special_cases = ["tee-shirt", "finger-nail", "hot-dog"]

def create_basket_combination():

    basket_combination = []
    
    for i in range(len(consumer_basket_sample)):

        for j in range(len(special_cases)):
            if(consumer_basket_sample[i].find(special_cases[j]) >= 0):
                case_temp = special_cases[j].replace('-', ':')
                consumer_basket_sample[i] = consumer_basket_sample[i].replace(special_cases[j], case_temp)  
        
        basket = consumer_basket_sample[i].split('-')
        for i in range(len(basket)):
            basket[i] = basket[i].replace(':', '-') 
        basket_combination.append(basket)
    return basket_combination


def order_basket_combination(basket_combination):
    return sorted(basket_combination, key=len)


def main():
    result = create_basket_combination()
    result = order_basket_combination(result)
    for i in range(len(result)):
        print(result[i])

if __name__ == "__main__":
    # execute only if run as a script
    main()
