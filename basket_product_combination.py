from itertools import combinations

consumer_basket_sample = ["bread-orange-soap",
                          "paper-chocolate",
                          "chocolate",
                          "hot-dog-milk",
                          "hot-dog",
                          "finger-nail-bread",
                          "bread", "orange",
                          "tee-shirt-bread",
                          "soap",
			  "paper",
                          "tee-shirt",
                          "milk",
                          "finger-nail",
                          "orange-bread-hot-dog-milk",
                          "tee-shirt-hot-dog",
                          "tee-shirt-hot-dog-arc-en-ciel-milk",
                          "bread"]

special_cases = ["tee-shirt", "finger-nail", "hot-dog", "arc-en-ciel"]

def get_baskets():
    baskets = []  
    for i in range(len(consumer_basket_sample)):

        for j in range(len(special_cases)):
            if(consumer_basket_sample[i].find(special_cases[j]) >= 0):
                case_temp = special_cases[j].replace('-', ':')
                consumer_basket_sample[i] = consumer_basket_sample[i].replace(special_cases[j], case_temp)  
        
        basket = consumer_basket_sample[i].split('-')
        for i in range(len(basket)):
            basket[i] = basket[i].replace(':', '-') 
        baskets.append(basket)
    return baskets


def order_baskets(baskets):
    return sorted(baskets, key=len)


def get_products(baskets):   
    products = []   
    for basket in baskets:
        for product in basket:
            products.append(product)
            
    products = list(set(products)) 
    return products


def get_basket_combination_by_size(products, max_size):
    basket_combination_by_size = []
    for i in range(1, max_size+1):  
        combination_list = list(combinations(products, i))

        combinations_str = []       
        for items in combination_list:
            combination_str = "" 
            for item in items:
                combination_str += item + "-"
            combination_str = combination_str[:-1]
            combinations_str.append(combination_str)         
        combination_str = combination_str[:-1]      
        basket_combination_by_size.append(combinations_str)
        
    return list(basket_combination_by_size)

        
def main():
    
    print("===== ORDERED BASHETS =====")
    baskets = get_baskets()
    baskets = order_baskets(baskets)
    for basket in baskets:
        print(basket)
 
    print("===== ALL PRODUCTS =====")
    products = get_products(baskets)
    print(products)
    
    print("===== BASHETS COMBINAISON BY SIZE =====")
    basket_combination_by_size = get_basket_combination_by_size(products, 3)
    i = 1
    for basket_combination in basket_combination_by_size:
        print("")
        print("BASHETS COMBINAISON OF SIZE", i, ":")
        print(basket_combination)
        i = i + 1

if __name__ == "__main__":
    # execute only if run as a script
    main()
