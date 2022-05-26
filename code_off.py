def find_disarium(start_page, end_page):

    if start_page > end_page:
        temp = start_page
        start_page = end_page
        end_page = temp
    
    expected_inputs = []
    for i in range(1, 3000000):
        expected_inputs.append(str(i))
 
    if (str(start_page) not in expected_inputs) or (str(end_page) not in expected_inputs):
        print("Please enter valid page numbers!")
        return
    
    for page in range (start_page, end_page + 1):
        number_list = []
        index_list = []
        number_string = str(page)
        counter = 0
        
        for char in number_string:
            counter += 1
            number_list.append(int(char))
            index_list.append(int(counter))
        
        total = 0
        for i in range(len(number_list)):
            total += number_list[i] ** index_list[i]

        if page == total:
            print(page)
        #print(number_list, index_list, total)

find_disarium(1, 600)
find_disarium(-1, 10)
find_disarium(600,1)
find_disarium("hey", "p")
